#inputing the number of rows
n = int(input("Enter a number: "))
#calculating the number of spaces
space = n - 2
prnt_ln = "*"*n
for j in range(1, n+1):
    if space > 0:
        prnt_ln_n = "*"*j+" "*space+"*"*j
        space -= 2
        print(prnt_ln_n)
    else:
        print(prnt_ln)