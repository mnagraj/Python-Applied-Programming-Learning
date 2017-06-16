s = input("Input a string ::")
d=l=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)