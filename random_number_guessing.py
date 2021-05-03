#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program gets the user to guess a pseudo-random number

import random


def main():
    # this function generates a pseudo-random number and gets the user
    #   to guess the number

    # input
    correct_number = random.randint(0, 9)  # a number from 0 - 9
    guess = int(input("Guess a number from 0 - 9: "))

    # process & output
    if guess == correct_number:
        print("\nCorrect!")
    else:
        print("\nIncorrect! The number was {0}.".format(correct_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
