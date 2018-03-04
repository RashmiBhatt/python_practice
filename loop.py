# execute of a statement multiple times
# two type finit and infinite
# three kind of loop in python for,while,nested
#while expression: statement    #syntax

count=0
while(count<9):
    print("number :",count)
    count= count+1
print('good bye')

import random
n=20
to_be_guessed =int(n*random.random())+1
guess= 0
while guess != to_be_guessed:
    guess =int(input("new number :"))
    if guess>0:
        if guess>to_be_guessed:
            print("number too large")
        elif guess< to_be_guessed:
            print('number to small')
    else:
        print('sorry that you are giving up ' )
        break
else:
    print("congratulation you made it ! ")



