#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:39:37 2018

@author: yinglirao
"""

import dill
from gensim.models import Word2Vec
import os
import itertools
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pylab as plt

os.chdir('/Users/yinglirao/Desktop/food projects/JamieOliver/')


def load_data():
    data1 = dill.load(open('./processed/clean_ingreds_table.pkd', 'rb'))
    data2 = dill.load(open('./processed/kaggle_ingreds_table.pkd', 'rb'))
    return data1+data2

def two_combo(data):
    data_two=[]
    for line in data:
        data_two.extend(list(itertools.combinations(line, 2)))
    return data_two

def ten_combo_len(data):
    length=[len(line) for line in data]
    mean_len=sum(length)/len(length)
    return mean_len

def word2vec_win(data, window=None):
    model = Word2Vec(data, window=window, min_count=1, sg=1) 
    # Training algorithm: sg=1 for skip-gram; otherwise CBOW
    model.save('./processed/kj_new_model_sg1_win_{}.bin'.format(int(window)))
    return model

def plot(result=None, figname=None, datapoints=None, annotate=False, model=None):
    plt.figure(figsize=(12,8), dpi=300)
    plt.scatter(result[:datapoints, 0], result[:datapoints, 1])
    if annotate==True:
        words=list(model.wv.vocab)[:datapoints]
        for i, word in enumerate(words):
            if i%5==0:
                plt.annotate(word, xy=(result[i,0], result[i,1]), fontsize=10)
    plt.savefig('./results/{}.png'.format(figname))
        
def pca_fit(X):
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    return result

def TSNE_fit(X):
    X1 = PCA(n_components=30).fit_transform(X)
    result = TSNE(n_components=2).fit_transform(X1)
    return result

def main():
    data = load_data() #3212 records of ingreds for all recipes
    data_two = two_combo(data)
    model = word2vec_win(data_two, window=2) #mean lenght of ingredients is 10

if __name__ == '__main__':
    main()
    
#model_j = Word2Vec.load('./processed/model_sg1_win_2.bin')
#model_k = Word2Vec.load('./processed/kaggle_model_sg1_win_2.bin')

#print(model)

#X = model.wv[model.wv.vocab]  #vector representation of all words
#result = TSNE_fit(X)
#plot(result = result, figname ='win2_sg1', datapoints=300, annotate=True, model=model)


# model.wv.most_similar_cosmul('beef', topn=10) #find most similar
#examples: sugar; beef; 
    
    
    