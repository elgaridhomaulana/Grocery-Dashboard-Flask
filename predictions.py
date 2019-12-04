import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

from data import pipe

words_not_good_great = ["not good", 
"not so good", 
"not a good", 
"not that good",
"not as good as",
"no good",
"not very good",
"doesn't taste good",
"not taste good",
"not nearly as good as",
"isn't good",
"aren't good",
"not great", 
"not so great", 
"not a great", 
"not that great",
"not as great as",
"no great",
"not very great",
"doesn't taste great",
"not taste great",
"not nearly as great as",
"isn't great",
"aren't great"]

flavor_words = ['no flavor',
'weird flavor',
'flavorless',
'strange flavor',
'lack flavor',
'lacking in flavor',
'not much flavor',
'weak flavor',
'odd flavor']

taste_words = ["doesn't taste",
"does not taste",
"no taste",
'tasteless']

like_words = [
    "didn't like",
    'not like',
    "don't like"
]

def predictions(text):
    stopwords_normal = stopwords.words('english')
    
    # change
    text = text.lower()
    for word in words_not_good_great:
        text = text.replace(word, 'bad')
    for word in flavor_words:
        text = text.replace(word, 'flavor_problem')
    for word in taste_words:
        text = text.replace(word, 'taste_problem')
    for word in like_words:
        text = text.replace(word, 'hate')
    text = text.replace('?', 'questionmark', 1)
    
    # clean
    text = re.sub('[^a-zA-Z]', ' ', text)
    list_text = word_tokenize(text)
    text_without_stopwords = [word for word in list_text if word not in stopwords_normal]
    text_clean  = ' '.join(text_without_stopwords)

    return pipe.predict([text_clean]), pipe.predict_proba([text_clean])
