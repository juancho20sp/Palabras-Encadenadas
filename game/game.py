"""
Turns feature branch
"""

class Game():
    def __init__(self):
        self.__num_players = 0
        self.__themes = set()
        self.__players = []
        self.__pos_indx = []

        self.__players_to_register = 0

        self.__winner = []
        self.__id_currently_playing = 1
        self.__next_player = 0

        self.__last_word = ""
        self.__last_valid_word = ""
        self.__words_on_game = []

        self.__is_playing = 0
        self.__editing_theme = ""
        self.__editing_player = ""

        # Turnos
        # ----------------------
        self.__playing = ""
        self._first_players = []
        self.__actual_players = []
        # ----------------------

    def create_player_ongame_data(self, players: int):
        data = []
        pos_indx = [i for i in range(players)]

        for i in range(players):
            if i == 0:
                player = {'id': i + 1,
                          'username': "user {}".format(i+1),
                          'score': 0,
                          'on_game': True,
                          'on_turn': True
                          }
            else:
                player = {'id': i+1,
                          'username': "user {}".format(i+1),
                          'score': 0,
                          'on_game': True,
                          'on_turn': False
                          }

            data.append(player)

        self.__pos_indx = pos_indx
        self.set_players(data)

    def give_up_player(self, id: int):
        self.get_players()[id - 1]['on_game'] = False
        self.get_players()[id - 1]['on_turn'] = False

        # Asignamos el nuevo turno
        for player in range(id-1, len(self.get_players())):
            if self.get_players()[player]['on_game'] == True:
                self.get_players()[player]['on_turn'] = True
                break


    def begin_turn(self, id: int):
        """
        :param id: Recibe el id del último jugador que tuvo el turno, se cuenta desde 1
        :return: Nada.
        """
        self.get_players()[id-1]['on_turn'] = False




        active_players = sum([1 for el in self.get_players() if el['on_game'] == True])


        if id == len(self.get_players()):
            if self.get_players()[0]['on_game'] == True:
                self.set_currently_playing_id(1)
            else:
                # CAMBIAR UD -1 POR ID
                for index in range(len(self.get_players())):
                    if self.get_players()[index]['on_game'] == True:
                        self.get_players()[index]['on_turn'] = True
                        self.set_currently_playing_id(self.get_players().index(self.get_players()[index]))
                        break
                    else:
                        continue
        else:
            if self.get_players()[id]['on_game'] == True:
                for index in range(id, len(self.get_players())):
                    if self.get_players()[index]['on_game'] == True:
                        self.get_players()[index]['on_turn'] = True
                        self.set_currently_playing_id(self.get_players().index(self.get_players()[index]) + 1)
                        break
            else:


                if id + 1 != len(self.get_players()):
                    for index in range(len(self.get_players())):
                        if self.get_players()[index]['on_game'] == True:
                            self.get_players()[index]['on_turn'] = True
                            self.set_currently_playing_id(self.get_players().index(self.get_players()[index]) + 1)
                            break
                        else:
                            continue
                else:
                    # QUITAR EL ID -1 Y PONER ID
                    for index in range(len(self.get_players())):
                        if self.get_players()[index]['on_game'] == True:
                            self.get_players()[index]['on_turn'] = True
                            self.set_currently_playing_id(self.get_players().index(self.get_players()[index]))
                            break
                        else:
                            continue



    def update_score(self, id: int, score: int) -> None:
        old_score = self.get_players()[id]['score']
        new_score = old_score + score

        self.get_players()[id]['score'] = new_score

    def get_currently_playing_id(self):
        return self.__id_currently_playing

    def set_currently_playing_id(self, id: int):

        if self.__players[id - 1]['on_game'] == True:
            self.__players[id - 1]['on_turn'] = True
            self.__id_currently_playing = id
        else:
            if id == len(self.get_players()):
                for index in range(len(self.get_players())):
                    if self.get_players()[index]['on_game'] == True:
                        self.get_players()[index]['on_turn'] = True
                        self.__id_currently_playing = self.get_players().index(self.get_players()[index]) + 1
                        break
            else:
                for index in range(id-1, len(self.get_players())):
                    for index in range(len(self.get_players())):
                        if self.get_players()[index]['on_game'] == True:
                            self.get_players()[index]['on_turn'] = True
                            self.__id_currently_playing = self.get_players().index(self.get_players()[index]) + 1
                            break

    def get_num_players(self):
        return self.__num_players

    def set_num_players(self, num: str):
        self.create_player_ongame_data(int(num))
        #self.set_active_players(int(num))
        self.__num_players = int(num)

    def get_players_to_register(self):
        return self.__players_to_register

    def set_players_to_register(self, num: int):
        self.__players_to_register = num

    def get_themes(self):
        my_list = list(self.__themes)
        my_word = ", ".join(my_list)
        return my_list

    def set_themes(self, theme: str):
        self.__themes.add(theme)

    def clear_themes(self):
        self.__themes.clear()

    def get_players(self):
        return self.__players

    def set_players(self, players: list):
        self.__players = players

    def get_winner(self) -> list:
        return self.__winner

    def set_winner(self, winners: list) -> None:  # Agregar ganador
        self.__winner = winners

    def get_next_player(self):
        pass

    def set_next_player(self):
        pass

    def get_last_word(self):
        return self.__last_word

    def set_last_word(self, word: str):
        self.__last_word = word

    def get_last_valid_word(self):
        return self.__last_valid_word

    def set_last_valid_word(self, word: str):
        self.__last_valid_word = word

    def get_is_playing(self):
        return self.__is_playing

    def set_is_playing(self, index: int):
        self.__is_playing = index

    def get_editing_theme(self):
        return self.__editing_theme

    def set_editing_theme(self, theme: str):
        self.__editing_theme = theme

    def get_editing_player(self):
        return self.__editing_player

    def set_editing_player(self, username: str):
        self.__editing_player = username

    # Turnos
    # -----------------------------------
    def get_playing(self) -> str:
        """

        :return: Retorna el ID del usuario en la base de datos.
        """
        return self.__playing

    def set_playing(self, player) -> None:
        """

        :param player: ID del usuario en la base de datos.
        :return:
        """
        self.__playing = player

    def get_first_players(self) -> list:
        return self.__first_players

    def set_first_players(self, players: list) -> None:
        self.__first_players = players

    def get_actual_players(self) -> list:
        """

        :return: Lista con los diccionarios correspondientes a cada usuario.
        """
        return self.__actual_players

    def set_actual_players(self, players: list) -> None:
        """

        :param players: Lista con un diccionario correspondiente a cada jugador.
        :return: Nada.
        """
        self.__actual_players = players
    # -----------------------------------


