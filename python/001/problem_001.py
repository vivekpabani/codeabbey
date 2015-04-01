#!/usr/bin/env python


"""
Problem Definition :

You are to add two numbers and tell their sum. Though you can do it manually, try to write a simple program in any programming language you know or like or want to learn.

input data:
2296878 8555823

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

print(number1+number2)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
