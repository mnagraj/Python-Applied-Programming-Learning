import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.

stop_words = set(stopwords.words('english'))
file1 = open("data.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for i in words:
    if not i in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+i)
        appendFile.close()