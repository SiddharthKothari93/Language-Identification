# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:21:00 2019

@author: skoth
"""

import os
audio = os.listdir("D:/IUB/DL/Project/Data/it 5000 wave/it 5000 wave")
noise = os.listdir("D:/IUB/DL/Project/Data/Noise/Volume_reduced")
from pydub import AudioSegment

for i in range(0,2500):
    print(i)
    sound1 = AudioSegment.from_file("D:/IUB/DL/Project/Data/it 5000 wave/it 5000 wave/"+str(audio[i]))
    
    if (i<500):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Volume_reduced/"+str(noise[0]))
    
    elif (i<1000):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Volume_reduced/"+str(noise[1]))
    
    elif (i<1500):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Volume_reduced/"+str(noise[2]))
    
    elif (i<2000):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Volume_reduced/"+str(noise[3]))
        
    else:
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Volume_reduced/"+str(noise[4]))
    
    
    spound2 = sound2-15
    combined = sound1.overlay(sound2)
    
    combined.export("D:/IUB/DL/Project/Data/it 5000 wave/it 2500 noise/"+str(audio[i]), format='wav')


