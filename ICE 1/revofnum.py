import math

print("Welcome to Reverse of a Number !!")

number = input('please enter the number to reverse it :')

n = int(number)

print('your entered number is:',n)

rev=0

while(n>0):
    r = n % 10
    n=n//10

    rev=(rev*10)+r

print("The reverse of a given number is:",rev)