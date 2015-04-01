#!/usr/bin/env python


"""
Problem Definition :

This problem introduces popular algorithm of the "linear search", which should be learnt thoroughly as it is often used in programming more complex tasks (sorting etc.)

Very common operation on sequence of values, or arrays is to find its extremal value - maximum or minimum. To achieve this one need to store current maximum (or minimum respectively) in a separate variable, and then run through array, comparing each of its elements to this variable. Whenever next value is greater than this temporary variable, this value should be copied into it (as a new maximum).

At the end of the pass this temporary variable will hold the extremum value.

Input data will give you exactly 300 numbers in a single line.
Answer should contain maximum and minimum of these values, separated by space.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

numbers = sys.argv[1:]
length = len(numbers)

print(numbers)
maximum = int(numbers[0])
minimum = int(numbers[0])

for i in xrange(0, length):
    number = int(numbers[i])

    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

print maximum, minimum
print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
