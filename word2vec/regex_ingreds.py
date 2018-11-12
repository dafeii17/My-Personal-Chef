#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:05:02 2018

@author: yinglirao
"""
import re

def regex_keywords(i):
    adj_words = re.compile(r'small|large|fresh(ly)?|quality|unsalted|handfuls?|bunch|^thin(ly)?|chunks?|'
                           'salted|organic|soft(ened)?|hard|light(ly)?|dried\s|ground|chopped|diced|sliced?|'
                           'eating|heaped|plus\sextra\sfor.*|^an?\s|\san?\s|trimmed|shelled|'
                            'free.?range|medium|fast.?action|ripe|regular|low.?fat|to\sdust|'
                            'higher.?welfare|gluten.?free|optional|to\sserve|to\sgrating|hulled|'
                            'to\sgarnish|to\staste|\spart\s|a\sfew|ask\syour\sfishmonger|splash|'
                            'such\sas|½|fat.?free|natural|^shelled|^cored|^and\b|\salt|sea.?salt|'
                            'fine(ly)\s|left.?over|washed|unwaxed|from\ssustainable\ssources?|'
                            'firm\s|filling|plus\sextra|for\sgrating|\sraw\s|peeled|stems?\s|'
                            'juice\sof|for\sdusting|pieces?|few\s|sprigs?\s|cored\s|quartered|good|'
                            'leaves\spicked|reserve\sthem|spun\s?dry|zest\s(of)?|wild\s|bottles?|'
                            'chilled|big\s|small\s|¼|roughly|ideally|total|plus|ripped|both|grated|for\s|'
                            'fine(ly)?\s|half\s|each\s|frying\s|fat\sremoved|gutted|jointed|preferably|'
                            'thin(ly)?\s|thick\s|at\sroom\stemper.*|about|ones\s|cut\sinto|'
                            'very\s|.*possible|broken\sup|beaten|\sand|skin\son|and\sdrained|skinless|'
                            'skinned|pinnboned|stone\sin|stoned|to\sserve|to\sdecorate|wild|your\schild.*|'
                            '.*removed|with\b|optional|minced|mixed|to\sserve|skin\soff.*|'
                            'shell\son|scale.*|if\sneeded|made\susing|baby\s|\setc')
                            
    quant_words1 = re.compile(r'[^a-zA-Z]+tablespoons?|[^a-zA-Z]+teaspoons?|[^a-zA-Z]+cups?')
    quant_words2 = re.compile(r'[^a-zA-Z]+kg\s|[^a-zA-Z]+g\s|[^a-zA-Z]+mls?\s|[^a-zA-Z]+pieces?|'
                              '[^a-zA-Z]+l\s|[^a-zA-Z]+litres?\s|[^a-zA-Z]+cm\s|'
                              '[^a-zA-Z]+tbsp\s|[^a-zA-Z]+tsp\s|\d+\s?x\s?\d+|[^a-zA-Z]+oz\s')
    note_words = re.compile(r'\([\w\s]+\)|for\sthe\s.+') #remove things in (): (see tip)/(see reference)
    special_char = re.compile(r'[^\w\s]') #remove all special characters, (, ), etc
    
    
    RE_clean = re.compile(r'^for\s.*|^into|^cubed|^pinch|^melted|^frying|deseeded|skinless|'
                          '^each|^thick|^thin(ly)?|^kg|^on\sthe.*|^to\s.*|^boned|boneless|^bone\s?in|'
                          '^red\b|^halved|^extra\b|^wedge|scrub(bed)?|^green\b|^from.*|^to\b|^ly\b|^strip\b'
                          'torn\sinto|^x\s|level\s|^lug\s|^mug\s|herby\stop\s|reserved|\stop\b|'
                          'cooked|shell\s\on\sking\s|dab[^\w]|wineglass\s|glass|live\s+|^g\s+|tesapoon|'
                          '\sclove|clove\s|stick\s|\sstick|tablepsoon|\stop|fillet|new\s|runny\s|^un\s|'
                          'head\s|jar\s|\sjar|^cut\s|colourful|curly\s|\smash|shredded|grating|^red\s|tablspoon|'
                          'split\s|^tin\s|tinned\s|\skg|\sin\s.+|classic|colour|'
                          'skinny|homemade|frozen|really|sized|roast|cold\s|^ed\s|'
                          'round\s|then\s|^d\s|instant|mature\s|extra\s|whole\s|^on\s|'
                          'devein(ed)?|uncook|jumbo|peel\s|^gold\s|^y\s|\sed\s|\sthread|'
                          'lite\s|at\sleast\smeat'
                          )
    
    i = re.sub(r'.*\sof\s', '', i) #get rid of a tin of sth, pinch of sth
    i = adj_words.sub('', i)  #remove stop-words 'fresh', 'unsalted'
    i = quant_words1.sub('', i)  #remove cup, tablespoon, teaspoon
    i = quant_words2.sub('', i)
    i = note_words.sub('', i)  #remove things in (), example-(see tip)
    i = re.sub(r'\d+', '', i)  #remove numbers
    i = special_char.sub(' ', i).strip() #remove all left special chars
    i = re.sub(r'\s+', ' ', i.lower().strip()) #remove extra space     final = [re.sub(r'ss\b', '__s__', i) for i in final]
    i = re.sub(r'ss\b', '__s__', i) #substitute ss with __s__
    i = re.sub(r'cos', '__co__', i)
    i = re.sub(r'oes\b', '__a__', i)
    i = re.sub(r'ches\b', '__c__', i)
    i = re.sub(r'leaves\b', '__v__', i)
    i = re.sub(r'chillies', '__llie__', i) 
    i = re.sub(r'parnsip', 'parsnip', i) 
    i = re.sub(r'steaksthick', 'steak', i) 
    i = re.sub(r'cheeseping', 'cheese', i) 
    i = re.sub(r'reduced\sfat', '', i) 
    i = re.sub(r'ooil', 'oil', i) 
    i = re.sub(r'swiss\sc', 'swiss cheese', i)
    i = re.sub(r'yoghurt', 'yogurt', i)
    i = re.sub(r'sun\s', 'sun dried ', i)
    i = re.sub(r'carott', 'carrot ', i)
    i = re.sub(r'^lean\s', '', i)

    i = re.sub(r'ras\b', '__ras__', i) 
    
    i = re.sub(r'ies\b', '__y__', i) 
    i = re.sub(r'us\b', '__u__', i) 
    
    i = re.sub(r's\b', '', i)  #remove final s
    i = re.sub(r'__ras__', 'ras', i) 
    i = re.sub(r'__co__', 'cos', i)
    i = re.sub(r'__a__', 'o', i) 
    i = re.sub(r'__s__', 'ss', i) 
    i = re.sub(r'__llie__', 'chilli', i) 
    i = re.sub(r'__v__', 'leaf', i) 
    i = re.sub(r'__c__', 'ch', i) 
    
    i = re.sub(r'__y__', 'y', i) 
    i = re.sub(r'__u__', 'us', i) 
    
    i = re.sub(r'^c\b', '', i) 
    i = re.sub(r'^other', '', i) 
    i = re.sub(r'\s+', ' ', i.lower().strip()) 
    i = RE_clean.sub('', i)  #remove for the final extra ones
    i = re.sub(r'\s+', ' ', i.lower().strip())  #remove extra space 
    
    i = RE_clean.sub('', i)  #remove for the final extra ones
    i = re.sub(r'\s+', ' ', i.lower().strip())  #remove extra space 
    
    return i

junks = ['and', 'un', 'ly', 'g', 'in', 'shredded', 'stock', 'one', 'cored',
         'stalk reserved', 'torn into', 'in', 'topping', 'seeded', 'sifted',
         'tinned', 'dried', 'de', 'strip', 'quarter', 'deep frying', 'cube', 'bay',
         'seed', 'level', 'shell on', 'tipo', 'drained weight', 'torn up',
         'cut in half', 'podded', 'cooked','stuffing', 'peel',
         'brazil', 'cold', 'frozen', 'glaze','broken into clove', 'made with egg',
         'brown', 'kidney', 'mixture', 'hot', 'bulb', 'ro attached',
         'i got mine from the butcher with the bone in', 'rub', 'in one',
         'deveined','golden', 'optional', 'green', 'little extra', 'debearded',
         'drained', 'pin boned', 'stalk', 'spun dry', 'block', 'defrosted', 'co',
         'pinboned', 'paste', 'bashed', 'leaf reserved', 'white', 'pinboned cut in half',
         'm vegetable stock', 'fat', 'dripping', 'drizzling', 'cutthick', 
         'sustainably sourced', 'lengthway seed scraped out','topped tailed', 
         'leafy top reserved', 'rinsed', 'knife', 'yolk', 'e rocket',
         'but either way i fine', 'if you can get them', 'red yellow',
         'belly on', 'squashed', 'left whole', 'coarsely', 'stale', 'the flowering kind',
         'roll', 'cleaned', 'atangle', 'long', 'zested halved', 'if', 'soaked drained',
         'variety', 'stin', 'approximately g', 'boiled', 'rocket', 'torn', 'black',
         'red', 'filling', 'extra', 'equal sized','drained rinsed', 'dip', 'only', 
         'not the pickled one', 'neck end','separated' ,'king edward', 'coral attached',
         'crushed', 'french', 'skewer', 'lengthway', 'r halved', 'cleaned sincriss cross fashion',
         'cox', 'whole', 'bone out', 'ooil', 'toasted', 'you will need', 'yellow',
         'with leaf', 'leafy reserved', 'ed p', 't', 'yellow green', 'jarred',
         'snipped', 'clean', 'ed', 'equal', 'broken into', 'linked together',
         'shell', 'well', 'y', 'twist', 'bow', 'feet', 'bone', 'up', 'char',
         'mi', 'peel devein', 'veg', 'in half', 'pinboned cut', 'chop', 'water',
         'casing', 'squirt', 'non spray', 'thawed squeezed dry', 'round', 'rin drain',
         'wafer', 'msg'
         ]

def extract_keywords(ingredients):
    final = []
    for i in ingredients:
        i = re.sub(r'[^\w]or\s', ',', i).strip()
        final.extend(i.split(','))
    final = [regex_keywords(i) for i in final]
    final = list(filter(lambda x: len(x)!=0 and x not in junks, set(final)))
    return final
