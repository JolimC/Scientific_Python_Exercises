# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import numpy as np
from sympy import dsolve, Eq, symbols, Function, sin
#from sympy import *

def solveA():
    x = symbols('x')
    y = symbols('y', cls=Function)
    deqn1 = Eq(y(x).diff(x), x / (2*y(x)))
    sol1 = dsolve(deqn1, y(x), ics={y(1): 1})
    print(sol1)


def solveB():
    x = symbols('x')
    y = symbols('y', cls=Function)
    deqn1 = Eq(y(x).diff(x), -y(x)/x)
    sol1 = dsolve(deqn1, y(x), ics={y(2): 3})
    print(sol1)
    
    
def solveC():
    x = symbols('x')
    y = symbols('y', cls=Function)
    deqn1 = Eq(y(x).diff(x), x**2 / y(x)**3)
    sol1 = dsolve(deqn1, y(x), ics={y(0): 1})
    print(sol1)
    
def solveD():
    x = symbols('x', cls=Function)
    t = symbols('t')
    deqn1 = Eq(x(t).diff(t, 2) + 5*x(t).diff(t) + 6*x(t), 0)
    sol1 = dsolve(deqn1, x(t), ics={x(0): 1})
    sol2 = dsolve(deqn1, x(t), ics={x(0): 0})
    print('If x(0) = 1: {}'.format(sol1))
    print('If x(0) = 0: {}'.format(sol2))
    
def solveE():
    x = symbols('x', cls=Function)
    t = symbols('t')
    deqn1 = Eq(x(t).diff(t, 2) + 5*x(t).diff(t) + 6*x(t), sin(t))
    sol1 = dsolve(deqn1, x(t), ics={x(0): 1})
    sol2 = dsolve(deqn1, x(t), ics={x(0): 0})
    print('If x(0) = 1: {}'.format(sol1))
    print('If x(0) = 0: {}'.format(sol2))
    