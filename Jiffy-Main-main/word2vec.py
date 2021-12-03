import pandas as pd
import numpy as np
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from gensim.models.phrases import Phrases, Phraser
import re
from collections import defaultdict
from time import time
import string
import multiprocessing
from gensim.models import Word2Vec
from clean import clean
from preprocess import preprocess
import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

#preprocess data
cwd = os.getcwd()
#place any files of any custom domain in a folder in the path given below to train them
path = cwd + '/dataset/'
data = preprocess(path)

phrases = Phrases(data, min_count = 30, progress_per = 10000)
bigram = Phraser(phrases)
sentences = bigram[data]

word_freq = defaultdict(int)
for sent in sentences:
	for i in sent:
		word_freq[i] += 1
print(len(word_freq))
print(sorted(word_freq, key = word_freq.get, reverse = True)[:50])
#define the model
cores = multiprocessing.cpu_count()
model = Word2Vec(min_count=5,
                     window=3,
                     size=300,
                     sample=6e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     workers=cores-1)
#train the model
t = time()
model.build_vocab(sentences, progress_per=10000)
print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))
model.train(sentences, total_examples=model.corpus_count, epochs=30, report_delay=1)
model.init_sims(replace=True)
model.wv.save_word2vec_format(cwd+'/models/word2vec.txt')	
