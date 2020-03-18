#!/usr/bin/env python3
open_file = open
import argparse
import os
import sys
from webbrowser import open,open_new_tab
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread
from time import sleep
import clipboard
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
bigsites={1:"stackoverflow.com",2:"github.com",3:"stackify.com",4:"medium.com",5:"quora.com",6:"redis7.com"}

def print_intro():
    home = os.path.expanduser("~")
    try:
        with open_file(home+"/.gsearch/icon.txt","r") as file:
            print(file.read())
    except:
        sys.exit("gsearch is not installed")
    sleep(0.5)
    print()
    print("Made by")
    sleep(0.5)
    print()
    try:
        with open_file(home+"/.gsearch/by.txt","r") as file:
            print(file.read())
    except:
        sys.exit("gsearch in not installed")
    sleep(0.5)

def main():
    parser = argparse.ArgumentParser(description="BIG Sites: "+', '.join('{} - {}'.format(k,v) for k,v in bigsites.items()))
    parser.add_argument("-q",
                         "--query",
                        help="search query",
                        nargs='+')
    
    parser.add_argument("-r",
                        "--results",
                        help="Open results by order (1 for first search result)",
                        nargs='+')
    
    parser.add_argument("-c",
                        "--copy",
                        action='store_true',
                        help="copy url to clipboard instead of open it in the webbrowser")
    
    parser.add_argument("-s",
                        "--site",
                        nargs="+",
                        help="Search ONLY from those sites.")
    
    parser.add_argument("-S",
                        "--bigsite",
                        nargs="+",
                        help="Search ONLY from the specifics bigsites.")
    
    parser.add_argument("-l",
                        "--list",
                        action='store_true',
                        help="list n the first 10 search result, cant go with -r.")
    parser.add_argument("-i",
                        "--insite",
                        nargs="+",
                        help="Search sites that contains this values")
    args = parser.parse_args()
    
    if not args.query: #print intro and help
        print_intro()
        parser.print_help()
        return 
    
    all_sites = []
    all_sites += args.site or []
    all_sites += args.bigsite or []
    print("searching {}{}{}{}{}.".format(
        f"{' '.join(args.query)} ",
        f"open results: {','.join(args.results)} " if args.results else "",
        f"from websites: {', '.join(all_sites)} " if all_sites else "",
        "but listing first " if args.list else "",
        "and coping url at end" if args.copy else ""))
    
    query = '+'.join(args.query)
    url="https://www.google.com/search?q="
    if args.bigsite:
            query += " |".join([f" site:{bigsites[int(x)]}" for x in args.bigsite])
    if args.site:
        query += " |".join([f" site:{x}" for x in args.site])
    if args.insite:
        query += " |".join([f" insite:{x}" for x in args.insite])
    if not args.results:
        if args.list:
            arr=get_filtered_links(f"{url}{query}")
            for i,v in enumerate(arr[:10]):
                print(f"{i + 1}) {v.find('h3').text}")
            arr_of_indexes = list(map(int,input("=> ").split()))
            if args.copy:
                clipboard.copy(arr[arr_of_indexes[-1]-1]['href'])
            else:
                for i in arr_of_indexes:
                    open(arr[i-1]['href'],new=2,autoraise=False)
        else:
            if args.copy:
                clipboard.copy(f"{url}{query}")
            else:
                open(f"{url}{query}")
    else:
        if args.list:
            print("-r/--results cant go with -l/--list!!!")
            return
        try:
            args.results=list(map(int,args.results))
        except:
            parser.print_help()
            return
        filtered_arr = get_filtered_links(f"{url}{query}")
        if args.copy:
            clipboard.copy(filtered_arr[-1]['href'])
        else:
            for i in args.results:
                open(filtered_arr[i-1]['href'],new=2,autoraise=False)
    if args.copy:
        print("copied succesfuly to clipboard")


def get_filtered_links(full_url):
    soup = bs(
        get(
            full_url,
            headers=headers
            )
            .content,'html.parser'
        )
    arr = soup.find_all('a')
    links_array = [a for a in arr if a.has_attr('href')]
    return [x for x in links_array if x.find("h3")]

if __name__ == "__main__":
    main()


