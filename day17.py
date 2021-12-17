#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:13:54 2021

@author: georg

Advent of code 2021
Day 17
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def main():
    pass

def get_max_y(target):
    # assumes pos:
    # pos = np.array([0,0])
    
    # find the one value for x (simple)
    test_sum_until = int(np.ceil((-1+(1+8*target[0][1])**0.5)/2))
    
    x_pos = np.cumsum(np.mgrid[:test_sum_until])
    possible_vx = np.mgrid[:test_sum_until][(x_pos <= target[0][1]) & (x_pos >= target[0][0])]
    possible_vx = possible_vx[0]
    
    # initial upwards speed will be downwards speed at exactly y=0 (above the target)
    # and the next step will be -(downward+1) until maybe in the field
    # next step from 0 should be at the bottom of targer
    max_vy = -1*target[1][0]-1
    max_y = max_vy*(max_vy+1)//2
    
    # max y is
    return (possible_vx,max_vy), max_y

def get_all_vel(target):
    # lists of target cells
    x_target = list(range(target[0][0],target[0][1]+1))
    y_target = list(range(target[1][0],target[1][1]+1))
    
    # functions to solve for velocities tha twill hit target zone
    getvx = lambda n, Lx: np.round(((np.array(Lx) + n*(n-1)//2)/n)[((np.array(Lx) + n*(n-1)//2)/n)%1 == 0]).astype(int)
    getvy = lambda n, Ly: np.round(((np.array(Ly) + n*(n-1)//2)/n)[((np.array(Ly) + n*(n-1)//2)/n)%1 == 0]).astype(int)
    
    # all non stopped paths
    all_vel = []
    max_steps = int((-1+(1+8*target[0][1])**0.5)/2)
    for n in range(1,max_steps):
        vx = getvx(n,x_target)
        vy = getvy(n,y_target)
        for vxk in vx:
           for vyk in vy:
               if not (vxk,vyk) in all_vel:
                   all_vel.append((vxk,vyk))
    # stopped paths
    max_vy = -1*target[1][0]-1
    test_sum_until = int(np.ceil((-1+(1+8*target[0][1])**0.5)/2))
    x_pos = np.cumsum(np.mgrid[:test_sum_until])
    possible_vx = np.mgrid[:test_sum_until][(x_pos <= target[0][1]) & (x_pos >= target[0][0])]
    
    for pos_vx in possible_vx:
        for vy in range(0,max_vy+1):
            if check_hit((pos_vx,vy),target):
                if not (pos_vx,vy) in all_vel:
                   all_vel.append((pos_vx,vy))
    return all_vel

def check_hit(dv,target,return_path=False):
    pos = np.array((0,0))
    dv = np.array(dv)
    if return_path: pos_list = [tuple(pos)]
    # while not overshot
    while pos[0] <= max(target[0]) and pos[1] >= min(target[1]):
        pos += dv
        if return_path: pos_list.append(tuple(pos))
        if check_path([pos],target):
            if return_path: return True, pos_list
            return True
        dv[0] = max(dv[0]-1,0)
        dv[1] -= 1
    if return_path: return False, pos_list
    return False

def check_path(pos_array,target):
    for p in pos_array:
        if ((p[0] <= max(target[0])) and (p[0] >= min(target[0])) and
            (p[1] <= max(target[1])) and (p[1] >= min(target[1]))):
            return True
    return False

def launch_plot(dv,target,fig_ax = None):
    pos = np.array([0,0])
    dv = np.array(dv)
    
    hit, pos_array = check_hit(dv,target,True)
    
    if isinstance(fig_ax, type(None)): fig, ax = plt.subplots(1,1)
    ax.scatter(*pos.T,c='r')
    ax.plot(*np.array(pos_array).T)
    ax.add_patch(Rectangle(target[:,0], *np.diff(target,axis=1),
                            facecolor='r', edgecolor='k', alpha=0.3) )
    return fig, ax

def day_17():
    print("******************************************************************")
    print("*                         DAY 17                                 *")
    print("******************************************************************")
    
    test_target_area_string = 'target area: x=20..30, y=-10..-5'
    target_area_string = 'target area: x=235..259, y=-118..-62'
    
    test_target_area_string = test_target_area_string[13:]
    target_area_string = target_area_string[13:]
    
    test_target_area_string = test_target_area_string.split(', ')
    target_area_string = target_area_string.split(', ')

    test_target_area = np.array([[int(d) for d in direction[2:].split('..')] for direction in test_target_area_string])
    target_area = np.array([[int(d) for d in direction[2:].split('..')] for direction in target_area_string])
    
    print("Part 1:")
    print("test:",get_max_y(test_target_area),"OK")
    print("Solution:",get_max_y(target_area),"OK")

    
    print("Part 2:")
    print("test:",len(get_all_vel(test_target_area)),"OK")
    print("Solution:",len(get_all_vel(target_area)),"OK")

if __name__ == '__main__':
    main()