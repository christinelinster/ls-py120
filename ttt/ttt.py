import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER= "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker = INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return f"{self.marker}"

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1,10)}

    def unused_squares(self):
        return [key for key, square
                in self.squares.items()
                if square.is_unused()]
    
    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()


    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_squares_at(self, key, marker):
        self.squares[key].marker = marker

    def count_markers_for(self, player, keys): # returns 0, 1, 2, or 3
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)


class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        self.display_welcome_message()
        self.board.display()
        
        while True:
            self.play_one_game()
            if not self.play_again():
                break
            else:
                self.reset_game()
            
        self.display_goodbye_message()
    
    def play_one_game(self):
        while True:
                self.human_moves()
                if self.is_game_over():
                    break

                self.computer_moves()
                if self.is_game_over():
                    break

                self.board.display()

        self.board.display_with_clear()
        self.display_results()


    def play_again(self):
        while True:
            answer = input("Do you want to play again? (y/n): ").lower()
            if answer in ("y", "yes", "n", "no"):
                break
                
            print("Sorry, that's not a valid choice.")
        clear_screen()
        return answer in ("y", "yes")

    def reset_game(self):
        self.board.reset()
        self.board.display_with_clear()
        

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")
    
    @staticmethod
    def _join_or(choices, delimiter=', ', conjunction='or'):
        prompt = [str(choice) for choice in choices]
        if len(prompt) == 1:
            return prompt[0]
        
        if len(prompt) == 2:
            return f"{prompt[0]} {conjunction} {prompt[1]}"
        return f"{delimiter.join(prompt[:-1])} {conjunction} {prompt[-1]}"

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            prompt = f"Choose a square ({self._join_or(valid_choices)}): "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            print("Sorry that's not a valid choice.")
            print()

        self.board.mark_squares_at(choice, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        
        choice = self.defensive_move()
        if not choice:
            choice = random.choice(valid_choices)
        # Need to make sure it is empty first
        self.board.mark_squares_at(choice, self.computer.marker)

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3
    
    def defensive_move(self):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            key = self.at_risk_square(row)
            if key:
                return key
        return None

    def at_risk_square(self, row):
        if self.board.count_markers_for(self.human, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key
        return None

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def someone_won(self):
        return self.is_winner(self.human) or self.is_winner(self.computer)

game = TTTGame()

game.play()