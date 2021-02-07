import random

r=random.randint(1,10)
print(r)

guessnumber = 0
check = True
num = None

while guessnumber < 3 and not(r == num):

    while check:
        print('Guess a number betwen 1 and 10')
        num=input('your guess: ')

        if num.isdigit():
            num=int(num)
            check = False

        else: print('Not a number. Try again.')

    if r == num:
        print('You Win! The number was: ' + str(r))

    else: print('Nope. Try again.')
    guessnumber += 1
    check = True

    if guessnumber == 3 and not(r == num):
        print('You lose! The number was: ' + str(r))
