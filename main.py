# Written by Frankie Flores for the Fall 2021 ACM Research Coding Challenge

import nltk
from nltk.tokenize import word_tokenize # Cite this source

fileReader = open("input.txt").read()
words = word_tokenize(fileReader)
print(words)