#!/usr/bin/env python


"""
Problem Definition :

You will be given the array for which checksum should be calculated. Perform calculation as follows: for each element of the array (starting from beginning) add this element to result variable and multiply this sum by 113 - this new value taken by modulo 10000007 should become the next value of result, and so on.

Read the article on checksum for detailed description of this algorithm. An example of calculation also could be found there.

Input data will tell the length of an array in the first line.
Array values themselves follow in the second line, separated by spaces.
Answer should have a single value - calculated checksum.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])

total = 0

for i in xrange(2, length+2):
    total = ((total + int(sys.argv[i]))*113) % 10000007

print(total)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
