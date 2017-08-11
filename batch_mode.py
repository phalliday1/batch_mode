# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 14:19:56 2017

@author: 8ME-HW-171-L
"""


## Batch Mode Automation
import csv
import numpy as np
import pandas as pd
import time

user_inputs = user_prompt()


#strings_ub = input("What is the maximum number of strings to consider?")
#strings_lb = input("What is the minimum number of strings to consider?")
#strings_its = input("How many iterations on the number of strings should be considered?")
#pitch_ub = input("What is the maximum E-W pitch to consider?")
#pitch_lb = input("What is the minimum E-W pitch to consider?")
#pitch_its = input("How many interations on pitch should be considered?")
#hourly = False if raw_input("Do you want 8760s?").lower() == 'no' or 'No' or 'n' or 'N' else True

#project_name = 'AZ_Eloy1'
version = 'VC1'
timestamp = time.strftime("%c")

params = {"Create Hourly":["Create Hourly","file","File name"],
          "Number of Trackers":["Number","of trackers",""],
          "Trackers Pitch EW":["Trackers","Pitch EW","[m]"],
          "Trackers Pitch NS":["Trackers","Shift EW","[m]"],
          "Trackers Shift EW":["Trackers", "Shift EW","[m]"],
          "Trackers Axis Tilt":["Trackers","Axis Tilt","[deg]"],
          "Trackers Phi Min":["Trackers","Phi Min","[deg]"],
          "Trackers Phi Max":["Trackers","Phi Max","[deg]"],
          "Backtracking":["Backtracking","","Y/N"],
          "PV Module":["PV module","*.PAN File","FileName"],
          "Rserie":["Rserie","","[Ohm]"],
          "Rshunt":["Rshunt","","[Ohm]"],
          "Rsh(0)":["Rsh(0)","","[Ohm]"],
          "Number Modules in series":["Nb module","in series",""],
          "Number of Strings":["Nb strings","in parall",""],
          "Inverter":["Inverter","*.OND File","Filename"],
          "Nb inverter":["Nb inverter","or MPPT",""],
          "Thermal Uc":["Thermal","Uc fact","[W/m2K]"],
          "Thermal Uw":["Thermal","Uw fact","[W/m2K]"],
          "STC Losses":["DCWiring","Loss","[% STC]"],
          "Resistance Wiring":["Rwiring","Array","[mOhm]"],
          "Soiling Loss":["Soiling","Loss","[%]"],
          "Module Quality":["Mod. quality","loss","[%]"],
          "Mismatch loss":["Mismatch","Loss","[%]"],
          "LID loss":["LID","Loss","[%]"],
          "IAM ashrae":["IAM ashrae","bo param",""],
          "Comment":["Simul","Comment",""]}

batch = pd.DataFrame(index=range(0,50),columns=['PVsyst simulations Batch mode;'])

batch.iloc[0,0] = 'Simulation parameters definition;'
batch.iloc[1,0] = "File modified on %s;" % timestamp
batch.iloc[2,0] = ';'
batch.iloc[3,0] = 'Project ;;; %s;'% user_inputs['project_name']
batch.iloc[4,0] = ''
batch.iloc[5,0] = ';'
batch.iloc[6,0] = 'Please define the parameters to be varied for each run;'
batch.iloc[7,0] = "Don't modify anything in the column titles !;"
batch.iloc[8,0] = 'Only the lines beginngin by "SIM_" will be executed;'
batch.iloc[9,0] = ';'
if hourly == True:
    batch.iloc[10,0] = 'Ident;Create Hourly;%s;%s;Simul;;'% (params['Number of Trackers'][0], params['Trackers Pitch EW'][0])
    batch.iloc[11,0] = 'file;%s;%s;Comment;;'% (params['Number of Trackers'][1], params['Trackers Pitch EW'][1])
    batch.iloc[12,0] = 'File name;%s;%s'% (params['Number of Trackers'][2], params['Trackers Pitch EW'][2])
else:
    batch.iloc[10,0] = 'Ident;%s;%s;Simul;;'%(params['Number of Trackers'][0], params['Trackers Pitch EW'][0])
    batch.iloc[11,0] = ';%s;%s;Comment;;'% (params['Number of Trackers'][1], params['Trackers Pitch EW'][1])
    batch.iloc[12,0] = ';%s;%s;'% (params['Number of Trackers'][2], params['Trackers Pitch EW'][2])
batch.iloc[13,0] = ';'

int1 = user_inputs['strings_lb']
int2 = user_inputs['pitch_ln']
delta1 = (user_inputs['strings_ub']-user_inputs['strings_lb'])/user_inputs['strings_its']
delta2 = (user_inputs['pitch_ub']-user_inputs['pitch_lb'])/user_inputs['pitch_its']

while int1 <= user_inputs['strings_ub']:
    while int2 <= user_inputs['pitch_ub']:
        count=2
        batch.iloc[13+count-1,0] = 'SIM_%s;%s;%s;%s'% (count, int1, int2, project_name)
        int2 = delta2


batch.to_csv('./batch_test.csv',sep=',', index=False)



