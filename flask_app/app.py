#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:12:28 2018

@author: yinglirao
"""

from flask import (Flask, render_template, request)
import recipes_get as rp
import glove_app as glove

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')

@app.route('/expedition')
def expedition():
	return render_template('expedition.html')

@app.route('/food-analogy-game')
def food_analogy():
	return render_template('food_analogy.html')

@app.route('/magic-explained')
def magic():
	return render_template('magic.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/recipes', methods=('GET', 'POST'))
def get_recipes():
    ingredients = request.form['ingredients']
    ingredients2 = ingredients.split(',')
    if ingredients2[0] == ingredients:
        ingredients2 = ingredients.split()
    ingredients = [i.strip().lower() for i in ingredients2]
    titles, ingreds, img_links, links = rp.get_recipes(ingredients)
    notes = ''
    if len(titles)==0:
        notes = 'Sorry currently we do not have any recipes match your ingredients'
    return render_template("recipes.html", recipe_result = zip(titles, ingreds, img_links, links),
                           notes = notes)   

@app.route('/similar', methods=('GET', 'POST'))
def similar():
    similar = request.form['similar'].lower()
    contents1 =[0]*2
    contents1[0] = 'Suggested substitutes for %s:'%similar
    contents1[1] = glove.get_similar(similar)[0]
    notes = ''
    if len(contents1[1]) == 0:
        notes = 'Sorry currenlty we do not have substitutes for %s.'%similar
    return render_template("similar.html", contents1=contents1, notes=notes)

@app.route('/match', methods=('GET', 'POST'))
def match():
    match = request.form['match'].lower()
    contents2 =[0]*2
    contents2[0] = 'Suggested goodies go well with %s:'%match
    contents2[1] = glove.get_similar(match)[1]
    notes = ''
    if len(contents2[1]) == 0:
        notes = 'Sorry currenlty we do not have suggested goodies go well with %s.'%match
    return render_template("match.html", contents2=contents2, notes=notes)

@app.route('/game', methods=('GET', 'POST'))
def game():    
    food1 = request.form['food3'].lower()
    food2 = request.form['food2'].lower()
    food3 = request.form['food1'].lower()
    foods = glove.food_analogies(food1, food2, food3)
    q3 = '\'%s\' stands to \'%s\' as \'%s\' stands to:'%(food3, food2, food1)
    food_names = [food1, food2, food3]
    notes = ''
    if len(foods) == 0:
        notes = 'Sorry currenlty we do not have answers for this.'
    return render_template("game.html", q3=q3, food_names = food_names, foods=foods, notes=notes)

if __name__ == '__main__':
  app.run(port=33507)


