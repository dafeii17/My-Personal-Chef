#My Personal Chef#
####When we cook at home following recipes, it often occurred to us that we may not have all the ingredients required by one recipe. On the other hand, we may have some ingredients at home, for example lamb, or tofu, and we want to try some interesting ingredients which go well with the ingredients we have. 
####My-Personal-Chef is a platform which gives users suggestions for ingredients substitutes or complementing ingredients. The platform also features a food word analogy game. Here are few examples: apple stands to pear as fish stands to clam; beef stands to bay leaf as banana stands to rum, or toasted coconut.
###It is developed with Python, BeautifulSoup, natural language processing, Flask, HTML/CSS, and deployed on Heroku.
[Web App URL](https://my-personal-chef.herokuapp.com)
##How It Works
###Data Extraction & Processing
####The recipe collections on this platform were scrapped from celebrity chef [Jamie Oliver’s website](https://www.jamieoliver.com). The ingredients list for each recipe are parsed to remove special characters, quantity and quality descriptions, numbers, and then split into individual keywords. 
###Word2Vec Model
####The word2vec model data is based on over 50,000 recipes with ingredient lists from various cuisines. About 49,000 recipes with ingredient lists are from [Kaggle dataset](https://www.kaggle.com/c/whats-cooking). The rest 2500 recipes are scrapped from Jamie Oliver’s website.
The word2vec model is trained with gensim API. For the ingredients list for one recipe, the sequence of ingredients is not as important as in a regular sentence. As the average recipe ingredients list length is about 10, the word2vec model is trained with window size of 10 with either CBOW(bag-of-words) model or skip-gram model. Alternatively, the ingredients list for one recipe is expanded into multiple training samples with ingredients length of two per sample. The expanded training samples cover all possible length two combination of the original ingredient list. The word2vec model is then trained with window size of 2.
The word2vec model transformed the ingredients in vector space, in such a way that complementing and similar ingredients share similar coordinates. To separate complementing ingredients from similar ingredients, the ingredients are re-ranked according to their semantic distances using NLTK wordnet API. 
###Food Analogy Game
The most famous word2vec arithmetic example is: king – man + woman = queen. This demonstrates that the vector distance between king and queen is similar to the distance between man and woman. After transforming food ingredients into vector space, we can illustrate the relationship between ingredients. For instance, if apple is similar to pear, what is similar to fish? We can add the vector distance between apple and pear onto fish, then we obtained clam, tentacles. 
###Cooking Recipe Retrieval
Users can type the available ingredients into the search bar, then the platform will return recipes which maximize the coexistence of those ingredients. For now, the home tab (recipe search) only returns recipes collected from Jamie Oliver’s website. Ongoing work is building a content filtering based recommendation system to suggest users cooking recipes. The recipe features include main ingredients, chef style, cuisine types, occasions. The content filtering recommendation will maximize the similarities between recipe features and user profile.



