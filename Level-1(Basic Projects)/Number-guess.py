This Python script implements a number guessing game using object-oriented programming.

Features:

1.Engaging Introduction: Welcomes the player, asks for their name, and sets the stage for the game.
2.Clear Instructions: Guides the player on how to make guesses.
3.Feedback: Provides hints if the guess is too high or too low.
3.Multiple Attempts: Offers up to 6 guesses to find the hidden number.
4.Victory and Defeat Messages: Congratulates the player on success or reveals the number if they run out of guesses.
5.Replay Option: Allows the player to start a new game.

Getting Started:

*Save the code: Create a Python file (e.g., number_guessing_game.py) and paste the code into it.
*Run the script: Open a terminal or command prompt, navigate to the directory containing number_guessing_game.py, and execute python number_guessing_game.py.
                                                                                     
Enjoy the game!


import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 200)
        self.name = ""

    def intro(self):
        print("Welcome to the Number Guessing Game!")
        self.name = input("May I ask you for your name? ")
        print(f"Hello, {self.name}! I am thinking of a number between 1 and 200.")
        time.sleep(0.5)
        print("Go ahead. Take a guess!")

    def pick(self):
        guesses_taken = 0
        while guesses_taken < 6:
            try:
                guess = int(input("Guess: "))
                if 1 <= guess <= 200:
                    guesses_taken += 1
                    if guess < self.number:
                        print("Too low!")
                    elif guess > self.number:
                        print("Too high!")
                    else:
                        break
                    if guesses_taken < 6:
                        time.sleep(0.5)
                        print("Try Again!")
                else:
                    print("Please enter a number between 1 and 200.")
            except ValueError:
                print("Please enter a valid number.")

        if guess == self.number:
            print(f'Congratulations, {self.name}! You guessed my number ({self.number}) in {guesses_taken} guesses!')
        else:
            print(f"Sorry, {self.name}. The number I was thinking of was {self.number}.")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower().strip() == "yes"

    def play(self):
        while True:
            self.intro()
            self.pick()
            if not self.play_again():
                print("Thank you for playing!")
                break

game = NumberGuessingGame()
game.play()
