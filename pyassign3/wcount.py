#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Norman"
__pkuid__  = "1700011727"
__email__  = "1700011727@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    text = ''
    for ch in lines:
        if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
            text = text+ch
        else:
            text = text+' '
    text = text.split()
    dictionary = {}
    for word in text:
        if word not in dictionary:
            dictionary[word] = text.count(word)  
        else:                          
            pass
    table = zip(dictionary.values(),dictionary.keys())
    table = sorted(table)
    table.reverse()
    for i in range(topn):
        (a,b) = table[i]
        print('{}      {}\n'.format(a,b))
    
if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
