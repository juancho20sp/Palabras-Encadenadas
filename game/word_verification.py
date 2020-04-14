from game.game import Game

# Objetos
game = Game()

def verify_end_begin_word(word: str) -> int:
    last_word = game.get_last_word()
    print("last word: {}".format(last_word))
    print("entered word: {}".format(word))
