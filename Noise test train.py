# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 04:11:05 2019

@author: skoth
"""


import glob
import pickle
import librosa
import numpy as np
import os

dirpath = "D:/IUB/DL/Project/Data/Noise pkl"

audio = os.listdir(dirpath)


with open(dirpath + "/" + audio[0], 'wb') as f:
  print(f)
    