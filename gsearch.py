#!/usr/bin/env python3
open_file = open
import argparse
from sys import argv
from webbrowser import open,open_new_tab
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread
from time import sleep
bigsites={1:"stackoverflow.com",2:"github.com",3:"stackify.com",4:"medium.com",5:"quora.com"}
def main():
    parser = argparse.ArgumentParser(description="BIG Sites: "+', '.join('{} - {}'.format(k,v) for k,v in bigsites.items()))
    parser.add_argument("-q", "--query", help="search query",nargs='+')
    parser.add_argument("-r", "--results", help="Open results by order (1 for first search result)",nargs='+')
    parser.add_argument("-S", "--bigsite", nargs="+",help=f"Search ONLY from the specifics bigsites.")
    args = parser.parse_args()
    if not args.query:
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
        parser.print_help()
        return
    print("searched: {} opening results: {} from websites: {}".format(args.query,args.results,[bigsites[int(x)] for x in args.bigsite] if args.bigsite else "all"))
    query = '+'.join(args.query)
    url="https://www.google.com/search?q="
    if args.bigsite:
            query += " |".join([f" site:{bigsites[int(x)]}" for x in args.bigsite])
    if not args.results:
        open(f"{url}{query}")
    else:
        try:
            args.results=list(map(int,args.results))
        except:
            parser.print_help()
            return
        soup = bs(get(f"{url}{query}").content,'html.parser')
        arr = soup.find_all('a')
        filtered_arr = [a for a in arr if a['href'][1:4] == 'url']
        #print("\n".join(map(str,filtered_arr)))
        for i in map(int,args.results):
            open(f"https://www.google.com{filtered_arr[i-1]['href']}",new=2,autoraise=False)

if __name__ == "__main__":
    main()


