# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:21:07 2017

@author: 8ME-HW-171-L
"""
def user_prompt():
    
    strings_ub = input("What is the maximum number of strings to consider?")
    strings_ln = input("What is the minimum number of strings to consider?")
    string_its = input("How many iterations on the number of strings should be considered?")
    pitch_ub = input("What is the maximum E-W pitch to consider?")
    pitch_lb = input("What is the minimum E-W pitch to consider?")
    pitch_its = input("How many interations on pitch should be considered?")

    return strings_ub, strings_ln, string_its, pitch_ub, pitch_lb, pitch_its




