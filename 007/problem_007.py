#!/usr/bin/env python


"""
Problem Definition :

There are two widespread systems of measuring temperature - Celsius and Fahrenheit. First is quite popular in Europe and second is well in use in United States for example.

By Celsius scale water freezes at 0 degrees and boils at 100 degrees. By Fahrenheit water freezes at 32 degrees and boils at 212 degrees. You may learn more from wikipedia on Fahrenheit. Use these two points for conversion of other temperatures.

You are to write program to convert degrees of Fahrenheit to Celsius.

Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
Answer should contain exactly N results, rounded to nearest integer and separated by spaces.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

length = int(sys.argv[1])

start = 2
for i in xrange(length):
    fh = int(sys.argv[start])
    sc = int(round((fh - 32)*5.0/9))
    print(sc),

    start += 1

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
