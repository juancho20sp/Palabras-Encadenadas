
class Game():
    def __init__(self):
        self.__num_players = 0
        self.__themes = set()
        self.__players = {}
        self.__players_to_register = 0
        self.__active_players = 0
        self.__winner = 0

    def create_player_ongame_data(self, players: int):
        players = dict([("Jugador {}".format(i + 1), 0) for i in range(players)])
        self.set_players(players)

    def get_num_players(self):
        return self.__num_players

    def set_num_players(self, num: str):
        self.create_player_ongame_data(int(num))
        self.set_active_players(int(num))
        self.__num_players = int(num)

    def get_players_to_register(self):
        return self.__players_to_register

    def set_players_to_register(self, num: int):
        self.__players_to_register = num

    def get_themes(self):
        my_list = list(self.__themes)
        my_word = ", ".join(my_list)
        return my_word

    def set_themes(self, theme: str):
        self.__themes.add(theme)

    def get_players(self):
        pass

    def set_players(self, players: dict):
        self.__players = players

    def get_active_players(self):
        return self.__active_players

    def set_active_players(self, num: int):
        self.__active_players = num

    def get_winner(self):
        return "El ganador"
        #return self.__winner

    def set_winner(self, winner):  # Agregar ganador
        self.__winner = winner