from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["jumping","jumps","jumped","running","runner"]
stemmed_words=[stemmer.stem(word)for word in words]
print(stemmed_words)
