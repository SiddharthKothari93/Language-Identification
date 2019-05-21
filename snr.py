# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:07:28 2019

@author: skoth
"""
import os
import librosa
import numpy as np

dirpath = "D:/IUB/DL/Project/Data/en 5000/en 2500 noise 30db"

audio = os.listdir(dirpath)


SNR = []
counter = 0
for i in audio:
    counter = counter + 1
    print(counter)
    Audio_Noise, sr=librosa.load("D:/IUB/DL/Project/Data/en 5000/en 2500 noise 30db/" + i, sr=None)
    Audio_wo_Noise,  sr = librosa.load("D:/IUB/DL/Project/Data/en 5000/en 5000 wav/" + i, sr=None)
    min_value = min(len(Audio_Noise),len(Audio_wo_Noise))
    SNR.append(10*(np.log10(np.sum(np.square(Audio_wo_Noise[:min_value]))/np.sum(np.square(np.subtract(Audio_wo_Noise[:min_value],Audio_Noise[:min_value]))))))

import seaborn as sns
sns.set(color_codes=True)
sns.distplot(SNR)
for i in range(len(SNR)):
    if SNR[i] < -100000:
        SNR[i] = -100000
np.sort(SNR)
print(np.average(SNR))
print(len(SNR))