import csv
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from make_helper_dictionary import nltk_tag_to_wordnet_tag, lemmatize_sentence
import gensim
import os


def print_format(l):
	print('here are the results \n')
	for i in range(len(l)):
		print(str(i) + ' - '+l[i])
	a = input('\nwant to get more details?(y/n) ')
	if a.lower() == 'y':
		if len(l) == 1:
			index = functions.index(l[0])
			print('\n')
			print("SYNTAX: ")
			print(syntax[index])
			print('\n')
			print('DESCRIPTION: ')
			print(description[index])
		else:
			n = int(input('\nenter the function:'))
			index = functions.index(l[n])
			print('\n')
			print("SYNTAX: ")
			print(syntax[index])
			print('\n')
			print('DESCRIPTION: ')
			print(description[index])

lemmatizer = WordNetLemmatizer()
cwd = os.getcwd()
#get user input word as a string
word = input('enter word: ')
word = lemmatize_sentence([word])[0]

reader = csv.reader(open(cwd + '/csv/helper_dictionary_3.csv', 'r'))
dictionary = {}
for row in reader:
	key = row[0]
	value = row[1:]
	dictionary[key] = value

df = pd.read_csv(cwd + '/csv/financepy.csv')
functions = df['func'].tolist()
syntax = df['arg'].tolist()
description = df['desc'].tolist()

reader2 = csv.reader(open(cwd + '/csv/description.csv', 'r'))
dictionary2 = {}
for row in reader2:
	key = row[0]
	value = row[1:]
	dictionary2[key] = value

if word not in dictionary and word not in dictionary2:
	func = []
	for i in functions:
		func.append(i.split('.')[-1].lower())
	suggestions = []
	for i in func:
		if word in i:
			suggestions.append(functions[i])
	if len(suggestions) > 0:
		print_format(suggestions)


	else:
		print("not found")
else:
	print('yes')

	if word in dictionary:
		v1 = dictionary[word]
	else:
		v1 = []
	if word in dictionary2:
		v2 = dictionary2[word]
	else:
		v2 = []
	v = list(set(v1+v2))
	print_format(v)
