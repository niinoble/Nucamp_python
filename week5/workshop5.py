from math import pi
import random


def guess_random_number(tries, start, stop):
    chosen_number = random.randint(start, stop)
    while tries > 0:
        print(f"Number of tries left: {tries}")
        tries -= 1
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == chosen_number:
            print("You guessed the correct number!")
            return
        elif guess > chosen_number:
            print("Guess lower!")
        elif guess < chosen_number:
            print("Guess higher!")

    print(f"You failed to guess the correct number: {chosen_number}")


def guess_random_num_linear(tries, start, stop):
    chosen_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {chosen_number}")

    for item in range(start, stop):
        if tries <= 0:
            print("The program failed to guess the correct number.")
            return
        print(f"Number of tries left: {tries}")
        if item == chosen_number:
            print("The program has guessed the correct number!")
            return
        else:
            print(f"The program is guessing... {item}")

        tries -= 1

    print("The program has failed to guess the correct number.")


def guess_random_binary(tries, start, stop):
    chosen_number = random.randint(start, stop)

    while tries > 0:

        guess = random.randint(start, stop)

        if guess == chosen_number:
            print(f"Found it! {chosen_number}")
            return
        elif guess < chosen_number:
            print("Guessing higher!")
            start = guess + 1

        elif guess > chosen_number:
            print("Guessing Lower!")
            stop = guess - 1

        tries -= 1

    print("Your program  failed to find the correct number.")


guess_random_binary(5, 0, 100)


'''     Test   '''
''' # Task 1  '''
# guess_random_number(5,0,10)
''' # Task 2  '''
# guess_random_num_linear(5,0,10)
