import tkinter as tk
from tkinter import ttk, messagebox
from files.game.game import Game
from files.game.points import word_points

# Variables
LARGE_FONT = ("Verdana", 19)
NORMAL_FONT = ("Verdana", 14)

# Game controller
game = Game()

class PalabrasEncadenadas(tk.Tk):
    """
    Clase controladora del juego, se encarga de generar los elementos necesarios para que el juego funcione y controla el flujo del mismo.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Icon
        #tk.Tk.iconbitmap(self, default="")

        # Title
        tk.Tk.wm_title(self, "Palabras Encadenadas")

        # Window size
        self.geometry("350x300+550+150")
        #self.resizable(False, False)

        # Container and its properties
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary for storing frames
        self.frames = {}

        # Fill the dictionary with the frames
        for view in (StartPage, GameMode, UsrRegisteredSelection, UsrRegistered,
                     UsrNotRegistered, MenuData, ThemeData, PlayerData, OnGame,
                     ScoreTable):
            # Pass the container to the frame
            frame = view(container, self)

            # Add the FULL frame to the dictionary
            self.frames[view] = frame

            # Frame config
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the default window
        self.show_frame(StartPage)

    def show_frame(self, view: tk.Frame) -> None:
        """
        Esta función se encarga de mostrar la ventana seleccionada por el usuario.
        :param view: Nombre de la clase que modela la 'vista' que será mostrada al usuario.
        :return: Nada.
        """
        # Take the 'view' from the dictionary
        frame = self.frames[view]

        # Put the 'view' on top
        frame.tkraise()

    def end_game(self) -> None:
        """
        Esta función se encarga de terminar el juego, en caso de que los jugadores así lo quieran o solo quede un jugador en pie.
        :return: Nada.
        """
        self.destroy()


class StartPage(tk.Frame):
    """
    Clase que crea los elementos del menú principal del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de la página inicial del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Bienvenido!", font=LARGE_FONT)
        title_2 = ttk.Label(self, text="¿Listo para jugar?", font=NORMAL_FONT)
        title.pack()
        title_2.pack()

        # Buttons
        play_btn = ttk.Button(self, text="¡A jugar!", command=lambda: controller.show_frame(GameMode))
        play_btn.pack(pady=35)

        data_btn = ttk.Button(self, text="Ver Datos", command=lambda: controller.show_frame(MenuData))
        data_btn.pack()

        exit_btn = ttk.Button(self, text="Salir", command=controller.end_game)
        exit_btn.pack(pady=35)


