
import random

random_num = random.randint(1,100)
count = 10
print('Welcome to Guess Game:')
print(f'you have {count} chances only')
print('Input the number between 1 to 100')

user_num = int(input('Enter your guess number: '))

while True:
    count -= 1
    if count == 0:
        print('Game over! you lost')
        print('Do you want to play again: y/n')
        ch = input('Enter your choice: y/n: ')
        if ch == 'y':
            print('Input the number between 1 to 100')

            user_num = int(input('Enter your guess number: '))
            count = 10
            count -= 1
        else:
            print('thank you for play this game')
            print('Best luck for the Next time')
            break
    if user_num < random_num:
        print(f'{user_num} is smaller than guess number and chances left {count}')
        user_num = int(input('Enter your guess number: '))
    elif user_num > random_num:
        print(f'{user_num} is greater than guess number and chances left {count}')
        user_num = int(input('Enter your guess number: '))
    else:
        print(f'your guess is correct {random_num}')
        break
