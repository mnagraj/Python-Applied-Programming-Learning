#Inputing the two lists

input_1 = input("Input list of words split by comma: ")
seq_a = set([words for words in input_1.split(",")])

print("given words into the list :",seq_a)

input_2 = input("Input list of words split by comma: ")
seq_b = set([words for words in input_2.split(",")])

print("given words into the list :",seq_b)

set_c = seq_a ^ seq_b

print("The Sysmetric Difference of Given Two sets is: ",set_c)