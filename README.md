gsearch made by itay S.M

from now, gsearch your problems.

<code>$ gsearch -q python3 socket PermissionError: [Errno 13] Permission denied</code>

Hello!!
I had an idea to make a program that will help you go another step in your favourite CLI.
gsearch will help you search,filter,list and then open your searches in yout default browser, ready for reading!!


usage: gsearch.py [-h] [-l] [-q QUERY] [-r RESULTS]
                  [-s SITE] [-S BIGSITE]

BIG Sites: 1 - stackoverflow.com, 2 - github.com, 3 - stackify.com, 4 -
medium.com, 5 - quora.com

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list search results in your CLI and open them by index
  -q QUERY [QUERY ...], --query QUERY [QUERY ...]
                        search query
  -r RESULTS [RESULTS ...], --results RESULTS [RESULTS ...]
                        Open results by order (1 for first search result)
  -s SITE, --site SITE  Search ONLY from this soecific site/s
  -S BIGSITE, --bigsite BIGSITE
                        Search ONLY from the specifics bigsite/s.

add gsearch to your commands:
Linux:

<code>
$ chmod +x ./gsearch.py
$ sudo ln -s ./gsearch.py /usr/bin/gsearch
</code>


usage:

<code>./gsearch.py -q python3 docs</code>
=> open google result of searching "python3 docs"

<code>./gsearch.py -l -q python3 docs</code>
=> list 10 first google result of searching "python3 docs" and let you choose which result/s to choose


<code>./gsearch.py -S 1 -q python3 IOError</code>
=> open google result of searching "python3 IOError" but from bufferoverflow.com only (the list is in the help(./gsearch.py -h))

<code>./gsearch.py -s mysite.com mysite2.com -q python3 IOError</code>
=> open google result of searching "python3 IOError" but from mysite.com and from mysite2.com only

<code>./gsearch.py -S 2 -q python3 IOError -r 1</code>
=> searching "python3 IOError" from github.com only and then opening the page of the first result
