# ACM Research Coding Challenge (Fall 2021)


## Explanation
For this challenge, I implemented the Natural Language Toolkit(1) library in Python: this library contains VADER(2) - Valence Aware Dictionary and sEntiment Reasoner - a sentiment analysis tool. Vader made the process simple: I removed the "noise" - or the punctuation - to make tokenizing the file easier for the sentiment analysis, since we only want to get the sentiment of the words, or tokens, and not the punctuation characters. After performing the sentiment analysis with Vader, I output the results: the percent of positive words, followed by the percent of negative words, followed by the percent of neutral words, and lastly a verdict on whether there is a positive or negative sentiment. Because the neutral words don't convey any sentiment, they were ignored when giving the verdict. 

For the given file, VADER determined that "input.txt" was 18.9% positive, 7.6% negative, and 73.5% neutral. When reading the first paragraph, it seems apparent that there is some negative connotation to the words, while also having sarcasm(?), although VADER only reads positive or negative sentiment. The second paragraph has more words with a positive connotation, so it makes sense that overall there is a higher positive sentiment percentage than negative.

Without VADER, this challenge becomes, well, challenging. If I were to do the sentiment analysis without VADER, I would first need to tokenize the words variable, which would be done by using the split() method provided by Python. Afterwards is where the machine learning comes in. Unfortunately, I do not know how to create a model nor train it, so this point is about as far as I can go with my current time constraints. I have an idea on how I would implement the machine learning myself, if I knew how to create the model. I would use a Naive Bayes model because of its ability to classify data into groups. I would supervise the model to ensure that the proper values are reached. The values would be placed on a scale of -3 to 3, which goes from: very negative (-3), negative (-2), somewhat negative (-1), neutral (0), somewhat positive (1), positive (2), and very positive (3). The program would take the average of the word sentiment values by summing them together and dividing by the total amount of words.


## Sources Cited
1. Natural Language Toolkit (NLTK): Steven Bird, Ewan Klein, and Edward Loper (2009). Natural Language Processing with Python. O’Reilly Media Inc. http://nltk.org/book

2. VADER Sentiment Analyzer: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
