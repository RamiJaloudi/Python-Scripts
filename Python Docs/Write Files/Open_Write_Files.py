# This is an exercise to open, write, etc....files.
# fileobj = open( filename, mode )

some_text = '''ABCDEFGHIJKLMNOPQRST,
1234567891011121314151617181920'''
# len(some_text)

fout = open('relativity', 'wt')
fout.write(str(some_text))
fout.close()


