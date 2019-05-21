{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\singh\\\\Box\\\\Deep Learning Project\\\\Scripts'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import librosa\n",
    "import numpy as np\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "train_df = pd.read_csv('C:\\\\Users\\\\singh\\\\Box\\\\Deep Learning Project\\\\Data\\\\trainingdata\\\\trainingData.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample Filename</th>\n",
       "      <th>Language</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>000kouqjfnk.mp3</td>\n",
       "      <td>Hmong Daw</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000w3fewuqj.mp3</td>\n",
       "      <td>Tektiteko</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000ylhu4sxl.mp3</td>\n",
       "      <td>Teribe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0014x3zvjrl.mp3</td>\n",
       "      <td>Chipaya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>001xjmtk2wx.mp3</td>\n",
       "      <td>KalmykOirat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sample Filename     Language\n",
       "0  000kouqjfnk.mp3    Hmong Daw\n",
       "1  000w3fewuqj.mp3    Tektiteko\n",
       "2  000ylhu4sxl.mp3       Teribe\n",
       "3  0014x3zvjrl.mp3      Chipaya\n",
       "4  001xjmtk2wx.mp3  KalmykOirat"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "languages = ['Hindi','Korean South','Bhojpuri']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "train_df_sub = train_df[train_df['Language'].isin(languages)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1128, 2)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample Filename</th>\n",
       "      <th>Language</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>00ywwvulzwa.mp3</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>01pd0w1exxo.mp3</td>\n",
       "      <td>Bhojpuri</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>01rjjbm5mtn.mp3</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>275</th>\n",
       "      <td>04ni1ngt11d.mp3</td>\n",
       "      <td>Bhojpuri</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>355</th>\n",
       "      <td>05uipha1itb.mp3</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Sample Filename  Language\n",
       "58   00ywwvulzwa.mp3     Hindi\n",
       "93   01pd0w1exxo.mp3  Bhojpuri\n",
       "96   01rjjbm5mtn.mp3     Hindi\n",
       "275  04ni1ngt11d.mp3  Bhojpuri\n",
       "355  05uipha1itb.mp3     Hindi"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(train_df_sub.shape)\n",
    "train_df_sub.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(195, 2)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_df_sub = train_df_sub.groupby('Language').head(65)\n",
    "train_df_sub.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sample Filename</th>\n",
       "      <th>Language</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>00ywwvulzwa.wav</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>01pd0w1exxo.wav</td>\n",
       "      <td>Bhojpuri</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>01rjjbm5mtn.wav</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>275</th>\n",
       "      <td>04ni1ngt11d.wav</td>\n",
       "      <td>Bhojpuri</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>355</th>\n",
       "      <td>05uipha1itb.wav</td>\n",
       "      <td>Hindi</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Sample Filename  Language\n",
       "58   00ywwvulzwa.wav     Hindi\n",
       "93   01pd0w1exxo.wav  Bhojpuri\n",
       "96   01rjjbm5mtn.wav     Hindi\n",
       "275  04ni1ngt11d.wav  Bhojpuri\n",
       "355  05uipha1itb.wav     Hindi"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_df_sub['Sample Filename'] = train_df_sub['Sample Filename'].str.replace('.mp3', '.wav')\n",
    "train_df_sub.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "directory = \"C:\\\\Users\\\\singh\\\\Box\\\\Deep Learning Project\\\\Data\\\\trainingdata\\\\hindi_korean_bhojpuri(wav)\\\\\"\n",
    "dirpath = \"C:\\\\Users\\\\singh\\\\Box\\\\Deep Learning Project\\\\Data\\\\trainingdata\\\\\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "def file_op(file):\n",
    "    #Loading train files\n",
    "\n",
    "    s,sr=librosa.load(file, sr=None)\n",
    "    S=librosa.stft(s, n_fft=1024, hop_length=512)\n",
    "\n",
    "    #Taking absolute of input and output of training file\n",
    "    S =  S.T\n",
    "    S_abs = np.abs(S)\n",
    "\n",
    "    #print(S_abs.shape)\n",
    "\n",
    "    return s, S, S_abs\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\00ywwvulzwa.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\01pd0w1exxo.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\01rjjbm5mtn.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\04ni1ngt11d.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\05uipha1itb.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0adiw4jd2vh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0brzbaynfio.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0bwbfbfxvr1.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0ec1nsncnvc.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0fleyjxbw1v.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0iapd2lck0h.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0jzzkllnyli.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0kajiv5vnlh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0kznowsn4ql.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0mw2tiuqjlf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0nffepjlfmp.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0ujcc5vsbnh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\0wmrtwefmwj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\11uekpvwm22.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\11ycidyh11g.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\121mmfyqbe5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\12fb5ikeyw3.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1311wyyqphh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\13afhgg50ub.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\13ddk3dm5oq.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\13oa4ebmzqj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\15tgxn4hlfh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\15wx0v40dzx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1alv0fra4vu.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1b3j0hx1zdr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1cm4vsulfew.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1fwa0bfo3vs.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1fwlmcgnphl.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1kdl2vnundp.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1lrc2bucups.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1mqlurofzcu.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1nc0wjirijz.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1oyr4dz52g0.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1pjtfhcpdg0.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1qncsun4yrl.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1sj05icgtjh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1skknmtzfh2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1smbn4j3qry.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1wifa3dsmpd.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1x0abi1c3tn.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1xxo2awjkb1.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1yyn1gkhmvf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\1yzw1435jld.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2110d4cxwug.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\21vg4zerfe5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\22zzsqa1wlc.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\23bkbsxcpgk.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\23hw2wbqume.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\23p4pdegqri.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\244elznv4cw.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\25cunnkzu0g.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\25ddeltl15h.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2a5y0dd4ns1.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2c4fwaqnclb.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2czq3regbma.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2d2x1krrc12.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2d33gnhklg5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2dpgzj4xxkr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2f0vht0taxz.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2flc0crdrum.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2gchuwhdgwx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2gk23agp2hp.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2gt53rgrw3d.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2i2ldczbbas.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2ijrmsw43m1.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2ju5wd5dumr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2k2lgwuhppf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2lmgrhwhjsu.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2lx2eyfi4do.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2lx5k3do3uv.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2msjr3tf3oz.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2msowsm0pbr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2q54l5qscyv.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2qw2zhf4bmj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2ro0pfyzucj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2sgpwo1rstm.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2taqiixnnjt.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2trrucsgbod.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2uv5yun0xj0.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2uykq4jfgki.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2vknz0hfmoa.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2wl2q1racvx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2x4tecw54un.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2y4j5w5yvgn.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2yabznqz1vo.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2zrgzwzzfid.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\2zyeu5y2qn4.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\303i0jxtcgj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\303tck3ujzp.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\30g1nwk5hxl.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\30kwtoyy3kh.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\30qj50uno3v.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\30wakqpg0ik.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\321dwezqtyp.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\32pesuxa1zk.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\32un2sjlose.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\333lh4wdskf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\33dv3fbkx3n.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3503wszdsxx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\35f20wnrbbj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\35xkqrhilyo.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3ci3abxd1fo.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3ctfpxcyws2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3cyixevccwg.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3emmoabevvf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3eq25qnjnw5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3fet3eip1g3.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3getwxbgulr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3hjn4cdm4m1.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3hkd0x21ls4.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3hzb05urel2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3j251v3yy3z.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3kwlqzty5nu.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3n4dvdgr2xl.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3ot1vbptfba.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3piuebekss2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3q51xcd3ebx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3rlyeyind0i.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3sfmaqwmjpn.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3sg3c3jgn1u.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3t4o2kxbuch.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3tc5otdvmf5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3vkq0ud3ox5.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3vpdesgl4f4.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3wfxswk2anj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3xuval2d5xf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3yphtsetzjy.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\3zlcjvovbqe.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\400meynwhej.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\40kpxyq04jx.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\41444cl2thw.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\44hhsusdcoj.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\44resubvuct.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\45mfabo2nhn.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4aplyhc11dr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4axhsvojxia.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4b41wqocpcy.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4c2iozudizb.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4cbidr2n3wg.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4eiqggoemxr.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4gnnswrym3f.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4hwzkdudxzc.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4j1ve5rugls.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4jdw2v3b2fy.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4jwuywy4xrc.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4jz2djsy2ah.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4khy25oflfi.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4kv3rtor552.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4ma2zcahd2c.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4mbjjv1pa1j.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4p5eviwcirv.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4po5vfu4nh2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4psd4yxutci.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4qj0htvj0ke.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4qm4ji4lvo2.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4re3uw2dst4.wav\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4ryxft1xeff.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4ryxvjo2pth.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4tyart0o2gd.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4yphyvq5d40.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4yqe3vu5sjf.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4zg0fyam2fs.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4zohwg05n5f.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\4ztlvj0qyqi.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\50opr5mjf24.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\513lskr23aa.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\51xuauuvnl4.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\51zh0ncsb15.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\52huplnatks.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\53hbzaux3t3.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\54bap1f30m0.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5bc4e01v4nt.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5blfwdv1q1e.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5c41esw0ct0.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5chliw2ksxi.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5ddxyj5kn2j.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5gsmw5f4l43.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5jqkpeea41j.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5kghm0bjkdl.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5mmfk5lgw0r.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5ns34yssa5w.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5ny1m0xc05b.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5qixiozlp43.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5sanv2lyu4r.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5tktnekdmgc.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5twwedyrcpq.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5ugtfrmac54.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5ulmx0z0h40.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5uv3cnuw0bd.wav\n",
      "C:\\Users\\singh\\Box\\Deep Learning Project\\Data\\trainingdata\\hindi_korean_bhojpuri(wav)\\5vfbugmcczp.wav\n"
     ]
    }
   ],
   "source": [
    "at_list = []\n",
    "spec_list = []\n",
    "spec_abs_list = []\n",
    "labels = []\n",
    "\n",
    "for i in range(train_df_sub.shape[0]):\n",
    "    file = directory+train_df_sub.iloc[i][0]\n",
    "    print(file)\n",
    "    \n",
    "    at, spec, spec_abs = file_op(file)\n",
    "    \n",
    "    at_list.append(at)\n",
    "    spec_list.append(spec)\n",
    "    spec_abs_list.append(spec_abs)\n",
    "    labels.append(train_df_sub.iloc[i][1])\n",
    "    \n",
    "    \n",
    "sound_lists = {'at_list':at_list,\n",
    "               'spec_list': spec_list,\n",
    "               'spec_abs_list': spec_abs_list,\n",
    "               'labels': labels\n",
    "              }\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Pickling the training data dictionary\n",
    "sound_lists_pkl = open(dirpath+\"train_sound_lists.pkl\",\"wb\")\n",
    "pickle.dump(sound_lists, sound_lists_pkl)\n",
    "sound_lists_pkl.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import shutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "# for i in range(train_df_sub.shape[0]):\n",
    "#     path = path = directory+train_df_sub.iloc[i][0]\n",
    "#     shutil.copy(path,'C:\\\\Users\\\\singh\\\\Box\\\\Deep Learning Project\\\\Data\\\\trainingdata\\\\hindi_korean_bhojpuri')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
