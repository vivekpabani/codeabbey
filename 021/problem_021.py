#!/usr/bin/env python


"""
Problem Definition :

Here is an array of length M with numbers in the range 1 ... N, where N is less than or equal to 20. You are to go through it and count how many times each number is encountered.
I.e. it is like Vowel Count task, but you have to maintain more than one counter. Be sure to use separate array for them, do not create a lot of separate variables, one for each counter.

Input data contain M and N in the first line.
The second (rather long) line will contain M numbers separated by spaces.
Answer should contain exactly N values, separated by spaces. First should give amount of 1-s, second - amount of 2-s and so on.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])
limit = int(sys.argv[2])

count = [0 for i in xrange(limit)]

for i in xrange(3, length+3):
    count[int(sys.argv[i]) - 1] += 1

for item in count:
    print(item),

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
