
import os
import csv
import random
import string

# go to Python interpreter by typing "Python".
# Type: os.getcwd()   - TO GET CURRENT PATH
# Type: os.chdir("C:\Users\Joh\Documents\Python Scripts\File Types") - TO CHANGE CURRENT PATH.
# Type: is.get
# filename = 'choice.csv"
# print filename
# file_path = os.path.join(os.getcwd(), filename)
# file_path
# then it should give you the path. 

def get_file_path(filename);
	cirrentdirpath = os.getcwd()
	file_ptath = os.path.join(os.getcwd(), filename)
	print file_path
	return file_path

	
path = get_file_path('choice.csv')

def read_csv(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		print reader

		
read.csv(path)
