import nltk
import string
import re

def remove_punct(text):
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

def remove_stopwords(tokenized_list):
    stopword = nltk.corpus.stopwords.words('english')
    text = [word for word in tokenized_list if word not in stopword]
    return text

def lemmatizing(tokenized_text):
    wn = nltk.WordNetLemmatizer() #you'll need to download wordnet from nltk
    text = [wn.lemmatize(word) for word in tokenized_text]
    return text

def lemmatize(file):
'''
takes a text file, strips it of punctuation, then tokenizes the data.
After tokenization, the stop words are removed.
Then the lemmas of each word is found and returned as a list.
'''
    rawData = open(file).read()
    cleanData = remove_punct(rawData)
    tokenized = tokenize(cleanData.lower())
    text_no_stop = remove_stopwords(tokenized)
    return lemmatizing(text_no_stop)