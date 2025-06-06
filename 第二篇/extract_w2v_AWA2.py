#  从predicates中的85个属性以及output_all_no_original_prompt_20中的334个属性提取得到419*300的词向量
#  output_all_no_original_prompt_20中的334*50的att与原始的85*50的att拼接得到419*50的att
import os,sys
pwd = os.getcwd()
sys.path.insert(0,pwd)
#%%
print('-'*30)
print(os.getcwd())
print('-'*30)
#%%
import pdb
import pandas as pd
import numpy as np
import gensim.downloader as api
import scipy.io as sio
import pickle
#%%
print('Loading pretrain w2v model')
model_name = 'word2vec-google-news-300'#best model
model = api.load(model_name)
dim_w2v = 300
print('Done loading model')
#%%
replace_word = [('newworld','new world'),('oldworld','old world'),('nestspot','nest spot'),('toughskin','tough skin'),
                ('longleg','long leg'),('chewteeth','chew teeth'),('meatteeth','meat teeth'),('strainteeth','strain teeth'),
                ('quadrapedal','quadrupedal')]
dataset = 'AWA2'
#%%
path = './predicates.txt'
df=pd.read_csv(path,sep='\t',header = None, names = ['idx','des'])
des = df['des'].values

for pair in replace_word:
    for idx,s in enumerate(des):
        des[idx]=s.replace(pair[0],pair[1])
print('Done replace OOD words')
#%%
# df['new_des']=des
# df.to_csv('./attribute/{}/new_des.csv'.format(dataset))
#%%

counter_err = 0
all_w2v = []
for s in des:
    # print(s)
    words = s.split(' ')
    if words[-1] == '':     #remove empty element
        words = words[:-1]
    w2v = np.zeros(dim_w2v)
    for w in words:
        try:
            w2v += model[w]
        except Exception as e:
            print(e)
            counter_err += 1
    all_w2v.append(w2v[np.newaxis,:])
print('counter_err ',counter_err)

path1 = './output_all_no_original_prompt_5.csv'
df1 = pd.read_csv(path1)#自动去掉第一行了
first_column = df1.iloc[:,0]
# print(first_column)
for value in first_column:
    w2v = np.zeros(dim_w2v)
    if " " in value:
        words = value.split(" ")
        for w in words:
            if w not in model:
                continue
            else:
                w2v += model[w]
    elif "-" in value:
        words = value.split('-')
        for w in words:
            if w not in model:
                continue
            else:
                w2v += model[w]
    elif value not in model:
        w2v += np.zeros(dim_w2v)
    else:
        w2v += model[value]
    all_w2v.append(w2v[np.newaxis,:])
    # print("循环内的：",len(all_w2v))

all_w2v=np.concatenate(all_w2v,axis=0)
print(all_w2v.shape)

with open('./w2v/{}_attribute_5.pkl'.format(dataset),'wb') as f:
    pickle.dump(all_w2v,f)


