# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:33:19 2019

@author: skoth
"""
import librosa
import glob
import numpy as np
import pickle

dirpath = "D:\\IUB\\DL\\Project\\Data\\ca 5000\\ca 5000 wav\\"####

def gen_stft(filepath):
  RawAmpVsTime, sr = librosa.load(filepath, offset=0.6, duration=5.6)
  mel_spectrogram = librosa.feature.melspectrogram(RawAmpVsTime, sr=sr)
  mel_spectrogram = mel_spectrogram.T
  mel_spectrogram_abs = np.abs(mel_spectrogram)
  
  return mel_spectrogram_abs

def loadFiles(filepattern):
  
  mel_spectrogram_List = []
  
  print(dirpath+filepattern)
#  print(glob.glob(dirpath+filepattern))
  i = 0
  for file in sorted(glob.glob(dirpath+filepattern)[:2500]):
    i = i+1
    if i%100==0:
        print(i)
      
    #while len(mel_spectrogram_List)<2500:
    mel = gen_stft(file)
#    stft = stft[:247,]
    mel_spectrogram_List.append(mel)

  dictOfLists = {'mel':mel_spectrogram_List}
  labels = ['Catalan' for i in range(len(dictOfLists['mel']))]####
  dictOfLists['labels'] = labels
  
  return dictOfLists

mel_spec_w_label = loadFiles("*")

lang = mel_spec_w_label['labels'][0]
print('Language:',lang)
print('shape mel:', mel_spec_w_label['mel'][0].shape)
print('length',len(mel_spec_w_label['mel']),len(mel_spec_w_label['labels']))

for i in range(len(mel_spec_w_label['mel'])):
    time=[]
    t = mel_spec_w_label['mel'][i].shape[1]
    time.append(t)

print('max length time:', max(time))
print('min length time:', min(time))

with open('D:/IUB/DL/Project/Data/ca 5000/'+lang+'_mel_2500.pkl', 'wb') as f:
  pickle.dump(mel_spec_w_label, f)

#Spectrograms of three features

#y, sr = librosa.load(dirpath+'000f968689b7d8d0770057693a59c2eb2b05a9f1e810372be32a4c0e4db72d1b692d178ee6d882cc3da069889aefeb2801d9d66408d04fe8f66e02de5ccfddd7.wav', offset=0.0, duration=5.0)
#
#mel = librosa.feature.melspectrogram(y=y, sr=sr)
#
#print(mel.shape)
#
##mel-freq
#S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
#import librosa.display
#import matplotlib.pyplot as plt
#plt.figure(figsize=(10, 4))
#librosa.display.specshow(librosa.power_to_db(S, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
#plt.colorbar(format='%+2.0f dB')
#plt.title('Mel spectrogram')
#plt.tight_layout()
#
##mfcc
#mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
#plt.figure(figsize=(10, 4))
#librosa.display.specshow(mfccs, x_axis='time')
#plt.colorbar()
#plt.title('MFCC')
#plt.tight_layout()
#
##stft
#D = np.abs(librosa.stft(y))
#import matplotlib.pyplot as plt
#plt.figure(figsize=(10, 4))
#librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
#plt.title('Power spectrogram')
#plt.colorbar(format='%+2.0f dB')
#plt.tight_layout()