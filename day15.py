#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:36:20 2021

@author: georg

Advent of code 2021
Day 15
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    # pass
    data_path = './input_day15'
    
    data = np.genfromtxt(data_path,dtype=str)
    
    data = np.array([[int(d) for d in r] for r in data])
    
    print("Solution:",Astar(data,(0,0),(-1,-1)),"OK")
    
def get_path_value(matrix,path):
    return sum([matrix[p] for p in path])


def get_lowest_path_value(value_map):
    """
    Only move right or down.
    """
    lowest_path = np.zeros(value_map.shape,dtype=int)
    lowest_path[0,:] = np.cumsum(value_map[0,:]) - value_map[0,0]
    lowest_path[:,0] = np.cumsum(value_map[:,0]) - value_map[0,0]
    for k_col in range(1,value_map.shape[0]):
        for k_row in range(1,value_map.shape[1]):
            lowest_path[k_col,k_row] = value_map[k_col,k_row] +\
                                        min(lowest_path[k_col-1,k_row],
                                            lowest_path[k_col,k_row-1])
    return lowest_path[-1,-1]

def get_neighbours(pos,n):
    # 4 corners
    if pos[0] == 0 and pos[1] == 0:
        steps = [[0,1],[1,0]]
    elif pos[0] == 0 and pos[1] == n-1:
        steps = [[0,-1],[1,0]]
    elif pos[0] == n-1 and pos[1] == 0:
        steps = [[0,1],[-1,0]]
    elif pos[0] == n-1 and pos[1] == n-1:
        steps = [[0,-1],[-1,0]]
    # 4 edges
    elif pos[0] == 0:
        steps = [[0,1],[1,0],[0,-1]]
    elif pos[1] == 0:
        steps = [[0,1],[1,0],[-1,0]]
    elif pos[0] == n-1:
        steps = [[0,1],[0,-1],[-1,0]]
    elif pos[1] == n-1:
        steps = [[0,-1],[-1,0],[1,0]]
    else:
        steps = [[-1,0],[0,-1],[0,1],[1,0]]
    return [ (pos[0]+s[0],pos[1]+s[1]) for s in steps]

def Astar(value_map,start,end):
    n = len(value_map)
    
    lowest_value_map =  np.ones(value_map.shape,dtype=int)*np.sum(value_map)*10
    visited = np.zeros(value_map.shape,dtype=bool)
    
    start = (0,0)
    end = (-1,-1)
    end = tuple(np.array(end)%value_map.shape)

    lowest_value_map[start] = 0
    
    while not np.all(visited):
        current_min_value = np.min(lowest_value_map[~visited])
        a,b = np.where(lowest_value_map == current_min_value)
        new_pos = [(k,i) for k,i in zip(a,b)]
        for pos in new_pos:
            if not visited[pos]:
                for neighbour in get_neighbours(pos,n):
                    if not visited[neighbour]:
                        # go through all neighbours and update the 
                        if lowest_value_map[pos]+value_map[neighbour] < lowest_value_map[neighbour]:
                            lowest_value_map[neighbour] = lowest_value_map[pos]+value_map[neighbour]
                visited[pos] = True
    return lowest_value_map[-1,-1]


def update_map(value_map,n):
    value_map = np.concatenate([(value_map+k-1)%9+1 for k in range(n)],axis=1)
    value_map = np.concatenate([(value_map+k-1)%9+1 for k in range(n)],axis=0)
    return value_map
    
    

def day_15():
    print("******************************************************************")
    print("*                         DAY 15                                 *")
    print("******************************************************************")
    
    test_data_path = './testinput_day15'
    data_path = './input_day15'
    
    test_data = np.genfromtxt(test_data_path,dtype=str)
    data = np.genfromtxt(data_path,dtype=str)
    
    test_data = np.array([[int(d) for d in r] for r in test_data])
    data = np.array([[int(d) for d in r] for r in data])
    
    print("Part 1:")
    print("Test:",get_lowest_path_value(test_data),"OK (40)")
    print("Test:",Astar(test_data,(0,0),(-1,-1)),"OK (40)")
    
    print("Solution:",Astar(data,(0,0),(-1,-1)),"OK (523)")
    
    
    print("Part 2:")
    test_data2 = update_map(test_data,5)
    data2 = update_map(data,5)
    print("Test:",Astar(test_data2,(0,0),(-1,-1)),"OK (315)")
    
    print("Solution:",Astar(data2,(0,0),(-1,-1)),"OK")

if __name__ == '__main__':
    main()