import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from clean import lemmatize_sentence
from gensim.models import KeyedVectors


path = os.getcwd()+'/models/'
model1 = KeyedVectors.load_word2vec_format(path + 'word2vec.txt', binary = False)
model2 = KeyedVectors.load_word2vec_format(path + 'glove.txt', binary = False)
q = [['cash','money'],['profit','gain'],['global','international'],['house','home'],['agreement','contract'],['employee','employer'],['firm','company'],['income','tax'],['inventory','stock']]
w2v = []
glove =[]
x=[]
for words in q:
	
	words = lemmatize_sentence(words)
	word1,word2 = words[0],words[1]
	x.append(word1 + ',' + word2)
	a = model1.similarity(word1,word2)
	b = model2.similarity(word1,word2)
	w2v.append(a)
	glove.append(b)

bar_width = 0.4
m_xpos = [i for i, _ in enumerate(x)]
f_xpos = [val + bar_width for val in m_xpos]
plt.xlabel('Words')
plt.ylabel('Similarity')
plt.title('Word2Vec vs GloVe')
tick_pos = [val + bar_width / 2 for val in m_xpos]
plt.xticks(tick_pos, x,rotation = 90)
plt.bar(m_xpos, w2v, label='Word2Vec', width=bar_width, color='#3949abff')
plt.bar(f_xpos, glove, label='GloVe', width=bar_width, color='#d23369ff')
plt.gcf().subplots_adjust(bottom=0.3)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.show()