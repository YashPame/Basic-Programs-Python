# Guess the Number between 2 number input by user
import random


def GuessGame():
    print("Player 1 turn")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    number = random.randint(num1, num2)
    print(number)

    chance = 1
    while True:
        enter = int(input("Enter guess: "))

        if enter > number:
            print("The number is smaller")
            chance = chance + 1
        elif enter < number:
            print("The number is greater")
            chance = chance + 1
        elif enter == number:
            print("Right guess, You Won!")
            print(f"You guessed in {chance} chances")
            break

    print("Player 2 turn")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    number = random.randint(num1, num2)
    print(number)

    chance2 = 1
    while True:
        enter = int(input("Enter guess: "))

        if enter > number:
            print("The number is smaller")
            chance2 = chance2 + 1
        elif enter < number:
            print("The number is greater")
            chance2 = chance2 + 1
        elif enter == number:
            print("Right guess, You Won!")
            print(f"You guessed in {chance2} chances")
            break

    if chance>chance2:
        print("Player 2 Win")
    elif chance<chance2:
        print("Player 1 Win")
    else:
        print("Draw")


GuessGame()
while True:
    restart = input("Enter c to continue, q to quit: ")
    if restart == 'c':
        GuessGame()
    elif restart == 'q':
        exit()
    else:
        print("Invalid")
