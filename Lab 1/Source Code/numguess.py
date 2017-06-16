#number Guessing Game

import random

print("Welcome to Number Guessing Game !!! \n")
print("If Number between 1 and 10 Choosen by you matches with the Systems Number generated randomly then you will win \n")
print("if not you can your attempt again for 5 times\n")

#initalizing the score and attempt to zero
attempt=0
score = 0




while attempt<6:

#generating the random number
 number = random.randint(1, 10)

#inputing users choice of number
 numguss = input('Guess the one number:   ')
 g = int(numguss)

#comparing the your choice with systmes number
 if g<number:
    print('number is less than the systems Guess Number\n')

 elif g>number:
    print('number is greater than the systems Guess Number\n')

 else:
    print('congratulations !! YOu Won , the number exactly matches with the systems number random number ',number)
    score=score+1

 attempt=attempt+1

 print('Your Score is :',score,'\n')

if score == 0:
     print('Try YOur Luck Again !!')