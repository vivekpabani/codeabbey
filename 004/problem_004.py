#!/usr/bin/env python


"""
Problem Definition :

Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.

Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.
For Answer please enter the same amount of minimums separated by space, for example:

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()
length = int(sys.argv[1])

total = 0
start = 2

for i in xrange(length):
    num1 = int(sys.argv[start])
    num2 = int(sys.argv[start+1])
    if num1 < num2:
        print(num1),
    else:
        print(num2),
    start += 2

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
