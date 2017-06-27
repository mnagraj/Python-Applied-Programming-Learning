#inputing the string
a = input("Enter a String to Convert into list and tuple:  ")
#for charecters in the string
b=set(a)
print("The set elements in the given string are:",b)
#for displaying the string elements in the list format
c=list(a)
print("The list elements are:", c)
#to display string elements in tuple form
d=tuple(a)
print("The tuple elements are:", d)

# list basic operations
print("some basic operations of list:")
b=[]
#inputing the list numbers
for i in range(0,5):
    a = int(input("enter no. :"))
    b.insert(i,a)
    i = i + 1
print("The list elements are :", b)

#max in list
print("the max number in list :", max(b))
#min in list
print("The min number in the list :", min(b))
#appending operation
c= int(input("enter one number to append :"))
b.append(c)
print("after appending the list with one element :",b)

#reverse of list
b.reverse()
print("reversing the list ",b)
#sorting of list
b.sort()
print("sorting the list in increasing order:",b)
