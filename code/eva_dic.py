import pandas as pd 
import numpy as np 
import os, re 
import glob
import pathlib


p_dic = pathlib.Path('dic')

for i in p_dic.glob('*.txt'):
  with open (i, 'r', encoding='cp932') as f:
    df = [ii.replace('\n', '').split(':') for ii in f.readlines()]

evaluation_df = pd.DataFrame(df, columns=['word', 'read', 'speech', 'score'])
evaluation_df = evaluation_df[~evaluation_df[['word', 'read', 'speech']].duplicated()]

eva_df = pd.merge(df, evaluation_df, how='inner', on=['word', 'speech'])
eva_df['score'] = eva_df['score'].astype(float)

score_df = eva_df.groupby('id').mean().reset_index()