#!/usr/bin/env python


"""
Problem Definition :

As any number greater than 9 is represented by several digits, we can calculate the sum of these digits. For example, for numbers 1492 and 1776 we get:

1 + 4 + 9 + 2 = 16
1 + 7 + 7 + 6 = 21
In this task you will be given several numbers and asked to calculate their sums of digits.

Important: while many programming languages have built-in functions to convert numbers to strings (from which digits could be extracted), you should not use this (since your goal is to learn some programming tricks).

Instead you need to implement algorithm with repetitive division by 10 (base of numeral system) and summing up the remainders. Read the Number to digits article for details on the algorithm.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()


def add_digits(num):
    total = 0

    while num > 0:
        num, digit = divmod(num, 10)
        total += digit

    return total

length = int(sys.argv[1])
start = 2

for numbers in xrange(length):

    num1 = int(sys.argv[start])
    num2 = int(sys.argv[start + 1])
    num3 = int(sys.argv[start + 2])

    answer = (num1 * num2) + num3

    print(add_digits(answer)),

    start += 3


print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
