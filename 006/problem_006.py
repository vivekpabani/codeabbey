#!/usr/bin/env python


"""
Problem Definition :

When program deals with numbers which have fraction part we sometimes want to round such values to whole integer. We'll need this for programming some later problems (to make answers more uniform, for example), so let us have the following dedicated exercise to learn this trick.

There are several pairs of numbers. For each pair you are to divide first by second and return the result, rounded to nearest integer.

In cases, when result contains exactly 0.5 as a fraction part, value should be rounded up (i.e. to next integer greater than given one). Note that for negative values "greater" means "closer to zero". Refer to the Wikipedia page on Rounding for more thorough explanations.

In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed (unless other is explicitly specified).
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
    answer = int(round(num1*1.0/num2))
    print(answer),

    start += 2

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
