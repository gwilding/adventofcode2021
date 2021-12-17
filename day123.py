#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:38:52 2021

@author: georg

aoc 2021
day 1

"""

import numpy as np
import matplotlib.pyplot as plt

def day_01():
    measurements = np.genfromtxt('./input_day01')
    print(sum(np.diff(measurements)>0))
    
    ma_3 = measurements[:-2] + measurements[1:-1] + measurements[2:]
    
    print(sum(np.diff(ma_3)>0))

class submarine:
    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.horizontal_position = 0
    def do(self,command,x):
        if command == 'up':
            self.aim -= x
        elif command == 'down':
            self.aim += x
        elif command == 'forward':
            self.horizontal_position += x
            self.depth += self.aim*x
    def __repr__(self):
        return 'H, D, A: (%i, %i, %i)'%(self.horizontal_position,self.depth, self.aim)

def day_02():
    commands = np.genfromtxt('./input_day02',dtype=str)
    commands = [[c[0],int(c[1])] for c in commands]
    
    test_commands = [['forward', 5],
                    ['down', 5],
                    ['forward', 8],
                    ['up', 3],
                    ['down', 8],
                    ['forward', 2]]
    
    # this can probably be done better
    dict_up_down = {'up': -1, 'down': 1, 'forward': 1}
    dict_steer_pos = {'up':1, 'down':1 ,'forward': 0}
    
    horizontal = 0
    depth = 0
    pos = [horizontal,depth]
    for c in test_commands:
        pos[dict_steer_pos[c[0]]] += c[1]*dict_up_down[c[0]]
    print("Test",pos,np.prod(pos))
    
    horizontal = 0
    depth = 0
    pos = [horizontal,depth]
    for c in commands:
        pos[dict_steer_pos[c[0]]] += c[1]*dict_up_down[c[0]]
    print("Final",pos,np.prod(pos))
    
    # part 2
    # testing
    sub = submarine()
    for c in test_commands:
        sub.do(c[0],c[1])
    sub
    print("Testing",sub.depth*sub.horizontal_position)
    
    sub = submarine()
    for c in commands:
        sub.do(c[0],c[1])
    sub
    print("Solution",sub.depth*sub.horizontal_position)

def day_03():
    test_report = ['00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010']
    test_report = np.array([list(r) for r in test_report],dtype=int)
    
    gamma = [sorted(r)[len(test_report)//2] for r in test_report.T]
    epsilon = [1*(not g) for g in gamma]
    
    gamma = ''.join([str(g) for g in gamma])
    epsilon = ''.join([str(g) for g in epsilon])
    
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    print("test:")
    print('gamma: ', gamma)
    print('epsilon: ', epsilon)
    print('product: ', gamma*epsilon)
    
    report = np.genfromtxt('./input_day03',dtype=str)
    report = np.array([list(r) for r in report],dtype=int)
    
    gamma = [sorted(r)[len(report)//2] for r in report.T]
    epsilon = [1*(not g) for g in gamma]
    
    gamma = ''.join([str(g) for g in gamma])
    epsilon = ''.join([str(g) for g in epsilon])
    
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    print("Result:")
    print('gamma: ', gamma)
    print('epsilon: ', epsilon)
    print('product: ', gamma*epsilon)
    
    
    # part 2 (testing)
    interative_report = test_report.copy()
    oxygen = []
    while interative_report.shape[0] > 1:
        # test_report[:,k]
        select_criterion = sorted(interative_report[:,0])[len(interative_report)//2]
        oxygen.append(select_criterion)
        interative_report = interative_report[interative_report[:,0] == select_criterion,1:]
    oxygen += list(interative_report[0])
    
    interative_report = test_report.copy()
    co2scrubber = []
    while interative_report.shape[0] > 1:
        # test_report[:,k]
        select_criterion = 1*(not sorted(interative_report[:,0],reverse=False)[len(interative_report)//2])
        co2scrubber.append(select_criterion)
        interative_report = interative_report[interative_report[:,0] == select_criterion,1:]
    co2scrubber += list(interative_report[0])
        
    oxygen = ''.join([str(g) for g in oxygen])
    co2scrubber = ''.join([str(g) for g in co2scrubber])
    
    oxygen = int(oxygen,2)
    co2scrubber = int(co2scrubber,2)
    print("test:")
    print('gamma: ', oxygen)
    print('epsilon: ', co2scrubber)
    print('product: ', oxygen*co2scrubber)
    
    # part 2
    # put this in a function for later!
    interative_report = report.copy()
    oxygen = []
    while interative_report.shape[0] > 1:
        # test_report[:,k]
        select_criterion = sorted(interative_report[:,0])[len(interative_report)//2]
        oxygen.append(select_criterion)
        interative_report = interative_report[interative_report[:,0] == select_criterion,1:]
    oxygen += list(interative_report[0])
    
    interative_report = report.copy()
    co2scrubber = []
    while interative_report.shape[0] > 1:
        # test_report[:,k]
        select_criterion = 1*(not sorted(interative_report[:,0],reverse=False)[len(interative_report)//2])
        co2scrubber.append(select_criterion)
        interative_report = interative_report[interative_report[:,0] == select_criterion,1:]
    co2scrubber += list(interative_report[0])
        
    oxygen = ''.join([str(g) for g in oxygen])
    co2scrubber = ''.join([str(g) for g in co2scrubber])
    
    oxygen = int(oxygen,2)
    co2scrubber = int(co2scrubber,2)
    print("Result:")
    print('gamma: ', oxygen)
    print('epsilon: ', co2scrubber)
    print('product: ', oxygen*co2scrubber)

def main():
    pass
    # day_01()
    # day_02()
    # day_03()

if __name__ == '__main__':
    main()