# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

'''
Carries out "iterations" iterations starting at "base", showing the 
last "list_size" elements of all the iterations.

The recurrence relation used is x_n+1 = 4_n * (1-x_n)
'''

def showIterations(base, iterations, list_size):
    curr = base
    list_to_return = []
    for i in range(0, iterations):
        if (i >= iterations - list_size):
            list_to_return.append(curr)
        curr = 4*curr*(1-curr)
    return list_to_return