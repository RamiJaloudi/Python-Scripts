
def print_table():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in numbers:
        print '\t' + str(i)
    print #End the header now

    for i in numbers:
        print i,
        for j in numbers:
            print '\t' + str(i * j),
        print
           
