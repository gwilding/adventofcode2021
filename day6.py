#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:29:56 2021

@author: georg

Advent of code day 6
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def evolve_n_days(state,N_days,verbose=False):
    lanternfish_cycle_numbers = np.zeros(9,dtype=int)
    for t in state:
        lanternfish_cycle_numbers[t] += 1
    if verbose:
        print("Initial state: %i lanternfish"%(np.sum(lanternfish_cycle_numbers)))
    for k in range(1,N_days+1):
        # decrease all timers
        lanternfish_cycle_numbers = np.roll(lanternfish_cycle_numbers,-1)
        # nr of fishes reseting at age 6 is the number of fish that also give birth
        lanternfish_cycle_numbers[6] += lanternfish_cycle_numbers[8]
        # fish at 0 give birth to fish at 8 and roll over
        if verbose: 
            print("After day %i: %i lanternfish"%(k,
                                            np.sum(lanternfish_cycle_numbers)))
    return np.sum(lanternfish_cycle_numbers)
    
        

def day_06():
    print("******************************************************************")
    print("*                         DAY 6                                  *")
    print("******************************************************************")
    print("Part 1")
    possible_cycles = 9 # 0 .. 8
    test_state = [3,4,3,1,2]
    test_numbers = []
    state = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,
             4,5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,
             5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,
             4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,
             2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,
             4,4,4,5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,
             2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,
             1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,3,4,2,1,3,2,5,3,2,2,
             3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,2,2,4,
             2,1,4]
    # testing
    N_days = 18
    sum_of_fish = evolve_n_days(test_state,N_days,True)
    print("Test 1: Nr of lanterfish after %i days: %i"%(N_days,sum_of_fish))
    N_days = 80
    sum_of_fish = evolve_n_days(test_state,N_days)
    print("Test 2: Nr of lanterfish after %i days: %i"%(N_days,sum_of_fish))

    # solution
    N_days = 80
    sum_of_fish = evolve_n_days(state,N_days)
    print("Solution: Nr of lanterfish after %i days: %i"%(N_days,sum_of_fish))
    
    print("Part 2:")
    # testing
    N_days = 256
    sum_of_fish = evolve_n_days(test_state,N_days)
    print("Test: Nr of lanterfish after %i days: %i"%(N_days,sum_of_fish))

    # solution
    N_days = 256
    sum_of_fish = evolve_n_days(state,N_days)
    print("Solution: Nr of lanterfish after %i days: %i"%(N_days,sum_of_fish))
if __name__ == '__main__':
    main()