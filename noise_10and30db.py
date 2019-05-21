# -*- coding: utf-8 -*-
"""
Created on Wed May  1 03:26:20 2019

@author: skoth
"""

import os
audio = os.listdir("D:/IUB/DL/Project/Data/ca 5000/ca 5000 wav")
noise = os.listdir("D:/IUB/DL/Project/Data/Noise/Normal Volume")
from pydub import AudioSegment

for i in range(0,2500):
    print(i)
    sound1 = AudioSegment.from_file("D:/IUB/DL/Project/Data/ca 5000/ca 5000 wav/"+str(audio[i]))
    
    if (i<500):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Normal Volume/"+str(noise[0]))
    
    elif (i<1000):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Normal Volume/"+str(noise[1]))
    
    elif (i<1500):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Normal Volume/"+str(noise[2]))
    
    elif (i<2000):
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Normal Volume/"+str(noise[3]))
        
    else:
        sound2 = AudioSegment.from_file("D:/IUB/DL/Project/Data/Noise/Normal Volume/"+str(noise[4]))
    
    
    sound_10db = sound2-10
    sound_30db = sound2-30
    combined_10db = sound1.overlay(sound_10db)
    combined_30db = sound1.overlay(sound_30db)
    
    combined_10db.export("D:/IUB/DL/Project/Data/ca 5000/ca 2500 noise 10db/"+str(audio[i]), format='wav')
    combined_30db.export("D:/IUB/DL/Project/Data/ca 5000/ca 2500 noise 30db/"+str(audio[i]), format='wav')