#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:03:27 2021

@author: georg

Advent of code 2021
Day 19
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def load_scans(path_in):
    scannerdata = []
    with open(path_in) as f:
        while True:
            line = f.readline()
            if not line:
                break
            if 'scanner' in line:
                scannerdata.append([])
            else:
                if not line == '\n':
                    line = [int(l) for l in line.rstrip().split(',')]
                    scannerdata[-1].append(line)
    return scannerdata
        
def get_distance_matrix(scan):
    # if len(scan.shape) == 3:
    #     return np.array([get_distance_matrix(s) for s in scan])
    dmat = np.zeros((len(scan),)*2)
    for k,beacon in enumerate(np.array(scan)):
        dmat[k,:] = np.sum((beacon-np.array(scan))**2,axis=1)
    return dmat

def eval_multiple_scans(scans):
    dmats = []
    for scan in scans:
        dmats.append(get_distance_matrix(scan))
    return dmats

def compare_distance_matrices(dmats):
    all_inter = set([])
    for k,dmat0 in enumerate(dmats):
        for dmat1 in dmats[(k+1):]:
            all_inter = all_inter.union(set(dmat0.flat).intersection(set(dmat1.flat)))
    
    for dmat0 in dmats:
        for dmat_row in dmat0:
            pass
    # set(dmats[0][0]).intersection(set(dmats[1][9]))
    
    all_sorted_distances = []
    for d1 in dmats:
        for d2 in d1:
            
            all_sorted_distances.extend(sorted(d2))
    all_unique = []
    for k,sorted_distance in enumerate(all_sorted_distances):
        if sorted_distance in all_sorted_distances[k+1:]:
            all_unique.append(sorted_distance)

def day_19():
    print("******************************************************************")
    print("*                         DAY 19                                 *")
    print("******************************************************************")
    
    test_data_2d = '/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day19_2d'
    test_data_3d_1scanner = '/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day19_3d_1scanner'
    test_data_3d = '/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day19_3d'
    
    
    
    scan_1_2d = load_scans(test_data_2d)
    eval_multiple_scans(scan_1_2d)
    
    scan_3d_1 = load_scans(test_data_3d_1scanner)
    dmat_3d_1 = eval_multiple_scans(scan_3d_1)
    
    scan_3d_2 = load_scans(test_data_3d)
    dmat_3d_2 = eval_multiple_scans(scan_3d_2)
    
    print("Part 1:")
    
    
    print("solution:","OK")
    
    print("Part 2:")
    print("test c:","OK")
    print("solution:","OK")

if __name__ == '__main__':
    main()