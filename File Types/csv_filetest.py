
import os
import csv
import random
import string

'''
Coding with Python: Learn to Read & Open a CSV File & Randomly Select an Entry

https://www.youtube.com/watch?v=NUVblHTElTk
'''

# go to Python interpreter by typing "Python".
# Type: os.getcwd()   - TO GET CURRENT PATH
# Type: os.chdir("C:\Users\Joh\Documents\Python Scripts\File Types") - TO CHANGE CURRENT PATH.
# Type: is.get
# filename = 'choice.csv"
# print filename
# file_path = os.path.join(os.getcwd(), filename)
# file_path
# then it should give you the path. 

def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	print file_path
	return file_path

	
path = get_file_path('choice.csv')

def read_csv(filepath):
        with open(filepath, 'rU') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader: # if not "Emai Address" in row:
                        print row[0], row[1], row[2]
                                
		
read_csv(path)
