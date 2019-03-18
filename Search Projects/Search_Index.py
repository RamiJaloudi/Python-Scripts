list = data_array
string = str(raw_input("Search keyword: "))
print string
for s in list:
    if string in str(s):
        print 'Yes'
        print list.index(s)
