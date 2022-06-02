import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x}: '))
        if guess_number < random_number:
            print("Sorry, that's not right! Number too low.")
        elif guess_number > random_number:
            print("Sorry, try again! Number too high.")
    print(f'Awesome you guessed the correct number, {random_number}!!!')

guess(20)




