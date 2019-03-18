from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythonly"]

##for w in example_words:
##    print(ps.stem(w))
    
new_text = "It is very important to by pythonly while you are pythoning. All pythones have pythoned in the past."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
