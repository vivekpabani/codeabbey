#!/usr/bin/env python


"""
Problem Definition :

Average (or mean) value of some numbers could be calculated as their sum divided by their amount. For example:

avg(2, 3, 7) = (2 + 3 + 7) / 3 = 4
avg(20, 10) = (20 + 10) / 2 = 15
You will be given several arrays, for each of which you are to find an average value.

Input data will give the number of test-cases in the first line.
Then test-cases themselves will follow, one case per line.
Each test-case describes an array of positive integers with value of 0 marking end. (this zero should not be included into calculations!!!).
Answer should contain average values for each array, rounded to nearest integer (see task on rounding), separated by spaces.

"""

__author__ = 'vivek'

import time

startTime = time.clock()

filename = 'input.txt'

data = []

for line in open(filename, 'rt').readlines():
    data.append(line.split())

del(data[0])

for line in data:
    total = 0

    for item in line:
        total += int(item)

    print int(round(total*1.0/(len(line)-1))),

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
