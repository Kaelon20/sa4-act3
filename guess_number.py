def guess_number(number):
    choice = input("Enter q to quit guessing and to continue enter anyhing else: ")
    if choice == 'q':
        print(f"Sorry! The number was {number}.")
    else:
        print("I'm thinking of a number...")
        guess = int(input("What number am I thinking of? "))

        if guess == number:
            print("Congratulations! You guessed the right number.")
        else:
            if guess > number:
                print('Guess was higher than number')
            else:
                print('Guess was lower than number')
            print("Wrong try again")
            guess_number(number)

number = 10
guess_number(number)