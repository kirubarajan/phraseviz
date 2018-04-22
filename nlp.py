import math
import re
import numpy as np
from nltk.corpus import stopwords
from scipy.spatial import distance
from gensim.models import Word2Vec

# Removes stopwords from string and tokenizes string
def tokenize(string):
  text = re.sub("[^a-zA-Z]", " ", string)
  tokens = text.lower().split()
  english_stop_words = set(stopwords.words("english"))
  tokens = [token for token in tokens if not token in english_stop_words]
  return tokens

# Splits text into vectorize-able sentences
def get_sentences(string):
  sentences = [tokenize(sentence) for sentence in string.split(".")]
  return sentences

# Generates and trains word2vec model
def get_model(data):
  sentences = get_sentences(data)
  model = Word2Vec(sentences, min_count=1)
  return model

def average_vector(vectors):
  return sum(vectors) / len(vectors)

def scaled_sigmoid(n):
  return 1 / (1 + math.exp(-n))

def similarity(string1, string2):
  with open('corpus.txt', 'r') as f:
    data = f.read().replace('\n', '')
  model = get_model(data)

  string1_token_embeddings = [model.wv(token) for token in tokenize(string1)]
  string2_token_embeddings = [model.wv(token) for token in tokenize(string1)]

  string1_embedding = average_vector(string1_token_embeddings)
  string2_embedding = average_vector(string2_token_embeddings)

  return scaled_sigmoid(distance.cosine(string1_embedding, string2_embedding))