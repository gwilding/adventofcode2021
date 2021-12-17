#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:51:54 2021

@author: georg

Advent of code 2021
Day 11
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def flash_octopuses(data,max_steps=100):
    
    
    neighbours = np.array([[i,j] for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0])
    
    # max_steps = 100
    total_flashes = 0
    for step in range(max_steps):
        # increase by 1
        data += 1
        flashes = np.where(data > 9)
        total_flashes += len(flashes[0])
        # reset when flashes
        data = np.where(data > 9,-np.inf,data)
        while len(flashes[0]):
        # resolve flashes
            for f in np.c_[flashes]:
                for n in neighbours:
                    check_loc = f+n
                    if (np.all(check_loc >= 0)
                        and check_loc[0] < data.shape[0]
                        and check_loc[1] < data.shape[1]):
                        data[tuple(check_loc)] += 1
            flashes = np.where(data > 9)
            total_flashes += len(flashes[0])
            # reset when flashes
            data = np.where(data > 9,-np.inf,data)
        data = np.where(data < 0,0,data)
    return total_flashes


def get_sync(data,max_steps=1000):
    neighbours = np.array([[i,j] for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0])
    
    # max_steps = 100
    total_flashes = 0
    for step in range(max_steps):
        # increase by 1
        data += 1
        flashes = np.where(data > 9)
        total_flashes += len(flashes[0])
        # reset when flashes
        data = np.where(data > 9,-np.inf,data)
        while len(flashes[0]):
        # resolve flashes
            for f in np.c_[flashes]:
                for n in neighbours:
                    check_loc = f+n
                    if (np.all(check_loc >= 0)
                        and check_loc[0] < data.shape[0]
                        and check_loc[1] < data.shape[1]):
                        data[tuple(check_loc)] += 1
            flashes = np.where(data > 9)
            total_flashes += len(flashes[0])
            # reset when flashes
            data = np.where(data > 9,-np.inf,data)
            
        data = np.where(data < 0,0,data)
        if np.all(data == 0):
            # will sync next step
            return step+1
        
    return data

def day_11():
    print("******************************************************************")
    print("*                         DAY 11                                 *")
    print("******************************************************************")
    test_data = np.genfromtxt('./testinput_day11',dtype=str)
    data = np.genfromtxt('./input_day11',dtype=str)
    
    test_data = np.array([[int(d) for d in r] for r in test_data])
    data = np.array([[int(d) for d in r] for r in data])
    
    neighbours = np.array([[i,j] for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0])
    
    print("Part 1:")
    
    max_steps = 100
    total_test_flashes = flash_octopuses(test_data.copy(),max_steps=100)
    print("Test:",total_test_flashes,"OK")

    total_flashes = flash_octopuses(data.copy(),max_steps=100)
    print("Result:",total_flashes,"OK")
    
    print("Part 2:")
    test_synced = get_sync(test_data.copy(),max_steps=10000)
    print("Test:",test_synced,"OK")
    synced = get_sync(data.copy(),max_steps=10000)
    print("Solution:",synced,"OK")

if __name__ == '__main__':
    main()