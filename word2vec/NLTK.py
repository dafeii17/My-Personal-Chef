#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:28:23 2018

@author: yinglirao
"""

import dill
import re
import os


top_words= dill.load(open('./processed/top_words.pkd', 'rb'))
vocab = [i for i in top_words if len(i.split())==1]

k_words = dill.load(open('./processed/k_single_wds.pkd', 'rb'))
add_words = [i for i in k_words if i not in vocab]

#2.26 version1 - discard 1st try
#2.13 version4- changed to version1 
#2.0 version2
#1.8 version3

from nltk.corpus import wordnet as wn

def clean(dict_):
    for key, val in dict_.items():
        new_w = [re.sub(r'_', ' ', word) for word in val]
        dict_.update({key: new_w})
    return dict_
    
def syn(vocab):
    vocab_syn_dict1 = {word:[] for word in vocab}
    vocab_syn_dict2 = {word:[] for word in vocab}
    i=0
    for net2 in wn.all_synsets():
        if i%1000==0:
            print('%d synset has been processed...'%i)
        names = [lemma.name() for lemma in net2.lemmas()]
        for word in vocab:
            try:
                for net1 in wn.synsets(word):
                    lch = net1.lch_similarity(net2)
                    if lch>=2.13:
                        vocab_syn_dict1[word].extend(names)
                    if lch>=2.20:
                        vocab_syn_dict2[word].extend(names)
            except:
                continue
        i+=1
        
    vocab_syn_dict1 = clean(vocab_syn_dict1)
    vocab_syn_dict2 = clean(vocab_syn_dict2)
    
    return vocab_syn_dict1, vocab_syn_dict2

res = syn(add_words)
vocab_syn_dict_add213 = res[0]
vocab_syn_dict_add220 = res[1]

dill.dump(vocab_syn_dict_add213, open('./processed/vocab_syn_dict_add213.pkd', 'wb'))
dill.dump(vocab_syn_dict_add220, open('./processed/vocab_syn_dict_add220.pkd', 'wb'))




