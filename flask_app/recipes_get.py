#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:31:22 2018

@author: yinglirao
"""
import dill
from collections import Counter

idx_table = dill.load(open('./models/idx_table.pkd', 'rb')) #dictionary type

recipes = dill.load(open('./models/recipes_full_repeat_removed.pkd', 'rb'))

def recipe_idx_retrive(userlist):
    res = []
    for ingred in userlist:
        try:
            recipe_idx = list(idx_table[ingred])
            res.extend(recipe_idx)
        except:
            continue
    res = sorted(Counter(res).items(), key=lambda x: x[1], reverse=True)
    #top_res = [i[0] for i in res[:5]]
    idxs = [i[0] for i in res[:5]]
    return idxs

def get_recipes(userlist):
    idxs = recipe_idx_retrive(userlist)
    
    recipe_names = [recipes[idx][0] for idx in idxs]
    recipe_ingreds = [recipes[idx][1] for idx in idxs]
    #recipe_steps = [recipes[idx][2] for idx in idxs]
    img_links = [recipes[idx][3] for idx in idxs]
    recipe_links = ['https://www.jamieoliver.com'+recipes[idx][4] for idx in idxs]
    return recipe_names, recipe_ingreds, img_links, recipe_links
    




