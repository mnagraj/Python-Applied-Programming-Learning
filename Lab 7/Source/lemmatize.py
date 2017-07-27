from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter

#lemmatize
lemmatizer = WordNetLemmatizer()
l = ('')
file1 = open("filteredtext.txt")
line = file1.read()# Use this to read file content as a stream:

words = line.split()
for i in words:

        lem = lemmatizer.lemmatize(i,pos='v')
        print(lem)
        l = l +' ' +lem
print(l)


#word frequency

cap_words = [word.upper() for word in words] #capitalizes all the words

word_counts = Counter(cap_words)


# Top 5 words in the given file
print(word_counts.most_common())
for k, v in word_counts.most_common(5):
    print('%s: %i' % (k, v))




#removing all verbs using POS tags
for i in l:
  words = word_tokenize(l)

  sent = pos_tag(words)

for s in sent:
        if s[1] not in ['VB', 'VBN','VBG']:
            print(s)


