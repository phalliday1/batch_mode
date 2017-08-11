# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:21:07 2017

@author: 8ME-HW-171-L
"""
def user_prompt():
    
    strings_ub = input("What is the maximum number of strings to consider?")
    strings_lb = input("What is the minimum number of strings to consider?")
    strings_its = input("How many iterations on the number of strings should be considered?")
    pitch_ub = input("What is the maximum E-W pitch to consider?")
    pitch_lb = input("What is the minimum E-W pitch to consider?")
    pitch_its = input("How many interations on pitch should be considered?")
    
    inputs= {'strings_ub':strings_ub,
             'strings_lb':strings_lb,
             'strings_its':strings_its,
             'pitch_ub':pitch_ub,
             'pitch_lb':pitch_lb,
             'pitch_its':pitch_its}

    return inputs




