import random

class Player:
    CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    def __init__(self):
        self.move = None
        self.move_history = []
        self.points = 0

    def display_move_history(self):
        if not self.move_history:
            print("No moves yet")
        for i, move in enumerate(self.move_history):
            print(f"Move {i + 1}: {move}")

class Computer(Player):
    def __init__(self):
        super().__init__()
   

class R2D2(Computer):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        self.move = "rock"
        self.move_history.append(self.move)

class HAL(Computer):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        weights = [15, 15, 40, 15, 15]
        self.move = random.choices(Player.CHOICES, weights=weights, k=1)[0]
        self.move_history.append(self.move)

class DANEEL(Computer):
    def __init__(self, human_player):
        super().__init__()
        self._human_player = human_player

    def choose(self):
        human_moves = self._human_player.move_history
        if not human_moves or len(human_moves) < 2:
            self.move = random.choice(Player.CHOICES)
        else:
            self.move = human_moves[-2]
        self.move_history.append(self.move)


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = f"\nPlease choose {', '.join(self.CHOICES[:-1])} or {self.CHOICES[-1]}: "
            
        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break
            
            print(f"Sorry, {choice} is not valid")

        self.move = choice
        self.move_history.append(self.move)

class RPSGame:
    WINNING_LINES = {"rock": ("scissors", "lizard"),
                     "paper": ("rock", "spock"),
                     "scissors": ("lizard", "paper"),
                     "lizard": ("spock", "paper"),
                     "spock": ("rock", "scissors")}

    WINNING_POINTS = 5

    def __init__(self):
        self._human = Human()
        self._computer = DANEEL(self._human)

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def _display_goodbye_message(self):
        print('\nThanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def _human_wins(self):
        return self._computer.move in self.WINNING_LINES[self._human.move]

    def _computer_wins(self):
        return self._human.move in self.WINNING_LINES[self._computer.move]
    
    def _display_winner(self):
        print(f'\nYou chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            self._human.points += 1
            print("\nYou win!")
        elif self._computer_wins():
            self._computer.points += 1
            print("\nComputer wins!")
        else:
            print("\nIt's a tie!")

    def _display_points(self):
        print(f"\nPlayer points: {self._human.points}")
        print(f"Computer points: {self._computer.points}")

    def play(self):
        self._display_welcome_message()
        self._display_points()

        while True:
            self._human.choose()
            self._computer.choose(self._human.move_history)

            self._display_winner()
            self._display_points()


            if self._human.points == self.WINNING_POINTS or self._computer.points == self.WINNING_POINTS:
                if self._human.points == self.WINNING_POINTS:
                    print(f"\nYou win this round of {self.WINNING_POINTS}!")
                elif self._computer.points == self.WINNING_POINTS:
                    print(f"\nComputer wins this round of {self.WINNING_POINTS}!")
                
                print(f"\nHuman's move history: ")
                self._human.display_move_history()

                print(f"\nComputer's move history: ")
                self._computer.display_move_history()

                if not self._play_again():
                        break
        self._display_goodbye_message()

    def _reset_game(self):
        self._human.points = 0
        self._human.move_history = []
        self._computer.points = 0
        self._computer.move_history = []


    def _play_again(self):
        answer = input("Would you like to play again? (y/n): ")

        while True:
            if answer.lower().startswith("y"):
               self._reset_game()
               return True
            
            if answer.lower().startswith("n"):
                return False
            
            answer = input("That's not a valid input. Would you like to play again? (y/n): ")


game = RPSGame()
game.play()