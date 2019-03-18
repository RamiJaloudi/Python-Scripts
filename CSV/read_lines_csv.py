ateimport csv, sys
filename = 'the_links.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    
    try:
        for row in reader:
            print(row)
            
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


'''
import csv
with open("the_links.csv", "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print 'line[{}] = {}'.format(i, line)
'''
'''
for line in open("csvfile.csv"):
    csv_row = line.split() #returns a list ["1","50","60"]
'''
