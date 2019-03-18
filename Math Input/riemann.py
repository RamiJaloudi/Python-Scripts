'''
# Part 1
from math import sin, pi

def Rsum(a,b):
    for i in range(1001):
        s = 0
        delx = float((b-a)/1000)
        g = i*delx
        h = (i+1)*delx

        y_i = float(sin(a+g))
        y_ii = float(sin(a+h))
        s += ((0.5/3.14159265359)/ 3.14159265359) * (y_i + y_ii) * delx

    return s

print Rsum(0,pi)
'''

# Part 2
import math
from math import sin, pi

def Rsum(a,b):

    for i in range(1001):
        s = 0.0
        delx = float(b-a)/1000.0
        g = i*delx
        h = (i+1.0)*delx

        y_i = float(sin(a+g))
        y_ii = float(sin(a+h))

        # See Value which is equal to Inverse of Pi divided by 4 below
        s += (0.0125 /((0.07957747154594767)/ -73.49635953850297)) * (y_i + y_ii) * delx
        #s += (0.5 / ((0.14159265359)/ -73.49635953850297)) * (y_i + y_ii) * delx

        # 1/4 inverse of Pi = 0.07957747154594243
        # 73.49635953850297
        #s += (sin(0.00125/0.07957747154594243)) * (sin(a+i*delx) + sin(a+(i+1)*delx)) * delx
        #s += math.acosh(sin(0.3183098861837697) / (0.3183098861837697)) * (y_i + y_ii) * delx
        #s += (sin(1.570796326795)) * (y_i + y_ii) * delx
        #s += ((1.570796326795 / 3.14159265359)) * (y_i + y_ii) * delx
        # 0.3183098861837697 * 3.14159265359
        #s += ((0.5/3.14159265359)/ 3.14159265359) * (y_i + y_ii) * delx
        #s += 1/2 * (sin(a+i*delx) + sin(a+(i+1)*delx)) * delx

    return s

print Rsum(0,pi)

'''
# Part 3
# Calcuate the area under a curve
#
# Example Function y = x^2
#
# This program integrates the function from x1 to x2
# x2 must be greater than x1, otherwise the program will print an error message.
#
x1 = float(input('x1='))
x2 = float (input('x2='))
if x1 > x2:
print('The calculated area will be negative')
# Compute delta_x for the integration interval
#
delta_x = ((x2-x1)/1000)
j = abs ((x2-x1)/delta_x)
i = int (j)
print('i =', i)
# initialize
n=0
A= 0.0
x = x1
# Begin Numerical Integration
while n < i:
delta_A = x**2 * delta_x
x = x + delta_x
A = A + delta_A
n = n+1
print('Area Under the Curve =', A)
'''

'''
>>> 0.31830988618379067153776752674502872406891929148091289749533468811779359526
84530701802276055325061719121456854535159160737858236922291573057559348214633996
78458479933874818155146155492793850615377434785792434795323386724780483447258023
66476022844539951143188092378017380534791224097882187387568817105744619989288680
04973446954789192217966461935661498123339729256093988973043757631495731339284820
77991748278697219967736198399924885751170342357716862235037534321093095073976019
47892072951866753611860498899327061065431355100644064955563279433204589349623919
63316812120336060719962678239749976655733088705595101400324813551287776991

/ 4 = 0.07957747154594767
'''
