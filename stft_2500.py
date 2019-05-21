# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:27:11 2019

@author: patil
"""

import glob
import pickle
import librosa
import numpy as np

dirpath = "D:/IUB/DL/Project/Data/en 5000/en 2500 noise"####

def gen_stft(filepath):
  RawAmpVsTime, sr = librosa.load(filepath, offset=0.6, duration=5.6)
  stft_spectrogram = librosa.stft(RawAmpVsTime, hop_length=500, n_fft = 256)
  stft_spectrogram = stft_spectrogram.T
  stft_spectrogram_abs = np.abs(stft_spectrogram)
  
  return stft_spectrogram_abs

def loadFiles(filepattern):
  
  stft_spectrogram_List = []
  
  print(dirpath+filepattern)
  print(glob.glob(dirpath+filepattern))
  i = 0
  for file in sorted(glob.glob(dirpath+filepattern)):
    i = i+1
    print(i)
      
    stft = gen_stft(file)
#    stft = stft[:247,]

    stft_spectrogram_List.append(stft)

  dictOfLists = {'stft':stft_spectrogram_List}
  labels = ['English' for i in range(len(dictOfLists['stft']))]####
  dictOfLists['labels'] = labels
  
  return dictOfLists

Audio_with_noise = loadFiles("/*")

lang = Audio_with_noise['labels'][0]
print('Language:',lang)
print('shape stft:', Audio_with_noise['stft'][0].shape)
print('length',len(Audio_with_noise['stft']),len(Audio_with_noise['labels']))

with open('D:/IUB/DL/Project/Data/en 5000/'+lang+'_w_Noise_stft_2500.pkl', 'wb') as f:
  pickle.dump(Audio_with_noise, f)

Audio_with_noise['stft'][10].shape
#del(Audio_with_noise)
