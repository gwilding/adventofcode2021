#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:06:18 2021

@author: georg
Advent of code 2021
Day 8


  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

class jumbled_display:
    def __init__(self,unique_pattern):
        # find 4 unique segments (1,4,7,8) and start to fill conversion map
        pattern_len = [len(u) for u in unique_pattern]
        true_len = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
        # digit 1 has only 2 segments
        # digit 4 has only 2 segments
        # digit 7 has only 2 segments
        # digit 8 has all 7  segments
        unique_map = {1: pattern_len.index(2),
                      4: pattern_len.index(4),
                      7: pattern_len.index(3),
                      8: pattern_len.index(7)}
        unique_segments_found = {1: set(unique_pattern[pattern_len.index(2)]),
                                 4: set(unique_pattern[pattern_len.index(4)]),
                                 7: set(unique_pattern[pattern_len.index(3)]),
                                 8: set(unique_pattern[pattern_len.index(7)])}
        
        # top segment: a = ???
        # segment from digit 7 that doesn't appear in 1
        conversion = {'a': (unique_segments_found[7]-unique_segments_found[1]).pop()}
        
        # go through 6 digit numbers
        # between union of 4 + 7 only appears in 9 and 8
        # -> only in one 6 segment number
        # only 1 6 segment number contains all of 1 -> 0
        index = -1
        union_47 = unique_segments_found[4].union(unique_segments_found[7])
        for k in range(3):
            index = pattern_len.index(6,index+1)
            if union_47.issubset(unique_pattern[index]):
                unique_segments_found[9] = set(unique_pattern[index])
                unique_map[9] = index
            elif unique_segments_found[1].issubset(unique_pattern[index]):
                unique_segments_found[0] = set(unique_pattern[index])
                unique_map[0] = index
            else:
                unique_segments_found[6] = set(unique_pattern[index])
                unique_map[6] = index
            
        # bottom left segment: e = ???
        # 8 - 9
        conversion['e'] = (unique_segments_found[8] - unique_segments_found[9]).pop()
        # top right segment: c = ???
        # 8 - 6
        conversion['c'] = (unique_segments_found[8] - unique_segments_found[6]).pop()
        # bottom right segment: f = ???
        # 1 - c / top right segment
        conversion['f'] = unique_segments_found[1].difference(conversion['c']).pop()
        # centre segment: d = ???
        # 8 - 0
        conversion['d'] = (unique_segments_found[8] - unique_segments_found[0]).pop()
        
        # go through 5 digit numbers: 2, 3, 5
        # 7 is only contained in 3
        # e/bottom left is only contained in 2
        index = -1
        for k in range(3):
            index = pattern_len.index(5,index+1)
            # 3
            if unique_segments_found[7].issubset(unique_pattern[index]):
                unique_segments_found[3] = set(unique_pattern[index])
                unique_map[3] = index
            # 2
            elif conversion['e'] in unique_pattern[index]:
                unique_segments_found[2] = set(unique_pattern[index])
                unique_map[2] = index
            # 5
            else:
                unique_segments_found[5] = set(unique_pattern[index])
                unique_map[5] = index
                
        self.pattern2digit = dict()
        for key in unique_segments_found.keys():
            self.pattern2digit[''.join(sorted(unique_segments_found[key]))] = key
        # all done
    def __call__(self,output):
        if isinstance(output,list):
            return [self.pattern2digit[''.join(sorted(out))] for out in output]
        return self.pattern2digit[''.join(sorted(output))]

def day_08():
    print("******************************************************************")
    print("*                         DAY 8                                  *")
    print("******************************************************************")
    print("Part 1")
    # make dictionary mapping digit to true segments
    # solve for dictionary mapping real to true segments
    
    test_data = np.genfromtxt('./testinput_day08',dtype=str)
    data = np.genfromtxt('./input_day08',dtype=str)
    
    unique_patterns = []
    output_patterns = []
    for t in test_data:
        unique_patterns.append([''.join(sorted(s)) for s in t[:10]])
        output_patterns.append([''.join(sorted(s)) for s in t[11:]])
    proper_test_output = []
    for unique, output in zip(unique_patterns,output_patterns):
        proper_test_output.append(jumbled_display(unique)(output))
    
    print("test:",np.sum((np.array(proper_test_output) == 1) +
                   (np.array(proper_test_output) == 4) +
                   (np.array(proper_test_output) == 7) +
                   (np.array(proper_test_output) == 8)),"OK")
    
    unique_patterns = []
    output_patterns = []
    for t in data:
        unique_patterns.append([''.join(sorted(s)) for s in t[:10]])
        output_patterns.append([''.join(sorted(s)) for s in t[11:]])
    proper_output = []
    for unique, output in zip(unique_patterns,output_patterns):
        proper_output.append(jumbled_display(unique)(output))
    print("Result:",np.sum((np.array(proper_output) == 1) +
                   (np.array(proper_output) == 4) +
                   (np.array(proper_output) == 7) +
                   (np.array(proper_output) == 8)),"OK")
    
    
    print("Part 2")
    # join to integers
    proper_test_output = [int(''.join([str(d) for d in out])) for out in proper_test_output]
    proper_output = [int(''.join([str(d) for d in out])) for out in proper_output]
    print("Test:",np.sum(proper_test_output),"OK")
    print("Result:",np.sum(proper_output),"OK")
        

if __name__ == '__main__':
    main()