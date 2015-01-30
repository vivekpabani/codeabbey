#!/usr/bin/env python


"""
Problem Definition :

The simple measure of body constitution was proposed at the middle of XIX century. It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:

BMI = weight / height^2
Where weight is taken in kilograms and height in meters.

Four general grades are proposed:

Underweight     -           BMI < 18.5
Normal weight   -   18.5 <= BMI < 25.0
Overweight      -   25.0 <= BMI < 30.0
Obesity         -   30.0 <= BMI
For example, if I have weight of 80 kg and height of 1.73 m I can calculate:

BMI = 80 / (1.73)^2 = 26.7
i.e. somewhat overweight.

We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.

Input data contain number of people in the first line.
Other lines will contain two values each - weight in kilograms and height in metres.
Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces. For example:

"""

__author__ = 'vivek'

import time
import sys

startTime = time.clock()
length = int(sys.argv[1])

total = 0
start = 2

for i in xrange(length):
    num1 = float(sys.argv[start])
    num2 = float(sys.argv[start+1])
    bmi = num1*1.0/(num2**2)

    if bmi < 18.5:
        print('under'),
    elif bmi < 25.0:
        print('normal'),
    elif bmi < 30.0:
        print('over'),
    else:
        print('obese'),
    start += 2

print "\nRun time...{} secs \n".format(round(time.clock() - startTime, 4))
