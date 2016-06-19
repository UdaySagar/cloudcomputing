#!/usr/bin/env python
import sys

# initialize a variable to hold the last 9 characters from the last line
last_line_chars = ''

# iterate over each line
for line in sys.stdin:
  # Ignoring the first line
  if line[0] != '>':
     line = line.strip()
     # Concatenate the last line characters with this line to find 10 mers 
     line = last_line_chars + line
     # iterate over each line to find 10 mers
     for i in range(len(line)):
        # extract 10 character string from the line
        var_10mer = line[i:10+i]
        # printing only strings of length 10
        if len(var_10mer) == 10:
          print var_10mer,1
        # if the inner counter reaches length of the line - 10 then extract last 9 chars
        if i == len(line) - 10 :
            last_line_chars = var_10mer[1:10]