class GameMode(tk.Frame):
    """
    Clase que crea los elementos del menú de selección de modo del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de la página de 'selección de modo' del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="Palabras Encadenadas", font=LARGE_FONT)
        title.pack()

        # Labels and inputs
        # Player input
        players_frame = tk.Frame(self)
        players_frame.pack(pady=15)

        num_players = ttk.Label(players_frame, text="¿Cuántas personas van a jugar?", width=30)
        num_players.pack(side="left")

        num_players_spinbox = ttk.Spinbox(players_frame, from_=0, to=10)
        num_players_spinbox.pack(fill="x")

        # Test values spinbox
        # save_num_players_btn = ttk.Button(self, text="Guardar jugadores", command=lambda: self.print_players(num_players_spinbox.get()))
        # save_num_players_btn.pack()
        # -------------------

        # Theme
        theme_frame = tk.Frame(self)
        theme_frame.pack(pady=15)

        theme = ttk.Label(theme_frame, text="¿Qué temas van a usar?", width=30)
        theme.pack(side="left")

        theme_combo = ttk.Combobox(theme_frame, values=["One", "Two", "Three"])
        theme_combo.pack(fill="x")

        # Theme test combobox
        save_theme_btn = ttk.Button(self, text="Agregar tema", command=lambda:self.add_theme(theme_combo.get()))
        save_theme_btn.pack()
        # -------------------

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=20)

        next_btn = ttk.Button(buttons_frame, text="Siguiente", command=lambda:self.sumbit_all_data(num_players_spinbox.get(), theme_combo.get(), controller))


        next_btn.pack(side="left")
        back_btn = ttk.Button(buttons_frame, text="Atrás", command=lambda:controller.show_frame(StartPage))
        back_btn.pack(padx=15)

    #def add_players(self, num):
        """
        Esta función imprime el número de jugadores ingresado por el usuario a través del Spinbox.
        :param num: Valor seleccionado en el Spinbox.
        :return: Nada.
        """
        #game.set_num_players(num)
        #print("Getting from game.py {}".format(game.get_num_players()))
        #game.get_players()

    def add_theme(self, theme: str):
        """
        Esta función imprime el valor seleccionado por el usuario a través del ComboBox de temas.
        :param theme: El tema seleccionado en el Combobox.
        :return: Nada.
        """
        game.set_themes(theme)
        messagebox.showinfo("Palabras Encadenadas", "El tema ha sido añadido correctamente.")
        print("The themes are: {}".format(game.get_themes()))

    def sumbit_all_data(self, players: str, theme: str, controller: classmethod):
        if (int(players) == 0) or int(players) > 10:
            messagebox.showerror("Palabras Encadenadas", "El número de jugadores es inválido")
            controller.show_frame(GameMode)

        elif theme == "":
            messagebox.showerror("Palabras Encadenadas", "Debe elegir un tema para iniciar el juego")
            controller.show_frame(GameMode)
        else:
            game.set_num_players(players)
            game.set_players_to_register(int(players))
            game.set_themes(theme)

            messagebox.showinfo("Palabras Encadenadas", "Todo listo. ¡A jugar!")

            # DELETE BEFORE FINAL SUBMISSION
            players = game.get_num_players()
            themes = game.get_themes()
            print("{} {}".format(players, themes))
            # ------------------------------

            controller.show_frame(UsrRegisteredSelection)


class UsrRegisteredSelection(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de la página de 'selección de regustro de usuarios' del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Variables
        is_selected = tk.IntVar()
        is_selected.set(0)

        # Title
        title = ttk.Label(self, text="¡Preparemos el juego!", font=LARGE_FONT)
        title.pack()

        # Subtitle
        subtitle = ttk.Label(self, text="¿Estás registrado?", font=NORMAL_FONT)
        subtitle.pack(pady=15)

        # Yes / No frame
        yn_frame = tk.Frame(self)
        yn_frame.pack()

        # Yes / No buttons
        yes_btn = ttk.Button(yn_frame, text="Sí", command=lambda: controller.show_frame(UsrRegistered))
        yes_btn.pack(side="left")

        no_btn = ttk.Button(yn_frame, text="No", command=lambda: controller.show_frame(UsrNotRegistered))
        no_btn.pack()

        # Navigation button frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=25)

        # Navigation buttons
        back_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(GameMode))
        back_btn.pack(ipadx=30)


class UsrRegistered(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de las vistas de ingreso de un usuario registrado al juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Preparemos el juego!", font=LARGE_FONT)
        title.pack()

        # Input frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=25)

        label = ttk.Label(input_frame, text="Email o nombre de usuario: ")
        label.pack(side="left")

        entry = ttk.Entry(input_frame)
        entry.pack(fill="x")

        # Navigation buttons frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=35)

        next_player = ttk.Button(buttons_frame, text="Siguiente", command=lambda: self.verify_next(controller))
        next_player.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(UsrRegisteredSelection))
        return_btn.pack(padx=10)

    def verify_next(self, controller):
        missing = game.get_players_to_register()
        game.set_players_to_register(missing - 1)
        missing = game.get_players_to_register()

        print("missing {}".format(missing))

        #game.set_players_to_register(missing - 1)
        #missing -= 1

        if missing > 0:
            print("A registrar!")

            # Función registrar
            #----------------

            controller.show_frame(UsrRegisteredSelection)
        else:
            messagebox.showinfo("PalabrasEncadenadas", "Todos los usuarios han sido registrados!")
            controller.show_frame(OnGame)


class UsrNotRegistered(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de las vistas de ingreso de un usuario no registrado al juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Preparemos el juego!", font=LARGE_FONT)
        title.pack()

        # Form
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20)

        # Name
        name_frame = tk.Frame(form_frame)
        name_frame.pack(pady=10)

        name_lbl = ttk.Label(name_frame, text="Nombre:", width=25)
        name_lbl.pack(side="left")

        name_entry = ttk.Entry(name_frame)
        name_entry.pack(fill="x")

        # Last name
        last_frame = tk.Frame(form_frame)
        last_frame.pack(pady=10)

        last_lbl = ttk.Label(last_frame, text="Apellido:", width=25)
        last_lbl.pack(side="left")

        last_entry = ttk.Entry(last_frame)
        last_entry.pack(fill="x")

        # Username
        username_frame = tk.Frame(form_frame)
        username_frame.pack(pady=10)

        username_lbl = ttk.Label(username_frame, text="Nombre de usuario:", width=25)
        username_lbl.pack(side="left")

        username_entry = ttk.Entry(username_frame)
        username_entry.pack(fill="x")

        # Email
        email_frame = ttk.Frame(form_frame)
        email_frame.pack(pady=10)

        email_lbl = ttk.Label(email_frame, text="Correo electrónico:", width=25)
        email_lbl.pack(side="left")

        email_entry = ttk.Entry(email_frame)
        email_entry.pack(fill="x")


        # Navigation buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=15)

        next_player = ttk.Button(buttons_frame, text="Siguiente", command=lambda: self.verify_next(controller))
        next_player.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda:controller.show_frame(UsrRegisteredSelection))
        return_btn.pack(padx=10)

    def verify_next(self, controller):
        missing = game.get_players_to_register()
        game.set_players_to_register(missing - 1)
        missing = game.get_players_to_register()

        if missing > 0:
            print("A registrar!")
            controller.show_frame(UsrRegisteredSelection)
        else:
            messagebox.showinfo("Palabras Encadenadas", "Todos los usuarios han sido registrados correctamente!")
            controller.show_frame(OnGame)

class MenuData(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de las vistas de menú de selección de visualización de datos del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¿Qué información desea consultar?", font=NORMAL_FONT)
        title.pack(pady=10)

        # Navigation Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=15)

        players = ttk.Button(buttons_frame, text="Jugadores", command=lambda: controller.show_frame(PlayerData))
        players.pack(pady=10)

        themes = ttk.Button(buttons_frame, text="Temas", command=lambda: controller.show_frame(ThemeData))
        themes.pack(pady=15)

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(StartPage))
        return_btn.pack(pady=15)

class ThemeData(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de las vistas de los temas almacenados del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Temas!", font=LARGE_FONT)
        title.pack(pady=10)

        # Input frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=15)

        theme_lbl = ttk.Label(input_frame, text="Seleccione un tema:", width=20)
        theme_lbl.pack(side="left", padx=10)

        theme_combo = ttk.Combobox(input_frame, values=["One", "Two", "Three"])
        theme_combo.pack(fill="x")

        # Text area
        words_frame = tk.Frame(self)
        words_frame.pack(pady=10)

        words_area = tk.Text(words_frame, width=35, height=8)
        words_area.pack(fill="x", ipadx=5, ipady=5)

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        edit_btn = ttk.Button(buttons_frame, text="Editar")
        edit_btn.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(MenuData))
        return_btn.pack(padx=10)

class PlayerData(tk.Frame):
    """
    Clase que crea los elementos del menú de deciciones respecto al registro de usuarios del juego.
    """
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        """
        Constructor de las vistas de los jugadores registrados del juego.
        :param parent: Clase de la que hereda el contenedor.
        :param controller: Clase de la que hereda las funciones de control.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Jugadores!", font=LARGE_FONT)
        title.pack(pady=10)

        # Input
        input_frame = tk.Frame(self)
        input_frame.pack(pady=15)

        player_label = ttk.Label(input_frame, text="Seleccione un jugador:", width=20)
        player_label.pack(side="left")

        player_entry = ttk.Combobox(input_frame, values=["One", "Two", "Three"])
        player_entry.pack(fill="x", padx=10)

        # Text area
        words_frame = tk.Frame(self)
        words_frame.pack(pady=10)

        words_area = tk.Text(words_frame, width=35, height=8)
        words_area.pack(fill="x", ipadx=5, ipady=5)

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        edit_btn = ttk.Button(buttons_frame, text="Editar")
        edit_btn.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(MenuData))
        return_btn.pack(padx=10)

