#!/usr/bin/env python


"""
Problem Definition :

This is a simple problem to get introduced to string processing. You will be given several lines of text - and for each of them you should tell the number of vowels (i.e. letters a, o, u, i, e, y). Note: that y is regarded as vowel for purpose of this task.

Though simple, this technique is important in cipher-breaking approaches. For example refer to Caesar Cipher Cracker problem.

Input data contain number of test-cases in the first line.
Then the specified number of lines follows each representing one test-case.
Lines consist only of lowercase English (Latin) letters and spaces.
Answer should contain the number of vowels in each line, separated by spaces.

"""

__author__ = 'vivek'

import time

startTime = time.clock()

#vowels = ['a','e','i','o','u','y']
vowels = 'aeiouy'

filename = 'input.txt'
data = open(filename, 'rt').readlines()
length = int(data[0])
start = 1

for i in xrange(1, length+1):
    total = 0

    for character in data[i]:
        if character in vowels:
            total += 1

    print(total),

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
