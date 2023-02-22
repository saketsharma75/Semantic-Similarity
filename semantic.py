import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own'''

'''I found it interesting that the similarity scores are based on the contextual meaning of the words,
rather than just their surface-level similarity in spelling or pronunciation. An example of my own is: the words "apple" and "orange"
they are often compared or contrasted with each other because they are both types of fruit.'''

'''When the simpler language model 'en_core_web_sm' is used, the similarity scores are lower than when the more complex language model 'en_core_web_md' is used.
This is because the more complex language model has more information about the words and their meanings, which allows it to make more accurate similarity scores.
There is also a warning at the output that the simpler model has no word vectors loaded, which may not give useful similarity judgments.'''
