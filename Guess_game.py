import random

def guess_game(limit, number):
    random_number =  random.randint(1, number)
    try:
        while limit > 0:
            guess = int(input('What is your guess'))
            limit -= 1
            if random_number == guess:
                print('You got it right!')
                break
            elif guess > number:
                print('Guess is out of range')
                print(f'You have {limit} guess(es) left')
            else:
                print('That was wrong')
                print(f'You have {limit} guess(es) left')
        print('Game over')
        print(f'The random number was {random_number}')
    except ValueError:
        print('Only integers are allowed')
        
def easy():
    print("You are to guess a number between 1 and 10, and you have 6 guesses")
    guess_game(6, 10)
    
def medium():
    print("You are to guess a number between 1 and 20, and you have 4 guesses")
    guess_game(4, 20)
    
def hard():
    print("You are to guess a number between 1 and 50, and you have 3 guesses")
    guess_game(3, 50)
    
def try_again():
    again = input('Do you want to play again? Yes/No')
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print('Thanks for playing')
    else:
        print('Wrong input')
        try_again()
    
def welcome():
    print('Welcome to Ema guessing game')
    difficulty = input("Choose your difficuly between Easy, Medium and Hard")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print('Wrong input')
        welcome()
        

welcome()
