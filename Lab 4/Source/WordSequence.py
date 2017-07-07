#inputing the user words
list_words = input("Input list of words split by comma: ")
#storing the input words into list
seq_words = [words for words in list_words.split(",")]
print("Taking the input words into list:",(seq_words))
#sorting the list by alphabetical order
print(",".join(sorted(list(set(seq_words)))))

