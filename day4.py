#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:36:27 2021

@author: georg

Advent of code day 4
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def play_bingo(boards, draws):
    """
    

    Parameters
    ----------
    boards : (n by L by L)
        array, containing n boards of shape L by L.
    draws : list
        list of bingo numbers drawn.

    Returns
    -------
    None.

    """
    boards = boards.copy()
    draws = draws.copy()

    drawn = np.zeros_like(boards,dtype=bool)
    wins = np.array([],dtype=int).reshape(-1,3)
    # wins_full = []
    for draw in draws:
        # if draw == 0:
        #     break
        drawn[boards == draw] = True
        # check whether any board has a new complete row or column
        is_winner_horizontal = np.where(drawn.all(axis=1).any(axis=1))[0]
        is_winner_vertical   = np.where(drawn.all(axis=2).any(axis=1))[0]
        
        if len(is_winner_horizontal):
            for winner in is_winner_horizontal:
                # wins_full.append([draw,winner,np.sum(boards[winner]*(~drawn[winner]))*draw])
                if not winner in wins[:,1]:
                    wins = np.vstack((wins,
                               [draw,winner,np.sum(boards[winner]*(~drawn[winner]))*draw]))
                # set board that has won to false, and fill with -1 ones to avoid future wins
                drawn[winner] = False
                boards[winner] = -1
        if len(is_winner_vertical):
            for winner in is_winner_vertical:
                # wins_full.append([draw,winner,np.sum(boards[winner]*(~drawn[winner]))*draw])
                if not winner in wins[:,1]:
                    wins = np.vstack((wins,
                               [draw,winner,np.sum(boards[winner]*(~drawn[winner]))*draw]))
                # set board that has won to false, and fill with -1 ones to avoid future wins
                drawn[winner] = False
                boards[winner] = -1
    return wins
    
def day_04():
    print("******************************************************************")
    print("*                         DAY 4                                  *")
    print("******************************************************************")
    print("Part 1")
    test_boards = np.genfromtxt('./testinput_day04',dtype=int)
    boardsize = test_boards.shape[1]
    test_boards = test_boards.reshape(-1,boardsize,boardsize)
    test_drawn = np.zeros_like(test_boards,dtype=bool)
    test_draws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    
    print("test: (board, result) = %a"%play_bingo(test_boards,test_draws)[0,1:])
    # print("Test result:",np.sum(test_boards[winner]*(~test_drawn[winner]))*draw)
    
    boards = np.genfromtxt('./input_day04',dtype=int,skip_header=1)
    boardsize = boards.shape[1]
    boards = boards.reshape(-1,boardsize,boardsize)
    draws = np.genfromtxt('./input_day04',dtype=int,
                          skip_footer=len(boards)*boardsize,
                          delimiter=',')
    print("solution: (board, result) = %a"%(play_bingo(boards,draws)[0,1:]))
    
    # part 2
    print("Part 2")
    print("test: (board, result) = %a"%play_bingo(test_boards,test_draws)[-1,1:])
    print("solution: (board, result) = %a"%(play_bingo(boards,draws)[-1,1:]))
if __name__ == '__main__':
    main()