#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:09:54 2021

@author: georg

Advent of code 2021
Day 9
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def find_minimum(data):
    minimum = np.c_[data[:,:-1] < data[:,1:], np.ones(data.shape[0],dtype=bool)]
    # lower than left:
    minimum = minimum & np.c_[np.ones(data.shape[0],dtype=bool),data[:,1:] < data[:,:-1]]
    # lower than above:
    minimum = minimum & np.vstack((np.ones(data.shape[1],dtype=bool),data[1:,:] < data[:-1,:]))
    # lower than above:
    minimum = minimum & np.vstack((data[:-1,:] < data[1:,:],np.ones(data.shape[1],dtype=bool)))
    return minimum
    
def find_basin(data):
    basins = []
    minimum = find_minimum(data)
    
    minima_loc = np.c_[np.where(minimum)]
    
    steps = np.array([[0,1],
                      [0,-1],
                      [1,0],
                      [-1,0]])
    
    for m0 in minima_loc:
        basin = []
        add_loc_to_basin = [m0]
        basin_size = 1
        while len(add_loc_to_basin):
            basin = basin + add_loc_to_basin
            add_loc_to_basin = []
            for m in basin:
                # step through neighbours
                for s in steps:
                    check_loc = m+s
                    # lower bound
                    check_loc = np.where(check_loc<0,0,check_loc)
                    # upper bound
                    check_loc[0] = min(check_loc[0],data.shape[0]-1)
                    check_loc[1] = min(check_loc[1],data.shape[1]-1)
                    
                    # or another if here to skip!
                    # if (np.all(check_loc > 0)
                    #     and not check_loc[0] >= data.shape[0]
                    #     and not check_loc[1] >= data.shape[1]):
                    
                    if (data[tuple(check_loc)] < 9
                        and not np.all(check_loc == basin,axis=1).any()):
                        if (not len(add_loc_to_basin) or not np.all(check_loc == add_loc_to_basin,axis=1).any()):
                            add_loc_to_basin.append(check_loc)
        basins.append(np.array(basin))
    return basins

def day_09():
    print("******************************************************************")
    print("*                         DAY 9                                  *")
    print("******************************************************************")
    print("Part 1")
    
    test_data = np.genfromtxt('./testinput_day09',dtype=str)
    data = np.genfromtxt('./input_day09',dtype=str)
    
    test_data = np.array([[int(d) for d in r] for r in test_data])
    data = np.array([[int(d) for d in r] for r in data])

    test_minimum = find_minimum(test_data)
    print("Test:",np.sum(test_minimum*(1+test_data)),"OK")
    
    minimum = find_minimum(data)
    print("Test:",np.sum(minimum*(1+data)),"OK")


    print("Part 2")
    test_basins = find_basin(test_data)
    print("Test:",
          np.prod(sorted([len(b) for b in test_basins],reverse=True)[:3]),
          "OK")
    basins = find_basin(data)
    print("Test:",
          np.prod(sorted([len(b) for b in basins],reverse=True)[:3]),
          "OK")
     
if __name__ == '__main__':
    main()