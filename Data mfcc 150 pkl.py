# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:16:02 2019

@author: skoth
"""

import glob
import pickle
import librosa
import numpy as np

dirpath = "D:\IUB\DL\Project\Temp data\de 5000\de 5000"

def gen_MFCCMagnitude(filepath):

  RawAmpVsTime, sr=librosa.load(filepath, sr=None)
  mfcc_spectrogram = librosa.feature.mfcc(y = RawAmpVsTime, n_mfcc = 150)
  mfcc_spectrogram = mfcc_spectrogram.T
  
  return mfcc_spectrogram


def loadFiles(filepattern):
  
  mfcc_spectrogram_List = []
  
  print(dirpath+filepattern)
  print(glob.glob(dirpath+filepattern))
  i = 0
  for file in sorted(glob.glob(dirpath+filepattern)):
    i = i+1
    print(i)
      
    mfcc_spectrogram = gen_MFCCMagnitude(file)

    mfcc_spectrogram_List.append(mfcc_spectrogram)

  dictOfLists = {'mfcc_spectrogram':mfcc_spectrogram_List}
  
  return dictOfLists

Audio_with_noise = loadFiles("\*")

with open('D:\IUB\DL\Project\Temp data\de 5000\de5000.pkl', 'wb') as f:
  pickle.dump(Audio_with_noise, f)

del(Audio_with_noise)