import string

alphabet = set(string.ascii_lowercase)
#print the lower case alphabet
print(alphabet)
#inputing the String from user
st = input("enter the string:  ")
#converting the give string into lower case
print("The given string in lowercase:", st.lower())
#and getting each letter without no repetition
print("characters present in the given String:", set(st.lower()))
if set(st.lower()) >= alphabet:
    print("The Given Input String Contains all letters of Alphabet")

else:
    print("The Given Input String doesn't Contains all letters of Alphabet")
