#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 06:02:35 2021

@author: georg

Advent of code 2021
Day 16
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def hex2bin(string):
    binrep = ''
    for s in string:
        bin_string = bin(int(s,16))[2:]
        bin_string = '0'*(4 - len(bin_string)) + bin_string
        binrep += bin_string
    return binrep

def resolve_header(bstring):
    if set(bstring) == {'0'} or set(bstring)  == set():
        return [], '0'
    version = int(bstring[:3],2)
    type_ID =int(bstring[3:6],2)
    content_part = bstring[6:]
    return version, type_ID, content_part

def greater_than(x):
    return (x[0] > x[1])*1
def less_than(x):
    return (x[0] < x[1])*1
def equal(x):
    return (x[0] == x[1])*1

def decode(bstring,versioncount=[0],verbose=False):
    version, type_ID, content_part = resolve_header(bstring)
    
    # keep track of version count (for part 1)
    versioncount[0] += version
    blocksize_dict = {'0': 15, '1': 11}
    
    # literal package
    if type_ID == 4:
        buffer = content_part
        read_buffer = ''
        while buffer[0] == '1':
            read_buffer += buffer[1:5]
            buffer = buffer[5:]
        read_buffer += buffer[1:5]
        buffer = buffer[5:]
        if verbose: print("Version %i, Type ID %i, literal: %i"%(version,
                                                                 type_ID,
                                                                 int(read_buffer,2)))
        return int(read_buffer,2), buffer
    
    buffer = content_part
    type_length_ID = buffer[0]
    buffer = buffer[1:]
    
    # length OR number of packages
    len_or_pack = int(buffer[:blocksize_dict[type_length_ID]],2)
    # skip length bits
    buffer = buffer[blocksize_dict[type_length_ID]:]
    
    content = []
    if type_length_ID == '0':
        active_buffer = buffer[:len_or_pack]
        rest_buffer = buffer[len_or_pack:]
        while len(active_buffer):
            read_buffer, active_buffer = decode(active_buffer,versioncount,verbose=verbose)
            content.append(read_buffer)
        buffer = active_buffer + rest_buffer
    elif type_length_ID == '1':
        for k in range(len_or_pack):
            read_buffer, buffer = decode(buffer,versioncount,verbose=verbose)
            content.append(read_buffer)
    
    # for possible later expansion
    action_dict = {0: np.sum,
                   1: np.prod,
                   2: np.min,
                   3: np.max,
                   5: greater_than,
                   6: less_than,
                   7: equal}
    if verbose: print("Version %i, Type ID %i, Type length ID %s, result: %s = %i"%(version,
                                                                   type_ID,
                                                                   type_length_ID,
                                                                   action_dict[type_ID].__name__,
                                                                   action_dict[type_ID](content)))
    
    return action_dict[type_ID](content), buffer

def day_16():
    print("******************************************************************")
    print("*                         DAY 16                                 *")
    print("******************************************************************")
    
    data_path = './input_day16'
    
    with open(data_path) as f:
        data = f.readline().rstrip()
    
    string = 'D2FE28'
    bstring = hex2bin(string)
    decode(bstring)
    
    string = '38006F45291200'
    bstring = hex2bin(string)
    decode(bstring)
    
    string = 'EE00D40C823060'
    bstring = hex2bin(string)
    decode(bstring)
    print("Part 1:")
    
    string_list = ['D2FE28',
                   '38006F45291200',
                   'EE00D40C823060',
                   '8A004A801A8002F478',
                   '620080001611562C8802118E34',
                   'C0015000016115A2E0802F182340',
                   'A0016C880162017C3686B18A3D4780']
    
    
    for s in string_list:
        versioncount = [0]
        content,_ = decode(hex2bin(s),versioncount)
        print(versioncount[0])
    versioncount = [0]
    decode(hex2bin(data),versioncount)
    
    print("Part 2:")
    string_list = ['C200B40A82',
                   '04005AC33890',
                   '880086C3E88112',
                   'CE00C43D881120',
                   'D8005AC2A8F0',
                   'F600BC2D8F',
                   '9C005AC2F8F0',
                   '9C0141080250320F1802104A08']
    test_output = [3, 54, 7, 9, 1, 0, 0, 1]
    for s,test_content in zip(string_list,test_output):
        content, remaining_buffer = decode(hex2bin(s))
        print(content,remaining_buffer, content == test_content)
        
    
    print("Solution:",decode(hex2bin(data),versioncount)[0],"OK")
    

if __name__ == '__main__':
    main()