#input data
a =[(7, 4), (8, 2), (1,9), (4,1), (3, 6)]
print("my list of tuple elements are: \n",a)
#defining the last defination
def last(n): return n[-1]
#sorting function
def sort_tuple(tuple):
  return sorted(tuple, key=last)
#printing after sorting
print("\nAfter sorting the list with last element in tuple: \n\n", sort_tuple(a))



