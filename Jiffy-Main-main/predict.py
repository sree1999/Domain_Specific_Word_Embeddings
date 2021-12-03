import gensim
import os

#function to check sample inputs to the model
path = os.getcwd() + '/models/'
#change the model name in the line below to 'word2vec.txt' to load the Word2Vec model
model = gensim.models.KeyedVectors.load_word2vec_format(path + 'glove.txt', binary = False)
ans = model.similarity('profit','gain')
print(ans)
a = model.most_similar(positive = ['company'],negative = ['expenditure'])[:2]
print(a)
