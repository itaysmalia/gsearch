#!/usr/bin/env python3

import argparse
from sys import argv
from webbrowser import open
from requests import get
from bs4 import BeautifulSoup as bs
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results", help="Open results by index")
    parser.add_argument("-q", "--query", help="search query",nargs='+')
    args = parser.parse_args()

    print("searched: {} opening results: {}".format(
            args.query,
            args.results
            ))

    if not len(args.results):
        open(f"https://www.google.com/search?q={'+'.join(args.query)}")
    else:
        soup = bs(get(f"https://www.google.com/search?q={'+'.join(args.query)}").content)
        arr = soup.find_all('a')
        filtered_arr = [a for a in arr if a['href'][1:4] == 'url']
        #print("\n".join(map(str,filtered_arr)))
        for i in map(int,args.results):
            print(i)
            open(f"https://www.google.com{filtered_arr[i]['href']}")

if __name__ == "__main__":
    main()


