#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:12:56 2021

@author: georg

Advent of code 2021
Day 10
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def check_chunks(line):
    chunk_dict = {'(': 1, ')': -1,
                  '[': 2, ']': -2,
                  '{': 3, '}': -3,
                  '<': 4, '>': -4}
    current_open = []
    corrupt = False
    for c in line:
        action = chunk_dict[c]
        if action > 0: # we can always open another chunk
            current_open += [action]
        elif action < 0: # we received a close action
            if current_open[-1] == -action: # close matches current open: close
                # close current open
                current_open.pop(-1)
            else:
                # print("Corrupt: %s"%c)
                corrupt = c
                break
    
    # end reached:
    # print(current_open)
    return corrupt, current_open

def check_lines(list_of_lines):
    results = []
    corrupt_lines = []
    open_lines = []
    for line in list_of_lines:
        line_result = check_chunks(line)
        results.append(line_result)
        if line_result[0]:
            corrupt_lines.append(line_result[0])
        else:
            open_lines.append(line_result[1])
    return corrupt_lines, open_lines

def day_10():
    print("******************************************************************")
    print("*                         DAY 10                                 *")
    print("******************************************************************")
    test_data = np.genfromtxt('./testinput_day10',dtype=str)
    data = np.genfromtxt('./input_day10',dtype=str)
 
    corruption_value_dict = {')': 3,
                             ']': 57,
                             '}': 1197,
                             '>': 25137}
    closing_value_dict = {')': 1,
                          ']': 2,
                          '}': 3,
                          '>': 4}
    
    print("Part 1")
    corrupt_test_lines,open_test_lines = check_lines(test_data)
    print("test:",
          np.sum([corruption_value_dict[c] for c in corrupt_test_lines]),
          "OK")
    
    
    corrupt_lines,open_lines = check_lines(data)
    print("Solution:",
          np.sum([corruption_value_dict[c] for c in corrupt_lines]),
          "OK")
    
    print("Part 2")
    test_closing_scores = []
    for line in open_test_lines:
        score = 0
        for close in line[::-1]:
            score = score*5 + np.abs(close)
        test_closing_scores.append(score)
    print("Test:",
          int(np.median(test_closing_scores)),
          "OK")
    
    
    closing_scores = []
    for line in open_lines:
        score = 0
        for close in line[::-1]:
            score = score*5 + np.abs(close)
        closing_scores.append(score)
    print("Solution:",
          int(np.median(closing_scores)),
          "OK")
    
if __name__ == '__main__':
    main()