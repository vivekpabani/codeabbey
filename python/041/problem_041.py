#!/usr/bin/env python


"""
Problem Definition :

You will be again given triplets of numbers, but now the middle of them should be chosen - i.e. not the largest and not the smallest one. Such number is called the Median (of the set, array etc).

Be sure, this problem is not simply "another stupid exercise" - it is used as a part in powerful QuickSort algorithm, for example.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected medians of triplets, separated by spaces.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])

total = 0
start = 2
for i in xrange(length):
    left = int(sys.argv[start])
    right = int(sys.argv[start+1])
    mid = int(sys.argv[start+2])

    if right < left:
        right, left = left, right
    if mid < left:
        left, mid = mid, left
    if right < mid:
        right, mid = mid, right


    print(mid),
    start += 3

numbers = sys.argv[1:]
length = int(numbers[0])


print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
