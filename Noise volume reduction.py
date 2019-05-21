# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:07:35 2019

@author: skoth
"""

from pydub import AudioSegment

song = AudioSegment.from_wav("D:/IUB/DL/Project/Data/Noise/eatingchips_10s.wav")

# reduce volume by 10 dB
song = song - 14

# but let's make him *very* quiet
#song = song - 36

# save the output
song.export("D:/IUB/DL/Project/Data/Noise/Volume_reduced/eatingchips_10s_reducedvol.wav", "wav")