import os
import string
from clean import clean

#function to return a list oflists of the entire corpus cleaned and to be fed as input to the Word2Vec model
def preprocess(path):
	folders = os.listdir(path=path)
	data = []
	for folder in folders:
		for file in os.listdir(path+folder):
			f = open(path+folder+'/'+file,'r')
			doc = f.read()
			doc = clean(doc)
			data.append(doc)
	return data
