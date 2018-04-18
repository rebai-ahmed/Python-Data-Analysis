import nltk
import random

example_text = "I was feeling lonely yesterday so I went alone to the cinema to watch a movie."
example_text = nltk.word_tokenize(example_text)
random.shuffle(example_text)

print(example_text[0])

all_words = []
for w in example_text:
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(3))