import random

r=random.randint(1,10)

print('Guess a number betwen 1 and 10')
num=input('your guess: ')
num=int(num)

if r == num:
    print('You Win! The number was: ' + str(r))

else: print('You lose! The number was: ' + str(r))
