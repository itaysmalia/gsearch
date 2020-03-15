#!/usr/bin/env python3
open_file = open
import argparse
from sys import argv
from webbrowser import open,open_new_tab
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
bigsites={1:"stackoverflow.com",2:"github.com",3:"stackify.com",4:"medium.com",5:"quora.com",6:"redis7.com"}

def print_intro():
    with open_file("./icon.txt","r") as file:
        print(file.read())
    sleep(0.5)
    print()
    print("Made by")
    sleep(0.5)
    print()
    with open_file("./by.txt","r") as file:
        print(file.read())
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
    print("searching {}{}{}{}".format(
        f"{' '.join(args.query)} ",
        f"open results: {','.join(args.results or '')} ",
        f"from websites: {', '.join(all_sites or '')} ",
        "but listing first " if args.list else ""))
    
    query = '+'.join(args.query)
    url="https://www.google.com/search?q="
    if args.bigsite:
            query += " |".join([f" site:{bigsites[int(x)]}" for x in args.bigsite])
    if args.site:
        query += " |".join([f" site:{x}" for x in args.site])
    if not args.results:
        if args.list:
            #list
            arr=get_filtered_links(f"{url}{query}")
            for i,v in zip(range(1,11),arr[:10]):
                print(f"{i}) {v.find('h3').text}")
            arr_of_indexes = list(map(int,input("=> ").split()))
            print(arr_of_indexes)
            for i in arr_of_indexes:
                open(arr[i-1]['href'],new=2,autoraise=False)
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
        for i in args.results:
            open(filtered_arr[i-1]['href'],new=2,autoraise=False)


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


