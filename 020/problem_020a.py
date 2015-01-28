#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time

startTime = time.clock()


def count(s):
    return str(len(filter(lambda x : x in 'aeiouy', s)))

filename = 'input.txt'
data = open(filename, 'rt').readlines()
print ' '.join(count(data) for _ in xrange(int(data[0])))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
