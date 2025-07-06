class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

bingo_game = Bingo()
print(bingo_game.play())