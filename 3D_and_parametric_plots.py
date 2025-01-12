# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#plots y = 3*x**3 + 2*x**2 - 5
def plotA():
    x = np.linspace(-10,10,1000)
    plt.figure(1)
    plt.subplot(1,1,1)
    y = 3*x**3 + 2*x**2 - 5
    plt.plot(x, y)
    plt.show()


    
def plotB():
    x = np.linspace(-5,5,100)
    y = np.exp(-x**2)
    plt.figure(1)
    plt.subplot(1,1,1)
    plt.plot(x, y)
    plt.show()
    
def plotC():
    x, y = np.mgrid[-100:100:10000j, -100:100:10000j]
    z = x**2 - 2*x*y - y**2
    plt.contour(x, y, z, levels=[1])
    plt.show()
    
    
#helper 1 for plot D    
def plotDh1(x, y):
    return 4*x**2*np.exp(y) - 2*x**4 - np.exp(4*y)
    

def plotD():  
    X = np.linspace(-3, 3, 100)
    Y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(X, Y)
    Z = plotDh1(X, Y).T
    
    fig = plt.figure(1)
    ax = fig.add_subplot(1,1,1, projection='3d')
    p = ax.plot_wireframe(X,Y,Z, rstride=4, cstride=4)
    ax.plot_surface(X, Y, Z, rstride = 4, cstride = 4, alpha=0.25)
    cset=ax.contour(X,Y,Z,zdir='z',offset=-150, cmap=plt.cm.coolwarm)
    
    ax.set_zlim3d(-150, 0)
    
    plt.show()
    

def plotE():
    t = np.linspace(-4, 4, 100)
    x = t**2 - 3*t 
    y = t**3 - 9*t
    z = t
    
    fig = plt.figure(1)
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.plot(x, y, z)
    plt.show()
    
