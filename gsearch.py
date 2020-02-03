#!/usr/bin/env python3

import argparse
from sys import argv
from webbrowser import open,open_new_tab
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread
bigsites={1:"stackoverflow.com",2:"github.com"}
def main():
    parser = argparse.ArgumentParser(description=f"Bigsites are: {' , '.join('{} - {}'.format(k,v) for k,v in bigsites.items())}")
    parser.add_argument("-r", "--results", help="Open results by order (1 for first search result)",nargs='+')
    parser.add_argument("-q", "--query", help="search query",nargs='+')
    parser.add_argument("-S", "--bigsite", 
    help=f"Search ONLY from the specifics bigsites.")
    args = parser.parse_args()
    
    print("searched: {} opening results: {} from websites: {}".format(args.query,args.results,bigsites[int(args.bigsite)] if args.bigsite else "all"))
    if not args.query:
        parser.print_help()
        return
    query = '+'.join(args.query)
    url="https://www.google.com/search?q="
    if args.bigsite:
            query += f" site:{bigsites[int(args.bigsite)]}"
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


