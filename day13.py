#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:32:29 2021

@author: georg

Advent of code 2021
Day 13
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def load_origami(path_in):
    c = 0
    positions = []
    folds = []
    with open(path_in) as f:
        while True:
            c += 1
            line = f.readline()
            if not line:
                break
            if ',' in line:
                positions.append(line.rstrip())
            elif 'fold' in line:
                folds.append(line.rstrip())
    positions = [ tuple([int(p) for p in pos.split(',')]) for pos in positions]
    
    folds = [ fo.replace('fold along ','').split('=') for fo in folds]
    folds = [(f[0],int(f[1])) for f in folds]
    return positions, folds

class origami:
    def __init__(self,positions):
        sheet = np.zeros(np.max(np.array(positions),0)+1,dtype=bool)
        for p in positions:
            sheet[tuple(p)] = True
        self.sheet = sheet.T
        self.sum = np.sum(self.sheet)
    def __repr__(self):
        return str(np.sum(self.sheet)) + "\n" + str(self.sheet*1)
    def show(self):
        plt.matshow(self.sheet)
    def fold(self,instruction):
        """
        x is to the right
        y is down
        
        """
        if not isinstance(instruction, tuple):
            for i in instruction:
                self.fold(i)
        else:
            x_or_y, line = instruction
            if x_or_y == 'x': # fold LEFT -> transpose
                self.sheet = self.sheet.T
            layer_1 = self.sheet[:line,:]
            layer_2 = self.sheet[line+1:,:]
            new_layer = layer_1 + layer_2[::-1,:]
            self.sheet = new_layer
            if x_or_y == 'x': # fold LEFT
                self.sheet = self.sheet.T
            self.sum = np.sum(self.sheet)
        # return self
        

    
def day_13():
    print("******************************************************************")
    print("*                         DAY 13                                 *")
    print("******************************************************************")
    
    test_data_path = './testinput_day13'
    data_path = './input_day13'
    
    test_pos,test_folds = load_origami(test_data_path)
    pos,folds = load_origami(data_path)
    
    print("Part1:")
    ori_test = origami(test_pos)
    ori_test.fold(test_folds[0])
    
    ori = origami(pos)
    ori.fold(folds[0])
    
    print("Test:",ori_test.sum,"(17) OK")
    print("Solution:",ori.sum,"(724) OK")
    
    
    print("Part2:")
    ori = origami(pos)
    ori.fold(folds)
    ori.show()
    print("Solution: CPJBERUL")

if __name__ == '__main__':
    main()