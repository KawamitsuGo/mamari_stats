from pathlib import Path
import glob
import os, re
import emoji, mojimoji
from posixpath import dirname
import neologdn
import MeCab

import numpy as np 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

# データの読み込み
df = pd.read_csv('hoge.csv')

t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

morpheme_df = pd.DataFrame(columns=['id', 'word', 'speech', 'speech_'])

for row, item in df.iterrows():
  result = ''
  result = t.parse(item.plain_text)
  lines = result.split("\n")
  lines = lines[0:-2]
  for words in lines:
    word = re.split('\t|,',words)
    if word[1] !='助動詞' and word[1] != '助詞':
      morpheme_df = morpheme_df.append({'id':item.id, 'word':word[0], 'speech':word[1], 'speech_':word[2]}, ignore_index=True)
    else:
      pass 
