def guess_number(number):
    total_guesses = 5
    while total_guesses > 0:
        print(f'You have {total_guesses} remaining')
        print("I'm thinking of a number...")
        guess = int(input("What number am I thinking of? "))

        if guess == number:
            print("Congratulations! You guessed the right number.")
            return
        else:
            if guess > number:
                print('Guess was higher than number')
            else:
                print('Guess was lower than number')
            print("Wrong try again")
        total_guesses = total_guesses - 1
    
        print(f'Out of guesses number is {number}')
    

    

number = 10
guess_number(number)