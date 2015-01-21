#!/usr/bin/env python


"""
Problem Definition :

Input data will have:

initial integer number in the first line;
one or more lines describing operations, in form sign value where sign is either + or * and value is an integer;
last line in the same form, but with sign % instead and number by which the result should be divided to get the remainder.
Answer should give remainder of the result of all operations applied sequentially (starting with initial number) divided by the last number.

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a/b


def mod(a, b):
    return a % b


fun_dict = {
    '+': add,
    '-': subtract,
    '*': mul,
    '/': divide,
    '%': mod

}
answer = int(sys.argv[1])
start = 2
symbol = ''

while symbol != '%':
    symbol = sys.argv[start]
    answer = fun_dict[symbol](answer, int(sys.argv[start + 1]))
    start += 2

print(answer)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
