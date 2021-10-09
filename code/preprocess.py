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


from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('hoge.csv')

# 絵文字の削除
def remove_emoji(text):
    return ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)

df['plain_text'] = df['content'].map(remove_emoji)


# 文章の正規化
def normalize_text(text):
    text_ = neologdn.normalize(text)
    return text_

df['plain_text'] = df['plain_text'].map(normalize_text)


# URLの除去
def remove_text(text):
    text_ = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
    return text_

df['plain_text'] = df['plain_text'].map(remove_text)


# 数字の除去
def remove_digit(text):
    tmp = re.sub(r'(\d)([,.])(\d+)', r'\1\3', text)
    text_ = re.sub(r'\d+', '0', tmp)
    return text_

df['plain_text'] = df['plain_text'].map(remove_digit)


def remove_symbol(text):
# 半角記号の置換
    tmp = re.sub(r'[!-/:-@[-`{-~]', r' ', text)
    text_ = re.sub(u'[■-♯]', ' ', tmp)
    return text_

df['plain_text'] = df['plain_text'].map(remove_symbol)
