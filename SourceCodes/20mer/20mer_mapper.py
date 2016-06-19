#!/usr/bin/env python
import sys

# initialize a variable to hold the last 9 characters from the last line
last_line_chars = ''

# iterate over each line
for line in sys.stdin:
  # Ignoring the first line
  if line[0] != '>':
     line = line.strip()
     # Concatenate the last line characters with this line to find 20 mers 
     line = last_line_chars + line
     # iterate over each line to find 20 mers
     for i in range(len(line)):
        # extract 20 character string from the line
        var_20mer = line[i:20+i]
        # printing only strings of length 20
        if len(var_20mer) == 20:
          print var_20mer,1
        # if the inner counter reaches length of the line - 20 then extract last 19 chars
        if i == len(line) - 20 :
            last_line_chars = var_20mer[1:20]
