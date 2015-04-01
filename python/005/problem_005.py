#!/usr/bin/env python


"""
Problem Definition :

To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.

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
    num3 = int(sys.argv[start+2])

    if num1 < num2:
        if num1 < num3:
            print(num1),
        else:
            print(num3),
    elif num2 < num3:
        print(num2),
    else:
        print(num3),
    start += 3

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
