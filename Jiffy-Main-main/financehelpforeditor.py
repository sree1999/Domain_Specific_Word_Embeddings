
import gensim
from make_helper_dictionary import nltk_tag_to_wordnet_tag, lemmatize_sentence
import csv
import pandas as pd


import re
model = gensim.models.KeyedVectors.load_word2vec_format('glove.txt', binary = False)

reader = csv.reader(open('csv/helper_dictionary_3.csv', 'r'))
dictionary = {}
for row in reader:
   k, v = row[0],row[1:]
   dictionary[k] = v
df = pd.read_csv('file.csv')
functions = df['func'].tolist()
syntax = df['arg'].tolist()
description = df['desc'].tolist()
index = []
def findFunction(word):
	global index
	index = []
	word = lemmatize_sentence([word])[0]
	
	if word in dictionary:
		Functions = 'Related functions are \n'
		for i in range(len(dictionary[word])):
			if dictionary[word][i] != '':
				Functions = Functions+(str(i) + ' - '+dictionary[word][i] + '\n')
				index.append(functions.index(dictionary[word][i]))
		#a = input('\nwant to get more details?(y/n) ')
		# if a.lower() == 'y':
		# 	n = int(input('\nenter the function:'))
		# 	index = functions.index(dictionary[word][n])
		# 	print('\n')
		# 	print("SYNTAX: ")
		# 	print(syntax[index])
		# 	print('\n')
		# 	print('DESCRIPTION: ')
		# 	print(description[index])

	else:
		Functions ='Not found! \n Try a different keyword'
	return Functions 

def helpFunction(num):
	global index
	#word = lemmatize_sentence([word])[0]
	#n = int(input('\nEnter the function:'))
	#index = functions.index(dictionary[word][function_index])
	func_desc="SYNTAX: "+syntax[index[num]] + '\n' + 'DESCRIPTION: ' + description[index[num]]
	synt = syntax[index[num]]
	return func_desc,synt
