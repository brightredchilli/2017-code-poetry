import random
import textblob
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.blob import _penn_to_wordnet as penn_to_wordnet

# print("Translation Test:")
# translation_test = TextBlob("something is haunting europe")
# print(translation_test.translate(to="es"))

test = "dialectical impressionism"
blob = TextBlob(test)
print ("blob = TextBlob(\"{}\")".format(test))
print("blob.sentences = ", blob.sentences)
print("blob.tags = ", blob.tags)
print("blob.words = ", blob.words)
print("blob.words[1] = ", blob.words[1])
print("blob.words.lemmatize() = ", blob.words.lemmatize())
print("\n")

test = "running"
word = Word(test)
print ("word = Word(\"{}\")".format(test))
print("word.lemmatize(v)", word.lemmatize("v"))
print("\n")
print(penn_to_wordnet(word.tags))

test = "beautifully"
word = WordList(test)
print ("word = Word(\"{}\")".format(test))
pos = textblob.wordnet.ADJ
print("word.lemmatize(\"{}\")".format(pos), word.lemmatize(pos))
print("\n")

print("Word(\"hack\").get_synsets(pos=VERB)", Word("hack").get_synsets(pos=VERB))
print("\n")
