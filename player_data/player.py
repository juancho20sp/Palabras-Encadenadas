players = []
class Player():
    def __init__(self, id: int, usr: str, score: int):
        self.__id = id
        self.__username = usr
        self.__score = score
        self.__on_game = True
        self.__on_turn = False

        self.player = {
            'id': self.__id,
            'username': self.__username,
            'score': self.__score,
            'on_game': self.__on_game,
            'on_turn': self.__on_turn
        }

        players.append(self.player)


    def get_id(self):
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_username(self):
        return self.__username

    def set_username(self, usr: str) -> None:
        self.__username = usr

    def get_score(self):
        return self.__score

    def set_score(self, score: int) -> None:
        self.__score = score

    def get_on_game(self):
        return self.__on_game

    def set_on_game(self, on_game = bool) -> None:
        self.__on_game = on_game

    def get_on_turn(self):
        return self.__on_turn

    def set_on_turn(self, on_turn: bool) -> None:
        self.__on_turn = on_turn

def create_player(player: 'Player'):
    players.append(player)
