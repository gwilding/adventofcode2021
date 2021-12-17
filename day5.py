#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:12:31 2021

@author: georg
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def get_input(path_in):
    raw_input = np.genfromtxt(path_in,dtype=str)
    raw_input = [[r[0],r[2] ] for r in raw_input]
    return np.array([[c.split(',') for c in r] for r in raw_input],dtype=int)

def day_05():
    print("******************************************************************")
    print("*                         DAY 5                                  *")
    print("******************************************************************")
    print("Part 1")
    path_in_test = '/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day05'
    path_in = '/home/georg/Dropbox/georg/scripts/aoc2021/input_day05'
    
    vent_coords = get_input(path_in_test)
    vent_map = np.zeros(shape=(vent_coords.max()-vent_coords.min()+1,)*2,dtype=int)
    for vent in vent_coords:
        # check if vertical (x equal)
        if (vent[0][0] == vent[1][0]):
            vent_map[vent[0][0],min(vent[:,1]):max(vent[:,1])+1] += 1
        # check if horizontal (y equal)
        elif (vent[0][1] == vent[1][1]):
            vent_map[min(vent[:,0]):max(vent[:,0])+1,vent[0][1]] += 1
    vent_map = vent_map.T
    print("Test:",np.sum(vent_map >= 2))
    
    
    vent_coords = get_input(path_in)
    vent_map = np.zeros(shape=(vent_coords.max(),)*2,dtype=int)
    for vent in vent_coords:
        # check if vertical (x equal)
        if (vent[0][0] == vent[1][0]):
            vent_map[vent[0][0],min(vent[:,1]):max(vent[:,1])+1] += 1
        # check if horizontal (y equal)
        elif (vent[0][1] == vent[1][1]):
            vent_map[min(vent[:,0]):max(vent[:,0])+1,vent[0][1]] += 1
    vent_map = vent_map.T
    print("Result:",np.sum(vent_map >= 2))
    
    # part 2
    print("Part 2")
    vent_coords = get_input(path_in_test)
    vent_map = np.zeros(shape=(vent_coords.max()-vent_coords.min()+1,)*2,dtype=int)
    for vent in vent_coords:
        # check if vertical (x equal)
        if (vent[0][0] == vent[1][0]):
            vent_map[vent[0][0],min(vent[:,1]):max(vent[:,1])+1] += 1
        # check if horizontal (y equal)
        elif (vent[0][1] == vent[1][1]):
            vent_map[min(vent[:,0]):max(vent[:,0])+1,vent[0][1]] += 1
        # diagonal
        else:
            steps_needed = abs(vent[1,0]-vent[0,0]) + 1
            direction = np.sign(vent[1]-vent[0])
            for k in range(steps_needed):
                vent_map[tuple(vent[0] + direction*k)] += 1
    vent_map = vent_map.T
    print("Test:",np.sum(vent_map >= 2))
    
    
    vent_coords = get_input(path_in)
    vent_map = np.zeros(shape=(vent_coords.max()+1,)*2,dtype=int)
    for vent in vent_coords:
        # check if vertical (x equal)
        if (vent[0][0] == vent[1][0]):
            vent_map[vent[0][0],min(vent[:,1]):max(vent[:,1])+1] += 1
        # check if horizontal (y equal)
        elif (vent[0][1] == vent[1][1]):
            vent_map[min(vent[:,0]):max(vent[:,0])+1,vent[0][1]] += 1
        # diagonal
        else:
            steps_needed = abs(vent[1,0]-vent[0,0]) + 1
            direction = np.sign(vent[1]-vent[0])
            for k in range(steps_needed):
                vent_map[tuple(vent[0] + direction*k)] += 1
    vent_map = vent_map.T
    print("Result:",np.sum(vent_map >= 2))
if __name__ == '__main__':
    main()