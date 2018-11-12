#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:26:15 2018

@author: yinglirao
"""

import dill

from gensim.models import Word2Vec

model_j = Word2Vec.load('./models/model_sg1_win_2.bin')
model_k = Word2Vec.load('./models/kj_new_model_sg1_win_2.bin')
vocab_syn_dict = dill.load(open('./models/vocab_syn_dict_all213.pkd', 'rb'))

def get_syn(food):
    syn = []
    foods = food.split()
    for f in foods:
        try:
            syn.extend(vocab_syn_dict[f])
        except:
            continue
    return syn

def kaggle_words(food):
    try:
        return {i[0]: i[1] for i in model_k.wv.most_similar_cosmul(food, topn=15)}
    except:
        return {}

def jamie_words(food):
    try:
        return {i[0]: i[1] for i in model_j.wv.most_similar_cosmul(food, topn=15)}
    except:
        return {}

def get_similar(food):
    res = []
    cool = [] 
    similars = {}
    similars.update(kaggle_words(food))  
    try:
        similars.update(jamie_words(food))
    except:
        similars = similars
    similars = [i[0] for i in sorted(similars.items(), key=lambda x: x[1], reverse=True)]
    syn = get_syn(food)
    
    for item in similars:
        foodie = item.split()
        state = False
        for d in foodie:
            if d in syn:
                state=True
                break
        if state:
            res.append(item)
        else:
            cool.append(item)
        state = False
    return res[:10], cool[:10]

def food_analogies(food1, food2, food3):
    res = []
    try:
        ans = [i[0] for i in model_k.wv.most_similar_cosmul(positive=[food1, food2], 
                                         negative=[food3], topn=10)]   
        ans = sorted(ans, reverse=True)
    except:
        ans = []
    try:
        syn = get_syn(food1)
    except:
        syn = []
    for item in ans:
        foodie = item.split()
        state = False
        for d in foodie:
            if d in syn:
                state=True
                break
        if not state:
            res.append(item)
    return res[:3]
    
    
    
    


    