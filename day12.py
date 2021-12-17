#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:00:30 2021

@author: georg

Advent of code 2021
Day 12
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

class graph:
    def __init__(self,edges=None):
        # build graph
        if edges is None:
            graph_dict = {}
        else:
            graph_dict = {}
            for c in edges:
                if c[0] in graph_dict.keys():
                    graph_dict[c[0]].append(c[1])
                else:
                    graph_dict[c[0]] = [c[1]]
                if c[1] in graph_dict.keys():
                    graph_dict[c[1]].append(c[0])
                else:
                    graph_dict[c[1]] = [c[0]]
        self.graph_dict = graph_dict
        n = len(list(graph_dict.keys()))
        vertices = list(graph_dict.keys())
        vertex_id = dict([[v,k]for k,v in enumerate(vertices)])
        self.n = n
        self.vertices = vertices
        self.vertex_id = vertex_id
        
    def paths(self,start,end,allow_lowercase=1,verbose=True):
        # now go through all possible paths iteratively
        visited = [0] * self.n
        pathcount = [0]
        # variable for storing all paths, if needed later
        self.all_paths = []
        travelled = ''
        self.paths_recursive(start, end, visited, pathcount, travelled, allow_lowercase,verbose)
        return pathcount[0]
    
    def paths_recursive(self, start, end, visited, pathcount,travelled, allow_lowercase,verbose):
        # keep track of the travelled path
        travelled = travelled + " -> " + start
        # lowercase cannot be visited twice
        if start.islower():
            visited[self.vertex_id[start]] += 1
        # end reached
        if (start == end):
            pathcount[0] += 1
            if verbose: print("end reached:",travelled)
            self.all_paths.append(travelled)
        # try all connections of vertex
        i = 0
        while i < len(self.graph_dict[start]):
            # switch for higher number of visits to lowercase cave
            if allow_lowercase > 1:
                if (((not allow_lowercase in visited) or
                    (not visited[self.vertex_id[self.graph_dict[start][i]]])) and
                    (not visited[self.vertex_id['start']] == allow_lowercase) and
                    (not visited[self.vertex_id['end']] == 1)):
                    self.paths_recursive(self.graph_dict[start][i], end,
                                        visited, pathcount, travelled, allow_lowercase,verbose)
            else:
                if (not visited[self.vertex_id[self.graph_dict[start][i]]]):
                    self.paths_recursive(self.graph_dict[start][i], end,
                                        visited, pathcount, travelled, allow_lowercase,verbose)
            i += 1
        if start.islower():
            visited[self.vertex_id[start]] -= 1


def day_12():
    print("******************************************************************")
    print("*                         DAY 12                                 *")
    print("******************************************************************")
    test_data_a = np.genfromtxt('./testinput_day12a',dtype=str)
    test_data_b = np.genfromtxt('./testinput_day12b',dtype=str)
    test_data_c = np.genfromtxt('./testinput_day12c',dtype=str)
    data = np.genfromtxt('./input_day12',dtype=str)
    
    print("Part1:")
    test_a_connections = [(c.split('-')[0],c.split('-')[1]) for c in test_data_a]
    test_b_connections = [(c.split('-')[0],c.split('-')[1]) for c in test_data_b]
    test_c_connections = [(c.split('-')[0],c.split('-')[1]) for c in test_data_c]
    data = [(c.split('-')[0],c.split('-')[1]) for c in data]
    
    
    ga = graph(test_a_connections)
    paths_test_a = ga.paths('start','end')
    gb = graph(test_b_connections)
    paths_test_b = gb.paths('start','end')
    gc = graph(test_c_connections)
    paths_test_c = gc.paths('start','end')
    
    gs = graph(data)
    paths_solution = gs.paths('start','end')
    
    print("Test a:",paths_test_a,"(10) OK")
    print("Test b:",paths_test_b,"(19) OK")
    print("Test c:",paths_test_c,"(226) OK")
    print("Solution:",paths_solution,"(3298) OK")
    
    
    print("Part2:")
    
    ga = graph(test_a_connections)
    paths_test_a = ga.paths('start','end',2)
    gb = graph(test_b_connections)
    paths_test_b = gb.paths('start','end',2)
    gc = graph(test_c_connections)
    paths_test_c = gc.paths('start','end',2)
    
    gs = graph(data)
    paths_solution = gs.paths('start','end',2,verbose=False)
    
    print("Test a:",paths_test_a,"(36) OK")
    print("Test b:",paths_test_b,"(103) OK")
    print("Test c:",paths_test_c,"(3509) OK")
    print("Solution:",paths_solution,"OK")

    
    
    
if __name__ == '__main__':
    main()