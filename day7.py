#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:31:06 2021

@author: georg

Advent of code 2021
Day 7
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def day_07():
    print("******************************************************************")
    print("*                         DAY 7                                  *")
    print("******************************************************************")
    print("Part 1")
    
    test_positions = np.array([16,1,2,0,4,2,7,1,2,14])
    positions = np.genfromtxt('./input_day07',delimiter=',',dtype=int)
    
    # # complicated version
    # # testing
    # min_position = -1
    # min_cost = np.inf
    # for try_move_to in range(test_positions.min(),test_positions.max()+1):
    #     new_cost = np.sum(np.abs(test_positions - try_move_to))
    #     if new_cost < min_cost:
    #         min_position = try_move_to
    #         min_cost = new_cost
    # print("Best test position: %i with cost %i"%(min_position,min_cost))
        
    # # solution
    # min_position = -1
    # min_cost = np.inf
    # for try_move_to in range(positions.min(),positions.max()+1):
    #     new_cost = np.sum(np.abs(positions - try_move_to))
    #     if new_cost < min_cost:
    #         min_position = try_move_to
    #         min_cost = new_cost
    # print("Best position: %i with cost %i"%(min_position,min_cost))
    
    # simple version using median
    # testing
    min_test_position = np.median(test_positions)
    min_test_cost = np.sum(np.abs(test_positions - np.median(positions)))
    print("Best test position: %i with cost %i"%(min_test_position,
                                                 min_test_cost))
    
    min_position = np.median(positions)
    min_cost = np.sum(np.abs(positions - np.median(positions)))
    print("Best position: %i with cost %i"%(min_position,
                                            min_cost))
    
    print("Part 2")
    # complicated version
    # testing
    min_position = -1
    min_cost = np.inf
    for try_move_to in range(test_positions.min(),test_positions.max()+1):
        new_cost = np.sum(np.abs(test_positions - try_move_to)*(np.abs(test_positions - try_move_to)+1)/2)
        if new_cost < min_cost:
            min_position = try_move_to
            min_cost = new_cost
    print("Best test position: %i with cost %i"%(min_position,min_cost))
        
    # solution
    min_position = -1
    min_cost = np.inf
    for try_move_to in range(positions.min(),positions.max()+1):
        new_cost = np.sum(np.abs(positions - try_move_to)*(np.abs(positions - try_move_to)+1)/2)
        if new_cost < min_cost:
            min_position = try_move_to
            min_cost = new_cost
    print("Best position: %i with cost %i"%(min_position,min_cost))

if __name__ == '__main__':
    main()