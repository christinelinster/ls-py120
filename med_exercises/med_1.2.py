
import random

class GuessingGame:

    def __init__(self):
        self._remaining_guesses = 7
        self._number = random.randint(1, 100)
        self.guess = None

    def guess_number(self):
        self.guess = input("Enter a number between 1 and 100: ")
        while True:
            if self.guess.isdigit() and 1 <= int(self.guess) <= 100:
                self.guess = int(self.guess)
                self._remaining_guesses -= 1
                break

            self.guess = input("Invalid guess. Enter a number between 1 and 100: ")

    def display_result(self):
        if self.guess == self._number:
            print("That's the number!")
        elif self.guess > self._number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    def show_remaining_guesses(self):
        if self._remaining_guesses == 1:
            print("\nYou have 1 guess remaining.")
        else:
            print(f"\nYou have {self._remaining_guesses} guesses remaining.")

    def reset_game(self):
        self._number = random.randint(1,100)
        self._remaining_guesses = 7

    def game_over(self):
        if self.guess == self._number:
            print("\nYou won!")
            return True
        elif self._remaining_guesses == 0:
            print("\nYou have no more guesses. You lost!")
            return True

        return False

    def play(self):
        self.reset_game()
        while True:
            self.show_remaining_guesses()
            self.guess_number()
            self.display_result()
            if self.game_over():
                break



game = GuessingGame()
game.play()

# game = GuessingGame()
# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!