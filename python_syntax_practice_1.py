# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

#converts degrees F to C
def FtoC(df):
    return (df - 32) * 5/9

#determines if an integer is prime
def isPrime(num):
    if (num < 2):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            return False
    return True

#returns the total sum of all the primes up to num, 
#including num
def numPrimes(num):
    sum = 0;
    for i in range(2, num + 1):
        if (isPrime(i)):
            sum += i
    return sum        
    

'''
lists the pythagorean triples such that a, b <= m 
and c = b + n

Essentially, we are finding values for a,b that satisfy
a**2 + b**2 = (b+n)**2, which reduces to 
a**2 = 2*b*n + n**2
'''
def listTriples(m, n):
    triple_list = []
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            if (a**2 == 2*b*n + n**2):
                triple_list.append([a, b, b + n])
    return triple_list            