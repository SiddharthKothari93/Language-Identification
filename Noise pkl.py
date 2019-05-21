# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:19:57 2019

@author: skoth
"""

import glob
import pickle
import librosa
import numpy as np

dirpath = "D:\IUB\DL\Project\Data\en 5000\en 5000 noise"

def gen_MFCCMagnitude(filepath):

  RawAmpVsTime, sr=librosa.load(filepath, sr=None)
  mfcc_spectrogram = librosa.feature.mfcc(y = RawAmpVsTime, n_mfcc = 40)
  mfcc_spectrogram = mfcc_spectrogram.T
  
  return mfcc_spectrogram


def loadFiles(filepattern):
  
  mfcc_spectrogram_List = []
  
  print(dirpath+filepattern)
  print(glob.glob(dirpath+filepattern))

  for file in sorted(glob.glob(dirpath+filepattern)):
    
    mfcc_spectrogram = gen_MFCCMagnitude(file)

    mfcc_spectrogram_List.append(mfcc_spectrogram)

  dictOfLists = {'mfcc_spectrogram':mfcc_spectrogram_List}
  
  return dictOfLists

Audio_with_noise = loadFiles("\*")

with open('D:\IUB\DL\Project\Data\en 5000\en2500_noise.pkl', 'wb') as f:
  pickle.dump(Audio_with_noise, f)
  
def zero_padding(data):
  data1 = []
  for i in range(len(data['mfcc_spectrogram'])):
    rec = []
    max_len = 972
    t_len = data['mfcc_spectrogram'][i].shape[0]
    zeros = np.array(np.zeros([max_len-t_len, 40]))
    seq = np.concatenate((data['mfcc_spectrogram'][i],zeros), axis=0)
#    seq = seq.T
    rec.append(seq)
    rec.append('English')
    data1.append(rec)
  data1 = np.array(data1)
  return data1
    
catalan_w_noise = zero_padding(Audio_with_noise)
    
    with open('D:\IUB\DL\Project\Data\en 5000\en2500_noise.pkl', 'wb') as f:
      pickle.dump(catalan_w_noise, f)