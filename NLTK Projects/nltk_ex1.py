from nltk.tokenize import sent_tokenize, word_tokenize

##import nltk
##nltk.download()
'''
# toekinizing - word tokenizing...sentence tokenizers
# lexicon and corporas
# copora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their means
# investor-speak...regular english-speak
# investor speak "bull" = someone who is positive about the market
# english-speak "bull" = scary animal.
'''
# his code is on pythonproramming.net ....dashboard...data analysis...nltk

example_text = "Hello Mr. Smith, how are you toda? The weather is great and Python is awesome.  The sky is pinkish-blue. You should not eat carboard."

##print(sent_tokenize(example_text))
##
##print(word_tokenize(example_text))

##for i in word_tokenize(example_text):
##    print(i) 

'''
## My input: Here, opening a text file and reading it, decoding it, then tokenizing it. 
file = open('testtext.txt', 'r')
# print file.read()
temp = file.read()
draft = temp.decode('utf-8')
for i in word_tokenize(draft):
    print(i)
#print(sent_tokenize(draft))
'''


