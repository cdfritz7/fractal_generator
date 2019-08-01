# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:37:29 2018

@author: Connor
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#change polay to a two element array containing xy coordinate
def toxy(length, angle):
    return [length*np.cos(angle*np.pi/180), length*np.sin(angle*np.pi/180)]

#recursively plot trees
def recursiveTrees(ax, center, length, angle, color=100):
    color_arr = ['#13306D', '#403891', '#6b4596', '#90548b',
                 '#b8627d', '#de7065', '#f68f46', '#f9b641', 
                 '#efe350']
    if(length < .5):
        return
    pt1 = center
    pt2 = [toxy(length, angle)[0]+center[0], toxy(length, angle)[1]+center[1]]
    ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], linewidth=length*2, 
            color = color_arr[(int(color))%len(color_arr)])
    recursiveTrees(ax, pt2, length/1.5, angle-45, color+1)
    recursiveTrees(ax, pt2, length/1.5, angle+45, color+1)
    
if(__name__=="__main__"):
    #make figure
    ax = plt.figure().add_subplot(111)
    initial_length=10
    cutoff = 30
    ax.set_xlim((-cutoff, cutoff))
    ax.set_ylim((-cutoff, cutoff))
    ax.set_aspect('equal')
    
    color = 0
    #make trees
    recursiveTrees(ax, [0,0], initial_length, 0, color=color)
    #recursiveTrees(ax, [0,0], initial_length, 45,color='#2D708E')
    recursiveTrees(ax, [0,0], initial_length, 90,color=color)
    #recursiveTrees(ax, [0,0], initial_length, 135, color='#20A387')
    recursiveTrees(ax, [0,0], initial_length, 180,color=color)
    #recursiveTrees(ax, [0,0], initial_length, 225, color='#73D055')
    recursiveTrees(ax, [0,0], initial_length, 270,color=color)
    #recursiveTrees(ax, [0,0], initial_length, 315, color='#FDE725')
    
    #save trees
    ax.set_facecolor('k')
    ax.axis('off')
    plt.savefig("treefractal5.pdf", format="pdf", facecolor='k')
    plt.show()

    