class OnGame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: PalabrasEncadenadas):
        tk.Frame.__init__(self, parent)

        # Variables
        playing = tk.StringVar()
        playing.set(game.get_currently_playing_id())

        # Title
        title = ttk.Label(self, text="Palabras Encadenadas", font=LARGE_FONT)
        title.pack(pady=10)

        # Labels
        # Turn frame
        turn_frame = tk.Frame(self)
        turn_frame.pack(pady=15)

        turn_lbl = ttk.Label(turn_frame,  text="Es el turno de:", width=22)
        turn_lbl.pack(side="left")

        player_lbl = ttk.Label(turn_frame, textvariable=playing)
        player_lbl.pack(fill="x")

        # Themes frame
        theme_frame = tk.Frame(self)
        theme_frame.pack(pady=15)

        theme_lbl = ttk.Label(theme_frame, text="Temas en juego:", width=22)
        theme_lbl.pack(side="left")

        theme_ongame = ttk.Label(theme_frame, text="Temas_en_juego")
        theme_ongame.pack(fill="x")

        # Entry frame
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=25)

        entry_lbl = ttk.Label(entry_frame, text="Ingresa tu palabra:", width=22)
        entry_lbl.pack(side="left")

        entry = ttk.Entry(entry_frame)
        entry.pack(fill="x", padx=10)

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=25)

        validate_btn = ttk.Button(buttons_frame, text="Validar palabra", command=lambda: [self.validate_word(entry.get()),
                                                                                          playing.set(game.get_currently_playing_id())])
        validate_btn.pack(side="left")

        surrender_btn = ttk.Button(buttons_frame, text="Rendirse", command=lambda: [self.print_players(),
                                                                                    self.give_up(controller)])
        surrender_btn.pack(padx=10)

    def print_players(self):
        # print("Active players: {}".format(game.get_active_players()))
        pass

    def give_up(self, controller: PalabrasEncadenadas):
        before_players = sum([1 for el in game.get_players() if el["on_game"] == True])
        new_players = before_players - 1

        if new_players > 1:
            print("Giving up player {}".format(game.get_currently_playing_id()))

            # Set player status to False
            game.give_up_player(game.get_currently_playing_id())
            # --------------------------

            # Change turn

            # -----------

            game.begin_turn(game.get_currently_playing_id())
            controller.show_frame(OnGame)
        else:
            messagebox.showinfo("Palabras Encadenadas", "Finalizando juego...")
            controller.show_frame(ScoreTable)

    def validate_word(self, word: str):
        print("Palabra: {}".format(word))

        # Preparamos la palabra
        word = word.lower().strip()
        points = word_points(word)
        # ---------------------

        # Agregamos el puntaje al jugador
        game.update_score(game.get_currently_playing_id() - 1, points)
        # -------------------------------

        game.begin_turn(game.get_currently_playing_id())



    def refresh_player(self, id: int):
        pass

class ScoreTable(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Fin del juego!", font=LARGE_FONT)
        title.pack(pady=15)

        # Winner
        winner_frame = tk.Frame(self)
        winner_frame.pack(pady=10)

        winner_lbl = ttk.Label(winner_frame, text="Ganador:", width=15)
        winner_lbl.pack(side="left")

        winner_name = ttk.Label(winner_frame, text=game.get_winner())
        winner_name.pack(fill="x")

        # Winner score
        winner_score_frame = tk.Frame(self)
        winner_score_frame.pack(pady=10)

        score_lbl = ttk.Label(winner_score_frame, text="Puntaje", width=15)
        score_lbl.pack(side="left")

        score = ttk.Label(winner_score_frame, text="DEBO CONECTAR")
        score.pack(fill="x")

        # Navigation buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=25)

        see_scores = ttk.Button(buttons_frame, text="Ver puntajes", command=self.see_scores())
        see_scores.pack(side="left")

        finish_game = ttk.Button(buttons_frame, text="Finalizar juego", command=controller.end_game)
        finish_game.pack(padx=10)

    def see_scores(self):
        print("Here are the scores from MongoDB!")


