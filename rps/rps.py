import random

class Player:
    CHOICES = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = "Please choose rock, paper, or scissors: "

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

        print(f"Sorry, {choice} is not valid")

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')


    def _human_wins(self):
        winning_lines = {"rock": "scissors",
                         "paper": "rock",
                         "scissors": "paper"}
        human_move = self._human.move
        computer_move = self._computer.move

        return winning_lines[human_move] == computer_move

    def computer_wins(self):
        winning_lines = {"rock": "scissors",
                         "paper": "rock",
                         "scissors": "paper"}
        human_move = self._human.move
        computer_move = self._computer.move

        return winning_lines[computer_move] == human_move

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print("You win!")
        elif self.computer_wins():
            print("Computer wins!")
        else:
            print("It's a tie!")

    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()


    def _play_again(self):
        answer = input("Would you like to play again? (y/n)")
        return answer.lower().startswith("y")


game = RPSGame()
game.play()