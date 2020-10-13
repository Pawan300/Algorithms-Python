# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:57:36 2018

@author: pawan_300
"""
import pandas as pd
import csv
filename=r"C:\Users\pawan_300\Desktop\demo_feedback.csv"
data=pd.read_csv(filename)
data=data.fillna(method='bfill')
data.to_csv(r"C:\Users\pawan_300\Desktop\d_feedback.csv")  