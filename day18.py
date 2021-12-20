#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:38:21 2021

@author: georg

Advent of code 2021
Day 18
"""

import numpy as np
import copy
import matplotlib.pyplot as plt

def main():
    pass

class snail:
    def __init__(self,string_or_list_or_snail):
        if isinstance(string_or_list_or_snail,snail):
            self.sn = string_or_list_or_snail.sn
        elif isinstance(string_or_list_or_snail,list):
            self.sn = string_or_list_or_snail
        else:
            sn = self.getsnail_recursive(string_or_list_or_snail)
            self.sn = sn
        self.m = self.magnitude(self.sn)
    def __add__(self,other):
        new_snail = [copy.deepcopy(self.sn),copy.deepcopy(other.sn)]
        actions = [explode, split]
        do_action = 0
        while do_action < 2:
            new_snail, action_done = actions[do_action](new_snail)
            do_action += 1
            if action_done: do_action = 0
        return snail(new_snail)
    def __repr__(self):
        return str(self.sn)
    def magnitude(self,sn):
        if isinstance(sn, int):
            return sn
        else:
            return 3*self.magnitude(sn[0]) + 2*self.magnitude(sn[1])
    def sf(self,string):
        return [int(p) if p.isnumeric() else p for p in list(string.replace(',',''))]
    def getsnail_recursive(self,string_list):
        if isinstance(string_list,str):
            return self.getsnail_recursive(self.sf(string_list))
        if isinstance(string_list,int):
            return string_list
        elif len(string_list) == 4:
            return [string_list[1],string_list[2]]
        elif len(string_list) > 4:
            first_open = string_list.index('[')
            last_close = len(string_list) - string_list[::-1].index(']') - 1
            inner = string_list[first_open+1:last_close]
            if isinstance(inner[0],int):
                first_half = inner[0]
                second_half = inner[1:]
            else: 
                still_open = 1
                k = 1
                while still_open:
                    if inner[k] == '[':
                        still_open += 1
                    elif inner[k] == ']':
                        still_open -= 1
                    k += 1
                first_half = inner[0:k]
                second_half = inner[k:]
            if isinstance(second_half[0], int):
                second_half = second_half[0]
            return [self.getsnail_recursive(first_half),
                    self.getsnail_recursive(second_half)]

def dirtyaddright(sn,right):
    sn = copy.deepcopy(sn)
    replace_next = False
    for k0,s0 in enumerate(sn):
        if isinstance(s0,int):
            if not replace_next and s0 == -1:
                replace_next = not replace_next
            elif replace_next and s0 != -1:
                sn[k0] += right
                return sn
            continue
        for k1,s1 in enumerate(s0):
            if isinstance(s1,int):
                if not replace_next and s1 == -1:
                    replace_next = not replace_next
                elif replace_next and s1 != -1:
                    sn[k0][k1] += right
                    return sn
                continue
            for k2,s2 in enumerate(s1):
                if isinstance(s2,int):
                    if not replace_next and s2 == -1:
                        replace_next = not replace_next
                    elif replace_next and s2 != -1:
                        sn[k0][k1][k2] += right
                        return sn
                    continue
                for k3,s3 in enumerate(s2):
                    if isinstance(s3,int):
                        if not replace_next and s3 == -1:
                            replace_next = not replace_next
                        elif replace_next and s3 != -1:
                            sn[k0][k1][k2][k3] += right
                            return sn
                        continue
                    for k4,s4 in enumerate(s3):
                        if isinstance(s4,int):
                            if not replace_next and s4 == -1:
                                replace_next = not replace_next
                            elif replace_next and s4 != -1:
                                sn[k0][k1][k2][k3][k4] += right
                                return sn
                            continue
    return sn

def explode(sn):
    sn = copy.deepcopy(sn)
    for k0 in [0,1]:
        if isinstance(sn[k0],int): continue
        for k1 in [0,1]:
            if isinstance(sn[k0][k1],int): continue
            for k2 in [0,1]:
                if isinstance(sn[k0][k1][k2],int): continue
                for k3 in [0,1]:
                    if isinstance(sn[k0][k1][k2][k3],int): continue
                    left = sn[k0][k1][k2][k3][0]
                    right = sn[k0][k1][k2][k3][1]
                    sn[k0][k1][k2][k3] = -1
                    
                    sn = dirtyaddright(sn,right)
                    sn = flip(dirtyaddright(flip(sn),left))
                    
                    sn[k0][k1][k2][k3] = 0
                    
                    return sn, True
    return sn, False

def split(sn):
    sn = copy.deepcopy(sn)
    for k0 in [0,1]:
        if isinstance(sn[k0],int):
            if sn[k0] > 9:
                sn[k0] = [int(np.floor(sn[k0]/2)),
                          int(np.ceil(sn[k0]/2))]
                return sn, True
            continue
        for k1 in [0,1]:
            if isinstance(sn[k0][k1],int):
                if sn[k0][k1] > 9:
                    sn[k0][k1] = [int(np.floor(sn[k0][k1]/2)),
                                  int(np.ceil(sn[k0][k1]/2))]
                    return sn, True
                continue
            for k2 in [0,1]:
                if isinstance(sn[k0][k1][k2],int):
                    if sn[k0][k1][k2]> 9:
                        sn[k0][k1][k2] = [int(np.floor(sn[k0][k1][k2]/2)),
                                          int(np.ceil(sn[k0][k1][k2]/2))]
                        return sn, True
                    continue
                for k3 in [0,1]:
                    if isinstance(sn[k0][k1][k2][k3],int):
                        if sn[k0][k1][k2][k3] > 9:
                            sn[k0][k1][k2][k3] = [int(np.floor(sn[k0][k1][k2][k3]/2)),
                                                  int(np.ceil(sn[k0][k1][k2][k3]/2))]
                            return sn, True
                        continue
                    for k4 in [0,1]:
                        if isinstance(sn[k0][k1][k2][k3][k4],int):
                            if sn[k0][k1][k2][k3][k4] > 9:
                                sn[k0][k1][k2][k3][k4] = [int(np.floor(sn[k0][k1][k2][k3][k4]/2)),
                                                          int(np.ceil(sn[k0][k1][k2][k3][k4]/2))]
                                return sn, True
                            continue
    return sn, False
                    
def flip(sn):
    if isinstance(sn,int):
        return sn
    else:
        return [flip(sn[1]),flip(sn[0])]

def day_18():
    print("******************************************************************")
    print("*                         DAY 18                                 *")
    print("******************************************************************")
    
    stringb = np.genfromtxt('/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day18b',dtype=str)
    stringc = np.genfromtxt('/home/georg/Dropbox/georg/scripts/aoc2021/testinput_day18c',dtype=str)
    string = np.genfromtxt('/home/georg/Dropbox/georg/scripts/aoc2021/input_day18',dtype=str)
    
    
    
    print("Part 1:")
    snails_b = [snail(s) for s in stringb]
    snail_sum_b = snails_b[0]
    for sn in snails_b[1:]:
        snail_sum_b = snail_sum_b + sn
    solution_snail_sum_b = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    print(snail_sum_b,solution_snail_sum_b == snail_sum_b.sn)
    
    snails_c = [snail(s) for s in stringc]
    snail_sum_c = snails_c[0]
    for sn in snails_c[1:]:
        snail_sum_c = snail_sum_c + sn
    solution_snail_sum_c = [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
    print("test c:",snail_sum_c,snail_sum_c.sn == solution_snail_sum_c)
    print("test c:",snail_sum_c.m,snail_sum_c.m == 4140)
    
    snails = [snail(s) for s in string]
    snail_sum = snails[0]
    for sn in snails[1:]:
        snail_sum = snail_sum + sn
    print("solution:",snail_sum.m,"OK")
    
    print("Part 2:")
    snails_c = [snail(s) for s in stringc]
    max_m = 0
    for sn1 in snails_c:
        for sn2 in snails_c:
            mtemp = (sn1+sn2).m 
            if mtemp > max_m:
                max_m = mtemp
    print("test c:",max_m,"OK")
    
    snails = [snail(s) for s in string]
    max_m = 0
    for sn1 in snails:
        for sn2 in snails:
            mtemp = (sn1+sn2).m 
            if mtemp > max_m:
                max_m = mtemp
    print("solution:",max_m,"OK")

if __name__ == '__main__':
    main()