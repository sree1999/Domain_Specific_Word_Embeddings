import csv
from gensim.models import KeyedVectors
from clean import lemmatize_sentence
import os

path = os.getcwd()+'/models/'
model1 = KeyedVectors.load_word2vec_format(path + 'word2vec.txt', binary = False)
model2 = KeyedVectors.load_word2vec_format(path + 'word2vec_5.txt', binary = False)
model3 = KeyedVectors.load_word2vec_format(path + 'glove.txt', binary = False)
fields = ['word1', 'word2', 'word2vec', 'word2vec_5','glove']
q = [['cash','money'],['profit','gain'],['global','international'],['house','home'],['agreement','contract'],['pleaded','guilty'],['employee','employer'],['firm','company'],['income','tax'],['inventory','stock']]
f = open(os.getcwd() + '/csv/result.csv','w')
writer = csv.DictWriter(f, fields)
writer.writeheader()
csvwriter = csv.writer(f)
for words in q:
	try:
		words = lemmatize_sentence(words)
		word1,word2 = words[0],words[1]
		a = model1.similarity(word1,word2)
		b = model2.similarity(word1,word2)
		c = model3.similarity(word1,word2)
		csvwriter.writerow([word1,word2,a,b,c,])
	except:
		print(words)
f.close()









