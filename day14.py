#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 06:03:08 2021

@author: georg

Advent of code 2021
Day 14
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def load_insertions(path_in):
    insertions = np.genfromtxt(path_in,skip_header=1,dtype=str)
    insertions = [(i[0],i[2]) for i in insertions]

    with open(path_in) as f:
        header = f.readline().rstrip()
    
    return header, insertions

def insert(header, insertion_rules,steps=1):
    new_header = header
    for s in range(steps):
        for k,i in enumerate(insertion_rules):
            while new_header.count(i[0]):
                new_header = new_header.replace(i[0],i[0][0]+'<'+str(k)+'>'+i[0][1])
        for k,i in enumerate(insertion_rules):
            # new_header = new_header.replace(str(k),i[1])
            new_header = new_header.replace('<'+str(k)+'>',i[1])
    return new_header
    

class polymer:
    def __init__(self,base):
        self.base = base
    def insert(self,insertion_rules):
        """
        Insert rules once.

        """
        for k,i in enumerate(insertion_rules):
            while self.base.count(i[0]):
                self.base = self.base.replace(i[0],i[0][0]+'<'+str(k)+'>'+i[0][1])
        for k,i in enumerate(insertion_rules):
            self.base = self.base.replace('<'+str(k)+'>',i[1])
        # return self.base
    def evolve(self,insertion_rules,n):
        for k in range(n):
            self.insert(self,insertion_rules)
    
class compressed_polymer:
    def __init__(self,base):
        base = base
        base_pairs = dict([[base[k:k+2],0] for k in range(len(base)-1)])
        for k in range(len(base)-1):
            base_pairs[base[k:k+2]] += 1
        bases = dict([[b,0] for b in base])
        for b in base:
            bases[b] += 1
        self.base_pairs = base_pairs
        self.bases = bases
    def insert(self,insertion_rules):
        new_base_pairs = dict()
        for i in insertion_rules:
            if i[0] in self.base_pairs.keys():
                # two new pairs
                new_1 = i[0][0] + i[1]
                new_2 = i[1] + i[0][1]
                
                if i[1] in self.bases.keys():
                    self.bases[i[1]] += self.base_pairs[i[0]]
                else:
                    self.bases[i[1]] = self.base_pairs[i[0]]
                
                if new_1 in new_base_pairs.keys():
                    new_base_pairs[new_1] += self.base_pairs[i[0]]
                else:
                    new_base_pairs[new_1] = self.base_pairs[i[0]]
                if new_2 in new_base_pairs.keys():
                    new_base_pairs[new_2] += self.base_pairs[i[0]]
                else:
                    new_base_pairs[new_2] = self.base_pairs[i[0]]
        self.base_pairs = new_base_pairs
    def evolve(self,insertion_rules,n):
        for k in range(n):
            self.insert(insertion_rules)
        
    
        
        
    
def day_14():
    print("******************************************************************")
    print("*                         DAY 14                                 *")
    print("******************************************************************")
    
    test_data_path = './testinput_day14'
    data_path = './input_day14'
    
    test_header, test_insertion_rules = load_insertions(test_data_path)
    header, insertion_rules = load_insertions(data_path)
    
    print("Part1:")
    test = []
    test.append(insert(test_header, test_insertion_rules,1))
    test.append(insert(test_header, test_insertion_rules,2))
    test.append(insert(test_header, test_insertion_rules,3))
    test.append(insert(test_header, test_insertion_rules,4))
    
    test_solution =['NCNBCHB',
                    'NBCCNBBBCBHCB',
                    'NBBBCNCCNBBNBNBBCHBHHBCHB',
                    'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB']
    
    for k in range(4):
        print(test[k], test[k] == test_solution[k])

    # old version
    test_10 = insert(test_header, test_insertion_rules,10)    
    counts = [test_10.count(check) for check in set(test_10) if test_10.count(check)>0]
    print("Test:",max(counts)-min(counts),"OK")        
    
    # new compressed version
    test_poly = compressed_polymer(test_header)
    test_poly.evolve(test_insertion_rules,10)
    print("Test (new):",max(test_poly.bases.values())-min(test_poly.bases.values()),"OK")
    
    # old result
    result = insert(header, insertion_rules,10)    
    counts = [result.count(check) for check in set(result) if result.count(check)>0]
    print("Solution:",max(counts)-min(counts),"OK")   

    cpoly = compressed_polymer(header)
    cpoly.evolve(insertion_rules,10)
    print("Solution (new):",max(cpoly.bases.values())-min(cpoly.bases.values()),"OK")

    print("Part 2:")
    
    cpoly = compressed_polymer(header)
    cpoly.evolve(insertion_rules,40)
    print("Solution (new):",max(cpoly.bases.values())-min(cpoly.bases.values()),"OK")

if __name__ == '__main__':
    main()