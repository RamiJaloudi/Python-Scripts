'''
from random import *
def passwordGen(length,badChars = '',alpha = '1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM~`?'):
    alphaNew = list(set(alpha)^set(badChars))
    return "".join([alphaNew[randint(0,len(list(alphaNew)-1)] for i in range(length)])
'''

from random import *
passwordGen = lambda length, badChars = '',alpha = '1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM~`?': "".join([list(set(alpha)^set(badChars))[randint(0,len(list(set(alpha)^set(badChars)))-1)] for i in range(length)])
