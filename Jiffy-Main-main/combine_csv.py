import csv
import os

cwd = os.getcwd()

#load the 2 dictionaries to be merged 
reader1 = csv.reader(open(cwd + '/csv/helper_dictionary.csv', 'r'))
reader2 = csv.reader(open(cwd + '/csv/helper_dictionary_2.csv', 'r'))

#create a dictionary with keys as input words from both dictionaries

dictionary = {}
for row in reader1:
	key = row[0]
	value = row[1:]
	dictionary[key] = value
for row in reader2:
	key = row[0]
	if key in dictionary:
		q = list(set(row[1:]+dictionary[key]))
		dictionary[key] = q
	else:
		dictionary[key] = row[1:]


new_dictionary = {}
for ele in dictionary:
	if '_' not in ele:
		new_dictionary[ele] = dictionary[ele]
	else:
		s = ele.split('_')
		for i in s:
			if i in new_dictionary:
				value = new_dictionary[i] + dictionary[ele]
				new_dictionary[i] = value
			else:
				new_dictionary[i] = dictionary[ele]

#write dictionary to third csv file which is our helper function dictionary
file = open(cwd + '/csv/helper_dictionary_3.csv','w')
writer = csv.writer(file) 
for ele in new_dictionary:
	row = [ele] + new_dictionary[ele]
	writer.writerow(row)
file.close()

'''
for ele in dictionary:
	fns = [x for x in dictionary[ele] if x != '']
	if '_' in ele:
		s = ele.split('_')
		for i in s:
			if i not in dictionary:
				new_row = [i]+fns
				writer.writerow(row)
			else:
				value = dictionary[i]
				dictionary[i] = value + fns
				row = [i]+list(set(dictionary[i]))
	else:
		row = [ele]+fns
		writer.writerow(row)
file.close()
'''
