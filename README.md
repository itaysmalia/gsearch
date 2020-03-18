gsearch made by itay S.M

from now, gsearch your problems.

<code>$ gsearch -q python3 socket PermissionError: [Errno 13] Permission denied</code>

Hello!!
I had an idea to make a program that will help you go another step in your favourite CLI.
gsearch will help you search,filter,list and then open your searches in yout default browser, ready for reading!!

usage: 

gsearch [-h] [-q QUERY [QUERY ...]] [-r RESULTS [RESULTS ...]] [-c]
                  [-s SITE [SITE ...]] [-S BIGSITE [BIGSITE ...]]
                  [-t INTEXT [INTEXT ...]] [-u INURL [INURL ...]]
                  [-f FILETYPE [FILETYPE ...]] [-l]

BIG Sites: 1 - stackoverflow.com, 2 - github.com, 3 - stackify.com, 4 -
medium.com, 5 - quora.com, 6 - redis7.com, 7 - exploitdb.com

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY [QUERY ...], --query QUERY [QUERY ...]
                        search query
  -r RESULTS [RESULTS ...], --results RESULTS [RESULTS ...]
                        Open results by order (1 for first search result)
  -c, --copy            copy url to clipboard instead of open it in the web
                        browser
  -s SITE [SITE ...], --site SITE [SITE ...]
                        Search ONLY from those sites.
  -S BIGSITE [BIGSITE ...], --bigsite BIGSITE [BIGSITE ...]
                        Search ONLY from the specifics bigsites.
  -t INTEXT [INTEXT ...], --intext INTEXT [INTEXT ...]
                        Search sites that contains those values
  -u INURL [INURL ...], --inurl INURL [INURL ...]
                        Search sites that their url contains those values
  -f FILETYPE [FILETYPE ...], --filetype FILETYPE [FILETYPE ...]
                        Search files those types
  -l, --list            list n the first 10 search result, cant go with -r.


installation:
<code>./install.sh</code>
or:
<code>
mkdir ~/.gsearch
cp -v by.txt ~/.gsearch/by.txt
cp -v icon.txt ~/.gsearch/icon.txt
sudo ln -s $( pwd )/gsearch.py /usr/bin/gsearch
</code>

examples:

<code>./gsearch.py -q python3 IOError</code>
=> open google result of searching "python3 IOError".

<code>./gsearch.py -l -q python3 IOError</code>
=> list 10 first google result of searching "python3 IOError" and let you choose which result/s to choose.


<code>./gsearch.py -S 1 -q python3 IOError</code>
=> open google result of searching "python3 IOError" but from bufferoverflow.com only (the list is in the help(./gsearch.py -h)).

<code>./gsearch.py -s mysite.com mysite2.com -q python3 IOError</code>
=> open google result of searching "python3 IOError" but from mysite.com and from mysite2.com only.

<code>./gsearch.py -S 2 -q python3 IOError -r 1</code>
=> searching "python3 IOError" from github.com only and then opening the page of the first result.

<code>./gsearch.py -q python3 IOError -l -c</code>
=> searching "python3 IOError", listing the results and coping to clipboard the chosen's url.

<code>./gsearch.py -q python3 IOError -f pdf</code>
=> searching "python3 IOError" but only pdf files.