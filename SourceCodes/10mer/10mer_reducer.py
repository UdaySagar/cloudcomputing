#!/usr/bin/env python
import sys
import operator

# maps words to their counts
 
word2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word,count = line.split()
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
    # add the count to earlier one
    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
# Sort the lines in descending order to grab the first 10 top kmers
sorted_x = sorted(word2count.items(), key=operator.itemgetter(1), reverse=True)
#print the top 10 kmers to standard output
for i in range(0,10):
    print sorted_x[i][0], sorted_x[i][1]
