from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))
# The following will list the set of stopwords
# print(stop_words)

words = word_tokenize(example_sentence)

filtered_sentence = []

##for w in words:
##    if w not in stop_words:
##        filtered_sentence.append(w)
##print(filtered_sentence)

# Below is more efficient than the above block of code.
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)

'''
# Note: I tried opening this file, but tokenizing and stopwords failed. 
file = open('testtext.txt', 'r')
# print file.read()
temp = file.read()
# draft = temp.decode('utf-8')
# Below is more efficient than the above block of code.
filtered_sentence = [w for w in temp if not w in stop_words]
print(filtered_sentence)
'''
