#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:26:50 2018

@author: yinglirao
"""

from bs4 import BeautifulSoup
import requests
import os
import dill
import time 
from random import randint

def get_cuisine_type(country):
    response = requests.get('https://www.jamieoliver.com/recipes/category/world/%s/'%country)
    soup = BeautifulSoup(response.text, 'lxml')
    recipe_names = soup.select('div.recipe-title')
    categories = {name.text: country for name in recipe_names}
    return categories

def get_links():
    response = requests.get('https://www.jamieoliver.com/recipes/fish-recipes')
    soup = BeautifulSoup(response.text, 'lxml')
    recipe_links = [link.a['href'] for link in soup.select('div.recipe-block')]
    dill.dump(recipe_links, open('./recipe_links/fish-recipes_links.pkd', 'wb'))
    return recipe_links

def recipe_download(links, category):
    if not os.path.isdir('./raw/%s'%category): 
        os.mkdir('./raw/%s'%category)
        
    pages = {}
    for i in range(len(links)):
        if (i+1)%13 ==0:
            dill.dump(pages, open('./raw/%s/%s_%d.pkd'%(category,category,i), 'wb'))
            pages = {}
            sleep_time = randint(200, 600)
            print('downloading up to {}'.format(i))
            print('I am sleeping %d seconds'%sleep_time)
            time.sleep(sleep_time)

        pages[links[i]] = requests.get('https://www.jamieoliver.com{}'.format(links[i]))
        
    dill.dump(pages, open('./raw/%s/%s_final.pkd'%(category,category), 'wb'))
    return None

def main():
#    recipe_cuisine = {}
#    categories = ['mexican', 'british', 'italian', 'moroccan',
#                  'indian', 'greek', 'american', 'asian', 'spanish', 
#                  'chinese', 'peruvian', 'french']
#    for category in categories:
 #       recipe_cuisine.update(get_cuisine_type(category))
    #links = get_links()
    links = dill.load(open('./recipe_links/fish-recipes_links.pkd', 'rb'))
    recipe_download(links, 'fish-recipes')
    
    
if __name__ == '__main__':
    main()
    
