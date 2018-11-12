#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:19:26 2018

@author: yinglirao
"""

import dill
import regex_ingreds as rg
import pandas as pd
import numpy as np
import re
from collections import Counter

'''
#remove recipes with repeats
recipes_full = dill.load(open('./processed/recipes_full.pkd', 'rb'))
recipe_names={}
recipes_new = []
for i in recipes_full:
    if i[0] in recipe_names:
        continue
    else:
        recipe_names[i[0]] = 1
        recipes_new.append(i)
dill.dump(recipes_new, open('./processed/recipes_full_repeat_removed.pkd', 'wb'))
'''


def get_keywords():
    recipes = dill.load(open('./processed/recipes_full', 'rb'))
    recipe_keywords = []
    for recipe in recipes:
        recipe_keywords.append((recipe[0], rg.extract_keywords(recipe[1])))
    return recipe_keywords

recipe_keywords = get_keywords() #(recipe_name, regex_ingreds)
ingreds_keywords = [i[1] for i in recipe_keywords] #(regex_ingreds)

raw_vocab = []
raw_vocab = [word for ingreds in recipe_keywords for word in ingreds[1]]

vocab_counts = Counter(raw_vocab)
sorted_vocab = sorted(vocab_counts.items(), key=lambda x: x[1], reverse=True)#get top words

top_words = [i[0] for i in sorted_vocab[:970]]

top_words = dill.load(open('./processed/top_words.pkd', 'rb'))
recipes_full = dill.load(open('./processed/recipes_full_repeat_removed.pkd', 'rb'))
index_table = {key: set() for key in top_words}
for word in top_words:
    for idx in range(len(recipes_full)): #(recipe_name, orign_ingreds) 2092 records
        for ingred in recipes_full[idx][1]:
            if word in ingred:
                index_table[word].add(idx)
                
'''
clean_ingreds_table format: 
    
'''    

clean_ingreds_table = []
for ingreds in ingreds_keywords: #(regex_ingreds)
    clean = set()
    for ingred in ingreds: 
        if ingred in top_words:
            clean.add(ingred)
    clean_ingreds_table.append(clean)

dill.dump(top_words, open('./processed/top_words.pkd', 'wb'))
dill.dump(index_table, open('./processed/idx_table.pkd', 'wb'))
dill.dump(clean_ingreds_table, open('./processed/clean_ingreds_table.pkd', 'wb'))








