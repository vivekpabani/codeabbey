#!/usr/bin/env python


"""
Problem Definition :

Now your goal is to learn programming loops - i.e. repeated actions. You are to find sum of several numbers (more than two). It will be useful to do this in loop. Perhaps "for" loop will suit nicely since the amount of values for summation is given.

Input data has the following format:

first line contains N - amount of values to sum;
second line contains N values itself.
Answer should contain a single value - the sum of N values.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])

total = 0

for i in xrange(2, length+2):
    total += int(sys.argv[i])

print(total)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
