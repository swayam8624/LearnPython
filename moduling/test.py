'''
import random

print(dir(random))
l=[1,2,3,4,5]
random.shuffle(l)
print(l)

import sys
print(sys)
#first index is file name
first = sys.argv[1] #takes input while running file in the terminal in form of tuple
last = sys.argv[2]

print("hiii" + first + last)
'''
'''
#guessing game

import random

while True:
    try:
        n=int(input('enter a number \n'))
        num= random.randint(1,10)
        if n in range(1,11) and n==num:
            print("congrats")
            break
        else:
            print("sorry bud number is ", num)
            continue
    except ValueError:
        print('enter a number')
        continue
'''
'''
import pyjokes

print(pyjokes.get_joke('en','neutral'))
'''