'''
Title: Time-Stepping Naked Planet Model
Author: Kaitlyn Stark
Date: Sept 7, 2022

Purpose:
'''

import numpy
import matplotlib.pyplot

# variable definitions
time_step = 5
water_depth = 5
heat_capacity = 5 # units J/m^2K
s = 5 # solar constant
epsilon = 5
sigma = 5
e_inflx = 5 # units: W/m^2

time_li = []
temp_li = [0]

n_steps = int(input(""))

for i in range(0, n_steps):
    time_li.append(i*time_step)


