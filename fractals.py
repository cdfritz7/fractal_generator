# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:37:57 2018

@author: Connor
"""

import matplotlib.pyplot as plt
import math
import random
import numpy as np

#function for drawing circles on a matplotlib axis recursively
def recursiveCircles(center, length, ax, col = 'c'):
    if(length < .05):
        return
    circ = plt.Circle(center, length, linewidth=length/4 ,fill=False, color=col)
    ax.add_patch(circ)
    xy = toxy(length)
    recursiveCircles(center+[xy, xy], length/1.5, ax, col=col)
    recursiveCircles(center-[xy, xy], length/1.5, ax, col=col)


def toxy(length):
    return length*np.sin(45)

if(__name__=="__main__"):
    SAVE_DIR = None

    #set up axis and variables
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor('k')
    bound = 27
    ax.set_xlim((-bound, bound))
    ax.set_ylim((-bound, bound))
    ax.set_aspect('equal')
    center = np.array([0,0])
    length=10

    #make circles
    recursiveCircles(center-1, length, ax, col='r')
    recursiveCircles(center, length, ax)

    #save figure
    ax.axis('off')
    ax.set_facecolor('k')

    if not SAVE_DIR is None:
        plt.savefig(SAVE_DIR, format="jpg", dpi=1000, facecolor='k')

    plt.show()
