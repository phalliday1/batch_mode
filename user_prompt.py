# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:21:07 2017

@author: 8ME-HW-171-L
"""
def main():
    
    strings_ub = raw_input("What is the maximum number of strings to consider?")
    strings_lb = raw_input("What is the minimum number of strings to consider?")
    strings_its = raw_input("How many iterations on the number of strings should be considered?")
    pitch_ub = raw_input("What is the maximum E-W pitch to consider?")
    pitch_lb = raw_input("What is the minimum E-W pitch to consider?")
    pitch_its = raw_input("How many interations on pitch should be considered?")
    proj_name = raw_input("What is the PVSyst project name?")
    
    #inputs= {'strings_ub':float(strings_ub),
#             'strings_lb':float(strings_lb),
#             'strings_its':float(strings_its),
#             'pitch_ub':float(pitch_ub),
#             'pitch_lb':float(pitch_lb),
#             'pitch_its':float(pitch_its),
#             'name':proj_name}

    return float(strings_ub), float(strings_lb), float(strings_its), float(pitch_ub), float(pitch_lb), float(pitch_its), proj_name




