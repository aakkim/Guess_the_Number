import random

def computer_guess(x):
    low = 1
    high = x
    response = ''
    while response != 'c':
        if low != high:
            guess_number = random.randint(low,high)
        else:
            guess_number = low
        response = input(f"Is {guess_number} too low (L), too high (H), or correct (C)?: ").lower()
        if response == 'h':
            high = guess_number - 1
        elif response == 'l':
            low = guess_number + 1
    print(f"Congrats! The computer guessed your number, {guess_number} correctly!!!")

computer_guess(20)