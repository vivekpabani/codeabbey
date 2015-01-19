#!/usr/bin/env python


"""
Problem Definition :

Now you will be given several pairs of values and you need to calculate sum for each pair.

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])

total = 0
start = 2
for i in xrange(length):
    total = int(sys.argv[start]) + int(sys.argv[start+1])
    start += 2
    print(total),

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
