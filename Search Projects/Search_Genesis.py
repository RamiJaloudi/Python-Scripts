from Genesis import*

while True:
    mySearchText=input('Enter your Search Terms: \n')
    for i in Genesis1:
        if mySearchText in i:
            print(i)
