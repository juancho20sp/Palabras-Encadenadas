import tkinter as tk
from tkinter import ttk, messagebox
from files.game.game import Game
from files.game.points import word_points
from files.db_operations.users import create_user, search_user_by_email, search_user_by_username
from files.db_operations.themes import create_theme, get_themes, check_word, setup_words, add_word_db, words_already_played, is_word_played
from files.db_operations.themes import get_words


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
        """
        Constructor de la clase principal.
        :param args: Lista de argumentos de longitud variable, usado por convención.
        :param kwargs: Lista de argumentos de palabra clave de longitud variable, usado por convención.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        # Icon
        #tk.Tk.iconbitmap(self, default="")

        # Title
        tk.Tk.wm_title(self, "Palabras Encadenadas")

        # Window size
        self.geometry("350x360+550+150")
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
                     ScoreTable, AddTheme, AddWord):
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

        # Variables
        self.themes = get_themes()

        # Title
        title = ttk.Label(self, text="Palabras Encadenadas", font=LARGE_FONT)
        title.pack()

        # Labels and inputs
        # Player input
        players_frame = tk.Frame(self)
        players_frame.pack(pady=15)

        num_players = ttk.Label(players_frame, text="¿Cuántas personas van a jugar?", width=30)
        num_players.pack(side="left")

        self.num_players_spinbox = ttk.Spinbox(players_frame, from_=0, to=10)
        self.num_players_spinbox.pack(fill="x")

        # Test values spinbox
        # save_num_players_btn = ttk.Button(self, text="Guardar jugadores", command=lambda: self.print_players(num_players_spinbox.get()))
        # save_num_players_btn.pack()
        # -------------------

        # Theme
        theme_frame = tk.Frame(self)
        theme_frame.pack(pady=15)

        theme = ttk.Label(theme_frame, text="¿Qué temas van a usar?", width=30)
        theme.pack(side="left")

        self.theme_combo = ttk.Combobox(theme_frame, values=self.themes)
        self.theme_combo.pack(fill="x")

        # Buttons Combobox
        combo_buttons = ttk.Frame(self)
        combo_buttons.pack(pady=10)

        save_theme_btn = ttk.Button(combo_buttons, text="Agregar tema",
                                    command=lambda: [self.add_theme(self.theme_combo.get(), controller)
                                                     ])
        save_theme_btn.pack(side="left")

        refresh_btn = ttk.Button(combo_buttons, text="Refrescar temas", command=self.refresh_themes)
        refresh_btn.pack(padx=10)

        clear_btn = ttk.Button(self, text="Limpiar temas", command=self.clear_themes)
        clear_btn.pack(pady=5)
        # -------------------

        # Selected themes
        selected_frame = ttk.Frame(self)
        selected_frame.pack(pady=10)

        selected_lbl = ttk.Label(selected_frame, text="Temas en juego:", width=30)
        selected_lbl.pack(side="left")

        self.selected = tk.Listbox(selected_frame, height=3, width=22)
        self.selected.pack(fill="x")



        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=20)

        next_btn = ttk.Button(buttons_frame, text="Siguiente", command=lambda:[self.sumbit_all_data(self.num_players_spinbox.get(), self.theme_combo.get(), controller),
                                                                               setup_words(game.get_themes())])


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

    def add_theme(self, theme: str, controller) -> None:
        """
        Esta función imprime el valor seleccionado por el usuario a través del ComboBox de temas.
        :param theme: El tema seleccionado en el Combobox.
        :return: Nada.
        """

        if theme == "Agregar tema":
            messagebox.showinfo("test", "Agregar tema")
            controller.show_frame(AddTheme)
            self.themes = get_themes()
        elif theme == "Todos los temas":
            messagebox.showinfo("test", "TODOS los temas")
            self.selected.delete(0, tk.END)
            self.selected.insert(tk.END, theme)
            game.set_themes(theme)
        else:
            game.set_themes(theme)
            themes = game.get_themes()

            self.selected.delete(0, tk.END)

            for theme in themes:
                self.selected.insert(tk.END, theme)


            messagebox.showinfo("Palabras Encadenadas", "El tema ha sido añadido correctamente.")



        print("The themes are: {}".format(game.get_themes()))

    def refresh_themes(self) -> None:
        """
        Esta función actualiza los temas en el ComboBox.
        :return: Nada
        """
        self.themes = get_themes()
        self.theme_combo['values'] = self.themes

    def sumbit_all_data(self, players: str, theme: str, controller: PalabrasEncadenadas) -> None:
        """
        Esta función valida que todos los campos estén diligenciados y envía los datos a la clase encargada de gestionarlos.
        :param players: Entero correspondiente al número de jugadores ingresado por el usuario.
        :param theme: Tema(s) seleccionado(s) por el usuario.
        :param controller: Clase controladora, 'Palabras Encadenadas'.
        :return: Nada
        """
        if players == "":
            messagebox.showerror("Palabras Encadenadas", "Debe ingresar el número de jugadores.")
            controller.show_frame(GameMode)
        elif (int(players) == 0) or int(players) > 10:
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

    def clear_themes(self) -> None:
        """
        Esta función limpia los temas seleccionados por el usuario.
        :return: Nada
        """
        self.selected.delete(0, tk.END)
        game.clear_themes()
        messagebox.showinfo("Palabras Encadenadas", "Los temas han sido eliminados.")

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


        # DELETE THIS OPTION
        # SKIP TO GAME
        skip = ttk.Button(self, text="Skip registration", command=lambda: [controller.show_frame(OnGame),
                                                                           setup_words(game.get_themes())])
        skip.pack()

        add_word = ttk.Button(self, text="Add word", command=lambda: controller.show_frame(AddWord))
        add_word.pack()
        # ------------------

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

        self.entry = ttk.Entry(input_frame)
        self.entry.pack(fill="x")

        # Navigation buttons frame
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=35)

        next_player = ttk.Button(buttons_frame, text="Siguiente", command=lambda: self.verify_filled(controller))
        next_player.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(UsrRegisteredSelection))
        return_btn.pack(padx=10)

    def verify_filled(self, controller: 'PalabrasEncadenadas') -> None:
        """
        Esta función verifica que los datos hayan sido correctamente diligenciados.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada.
        """
        if self.entry.get() == "":
            messagebox.showerror("Palabras Encadenadas", "Debe ingresar los datos requeridos.")
        else:
            self.check_user(self.entry.get(), controller)

    def check_user(self, email: str, controller: 'PalabrasEncadenadas') -> None:
        """
        Esta función se encarga de revisar el usuario en la base de datos.
        :param email: String ingresado por el usuario, puede corresponder al 'username' o al 'email'.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada
        """
        is_email = True if '@' in email else False

        if is_email:
            response, user = search_user_by_email(email)

            if response == 1:
                # Usuarios pendientes por registrar
                missing = game.get_players_to_register()
                game.set_players_to_register(missing - 1)
                missing = game.get_players_to_register()
                print(missing)

                messagebox.showinfo("Palabras Encadenadas", "Bienvenido!")
                game.set_players_to_register(missing)

                # Limpiamos los entries
                self.entry.delete(0, tk.END)
                # ---------------------

                if missing > 0:
                    print("A registrar!")
                    print(missing)
                    controller.show_frame(UsrRegisteredSelection)
                else:
                    messagebox.showinfo("Palabras Encadenadas", "Todos los usuarios han sido registrados correctamente!")
                    controller.show_frame(OnGame)
            elif response == 2:
                res = messagebox.askyesno("Palabras Encadenadas", "El email no se encontró, ¿desea registrarse?")
                if res:
                    controller.show_frame(UsrNotRegistered)
                else:
                    controller.show_frame(UsrRegisteredSelection)
                self.entry.delete(0, tk.END)
            elif response == 3:
                messagebox.showerror("Palabras Encadenadas", "Email inválido, inténtelo nuevamente.")

                # Limpiamos los entries
                self.entry.delete(0, tk.END)
                # ---------------------

                controller.show_frame(UsrRegistered)

            print("")
            print("")
            print("User {}".format(user))
            print("")
            print("")
        else:
            response, user = search_user_by_username(email)

            if response == 1:
                # Usuarios pendientes por registrar
                missing = game.get_players_to_register()
                game.set_players_to_register(missing - 1)
                missing = game.get_players_to_register()
                print(missing)

                messagebox.showinfo("Palabras Encadenadas", "Bienvenido!")
                game.set_players_to_register(missing)

                # Limpiamos los entries
                self.entry.delete(0, tk.END)
                # ---------------------

                if missing > 0:
                    print("A registrar!")
                    print(missing)
                    controller.show_frame(UsrRegisteredSelection)
                else:
                    messagebox.showinfo("Palabras Encadenadas", "Todos los usuarios han sido registrados correctamente!")
                    controller.show_frame(OnGame)
            elif response == 2:
                res = messagebox.askyesno("Palabras Encadenadas", "El usuario no se encontró, ¿desea registrarse?")
                if res:
                    controller.show_frame(UsrNotRegistered)
                else:
                    controller.show_frame(UsrRegisteredSelection)
                self.entry.delete(0, tk.END)

            print("")
            print("")
            print("User {}".format(user))
            print("")
            print("")

    def verify_next(self, controller: 'PalabrasEncadenadas') -> None:
        """
        Esta función verifica el número de jugadores pendientes por registrar.
        :param controller: Clase controladora, 'PalabrasEncadendas' en este caso.
        :return: Nada
        """
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

        self.name_entry = ttk.Entry(name_frame)
        self.name_entry.pack(fill="x")

        # Last name
        last_frame = tk.Frame(form_frame)
        last_frame.pack(pady=10)

        last_lbl = ttk.Label(last_frame, text="Apellido:", width=25)
        last_lbl.pack(side="left")

        self.last_entry = ttk.Entry(last_frame)
        self.last_entry.pack(fill="x")

        # Username
        username_frame = tk.Frame(form_frame)
        username_frame.pack(pady=10)

        username_lbl = ttk.Label(username_frame, text="Nombre de usuario:", width=25)
        username_lbl.pack(side="left")

        self.username_entry = ttk.Entry(username_frame)
        self.username_entry.pack(fill="x")

        # Email
        email_frame = ttk.Frame(form_frame)
        email_frame.pack(pady=10)

        email_lbl = ttk.Label(email_frame, text="Correo electrónico:", width=25)
        email_lbl.pack(side="left")

        self.email_entry = ttk.Entry(email_frame)
        self.email_entry.pack(fill="x")


        # Navigation buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=15)

        next_player = ttk.Button(buttons_frame, text="Siguiente", command=lambda: [self.verify_filled(self.name_entry.get(), self.last_entry.get(), self.username_entry.get(), self.email_entry.get(), controller),
                                                                                   ])
        next_player.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda:controller.show_frame(UsrRegisteredSelection))
        return_btn.pack(padx=10)

    def verify_filled(self, name, lastname, username, email, controller: 'PalabrasEncadenadas') -> None:
        """
        Esta función verifica que todos los 'entries' estén diligenciados.
        :param name: Valor del entry input correspondiente a dicho campo.
        :param lastname: Valor del entry input correspondiente a dicho campo.
        :param username: Valor del entry input correspondiente a dicho campo.
        :param email: Valor del entry input correspondiente a dicho campo.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada
        """
        all_filled = True

        if name == "":
            all_filled &= False

        if lastname == "":
            all_filled &= False

        if username == "":
            all_filled &= False

        if email == "":
            all_filled &= False

        if all_filled:
            print("Todos los campos llenos")
            self.insert_user(name, lastname, username, email, controller)
        else:
            messagebox.showerror("Palabras Encadenadas", "Todos los campos deben ser diligenciados.")

    def insert_user(self, name, lastname, username, email, controller) -> None:
        """
        Procedimiento que se encarga de pasar los datos a la función encargada de crear los datos del usuario

        :param name: Nombre del usuario.
        :param lastname: Apellido del usuario.
        :param nickname: Username del usuario..
        :param email: Email del usuario
        :return: Nada.
        """
        response = create_user(name, lastname, username, email)

        # Dato correctamente insertado
        if response == 1:
            # Usuarios pendientes por registrar
            missing = game.get_players_to_register()
            game.set_players_to_register(missing - 1)
            missing = game.get_players_to_register()
            print(missing)

            messagebox.showinfo("Palabras Encadenadas", "Usuario creado correctamente!")
            game.set_players_to_register(missing)

            # Limpiamos los entries
            self.name_entry.delete(0, 'end'),
            self.last_entry.delete(0, 'end'),
            self.username_entry.delete(0, 'end'),
            self.email_entry.delete(0, 'end')
            # ---------------------

            if missing > 0:
                print("A registrar!")
                print(missing)
                controller.show_frame(UsrRegisteredSelection)
            else:
                messagebox.showinfo("Palabras Encadenadas", "Todos los usuarios han sido registrados correctamente!")
                controller.show_frame(OnGame)
        elif response == 2:
            messagebox.askretrycancel("Palabras Encadenadas", "Algo ha fallado, inténtalo nuevamente.")
            controller.show_frame(UsrNotRegistered)
        elif response == 3:
            messagebox.showerror("Palabras Encadenadas", "El usuario ya se encuentra registrado.")

            # Limpiamos los entries
            #self.name_entry.delete(0, 'end'),
            #self.last_entry.delete(0, 'end'),
            self.username_entry.delete(0, 'end'),
            self.email_entry.delete(0, 'end')
            # ---------------------

            controller.show_frame(UsrNotRegistered)
        elif response == 4:
            messagebox.showerror("Palabras Encadenadas", "Debe ingresar un email válido.")

            # Limpiamos los entries
            #self.name_entry.delete(0, 'end'),
            #self.last_entry.delete(0, 'end'),
            #self.username_entry.delete(0, 'end'),
            self.email_entry.delete(0, 'end')
            # ---------------------

            controller.show_frame(UsrNotRegistered)

    """def verify_next(self, controller):
        missing = game.get_players_to_register()
        #game.set_players_to_register(missing - 1)
        #missing = game.get_players_to_register()

        if missing > 0:
            print("A registrar!")
            controller.show_frame(UsrRegisteredSelection)
        else:
            messagebox.showinfo("Palabras Encadenadas", "Todos los usuarios han sido registrados correctamente!")
            controller.show_frame(OnGame)"""

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

        self.theme_combo = ttk.Combobox(input_frame)
        self.theme_combo.pack(fill="x")

        # Buttons frame
        refresh_frame = tk.Frame(self)
        refresh_frame.pack(pady=10)

        # Refresh button
        refresh_btn = ttk.Button(refresh_frame, text="Refrescar temas",
                                 command=lambda: [self.refresh_data()])
        refresh_btn.pack(side="left")

        # Show words button
        show_words_btn = ttk.Button(refresh_frame, text="Mostrar palabras",
                                    command=lambda: [self.show_words(self.theme_combo.get())])
        show_words_btn.pack(padx=10)

        # Text area
        words_frame = tk.Frame(self)
        words_frame.pack(pady=10)

        self.words_area = tk.Text(words_frame, width=35, height=8)
        self.words_area.pack(fill="x", ipadx=5, ipady=5)

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack()

        edit_btn = ttk.Button(buttons_frame, text="Editar")
        edit_btn.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: controller.show_frame(MenuData))
        return_btn.pack(padx=10)

    def refresh_data(self) -> None:
        """
        Esta función se encarga de refrescar la información que verá el usuario.
        :param selected_theme: Tema seleccionado en el combobox.
        :return: Nada.
        """
        themes = get_themes()
        themes.remove("Agregar tema")
        themes.remove("Todos los temas")

        # Actualizamos el combo
        self.theme_combo['values'] = themes

    def show_words(self, selected_theme: str) -> None:
        """
        Esta función actualiza las palabras que verá el usuario, de acuerdo al tema seleccionado.
        :param selected_theme: Tema seleccionado en el ComboBox
        :return: Nada.
        """
        # Actualizamos el textarea
        if selected_theme != "":
            self.words_area.delete('1.0', tk.END)
            self.words_area.insert('1.0', get_words(selected_theme))


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
    def __init__(self, parent: 'tk.Frame', controller: PalabrasEncadenadas):
        """
        Constructor de la vista correspondiente a 'OnGame'.
        :param parent: Clase de la que hereda componentes.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        """
        tk.Frame.__init__(self, parent)

        # Variables
        playing = tk.StringVar()
        playing.set(game.get_currently_playing_id())

        #setup_words(game.get_themes())

        #self.show_themes()

        # Title
        title = ttk.Label(self, text="Palabras Encadenadas", font=LARGE_FONT)
        title.pack(pady=10)

        # Labels
        # Turn frame
        turn_frame = tk.Frame(self)
        turn_frame.pack(pady=10)

        turn_lbl = ttk.Label(turn_frame,  text="Es el turno de:", width=22)
        turn_lbl.pack(side="left")

        player_lbl = ttk.Label(turn_frame, textvariable=playing)
        player_lbl.pack(fill="x")

        # Themes frame
        theme_frame = tk.Frame(self)
        theme_frame.pack(pady=15)

        theme_lbl = ttk.Label(theme_frame, text="Temas en juego:", width=22)
        theme_lbl.pack(side="left")

        self.theme_on_game = tk.Listbox(theme_frame, height=3)
        self.theme_on_game.pack(fill="x")

        # DELETE
        button = ttk.Button(theme_frame, text="Refresh", command=lambda: self.show_themes())
        button.pack(pady=5)
        # ------

        # Entry frame
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        entry_lbl = ttk.Label(entry_frame, text="Ingresa tu palabra:", width=22)
        entry_lbl.pack(side="left")

        self.entry = ttk.Entry(entry_frame)
        self.entry.pack(fill="x", padx=10)

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=25)

        validate_btn = ttk.Button(buttons_frame, text="Validar palabra", command=lambda: [self.validate_word(self.entry.get(), controller),
                                                                                          playing.set(game.get_currently_playing_id())])
        validate_btn.pack(side="left")

        surrender_btn = ttk.Button(buttons_frame, text="Rendirse", command=lambda: [self.print_players(),
                                                                                    self.give_up(controller),
                                                                                    playing.set(game.get_currently_playing_id())])
        surrender_btn.pack(padx=10)

    def print_players(self):
        # print("Active players: {}".format(game.get_active_players()))
        pass

    def show_themes(self) -> None:
        """
        Esta función se encarga de mostrar los temas en juego.
        :return: Nada
        """
        self.theme_on_game.delete(0, tk.END)

        themes = game.get_themes()

        if "Todos los temas" in themes:
            new_themes = get_themes()
            new_themes.remove("Todos los temas")
            new_themes.remove("Agregar tema")

            for theme in new_themes:
                self.theme_on_game.insert(tk.END, theme)
        else:
            for theme in themes:
                self.theme_on_game.insert(tk.END, theme)

    def give_up(self, controller: PalabrasEncadenadas) -> None:
        """
        Esta función se encarga de retirar el jugador en turno del juego.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada
        """
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

    def validate_word(self, word: str, controller: PalabrasEncadenadas) -> None:
        """
        Esta función se encarga de validar que la palabra ingresada cumpla con todas las reglas del juego.
        :param word: Palabra ingresada por el usuario.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en en este caso.
        :return: Nada
        """
        print("Palabra: {}".format(word))

        # Preparamos la palabra
        word = word.lower().strip()
        points = word_points(word)
        # ---------------------

        # Agregamos el puntaje al jugador
        game.update_score(game.get_currently_playing_id() - 1, points)
        # -------------------------------


        # Verificamos palabras en BD
        is_used = is_word_played(word)
        if is_used == 1:
            res = check_word(word)

            if res == 1:
                satisfy_rules = self.verify_end_begin_word(word)
                if satisfy_rules == 1:
                    messagebox.showinfo("Palabras Encadenadas", "Muy bien! Has sumado {} puntos".format(points))
                    game.set_last_valid_word(word)
                    words_already_played.append(word.title())
                self.entry.delete(0, tk.END)
            elif res == 2:
                valid = messagebox.askyesno("Palabras Encadenadas", "Esta palabra no está en la base de datos, ¿es válida?")
                if valid:
                    # messagebox.showinfo("Palabras Encadenadas", "Agrega la palabra a la base de datos")
                    game.set_last_word(word)
                    controller.show_frame(AddWord)
                    self.entry.delete(0, tk.END)

                else:
                    messagebox.showerror("Palabras Encadenadas", "Lo sentimos, la palabra no es válida. ¡Gracias por jugar!")
                    game.give_up_player(game.get_currently_playing_id())
        else:
            messagebox.showerror("Palabras Encadenadas", "¡Has perdido! \nLa palabra fue usada anteriormente.")
            game.give_up_player(game.get_currently_playing_id())
        # --------------------------

        game.begin_turn(game.get_currently_playing_id())

        """
        AL CREAR LA VENTANA DE AGREGAR PALABRA A LA BD
        ACTUALIZAR AHÍ MISMO ÚLTIMA PALABRA
        
        """

    def refresh_player(self, id: int):
        pass

    def verify_end_begin_word(self, word: str) -> int:
        """
        Esta función se encarga de revisar si la palabra ingresada inicia por la última letra
        de la última letra jugada.
        :param word: Palabra ingresada por el usuario.
        :return: 1. Si la palabra es válida, 2. Si la palabra es inválida.
        """
        if len(words_already_played) == 0:
            return 1
        else:
            last_word = game.get_last_valid_word()
            last_valid_letter = last_word[-1].title()
            first_letter = word[0].title()

            if last_valid_letter == first_letter:
                return 1
            else:
                game.give_up_player(game.get_currently_playing_id())


        print("last word: {} last letter: {}".format(last_word, last_valid_letter))
        print("entered word: {} first letter: {}".format(word, first_letter))

        return 2

class ScoreTable(tk.Frame):
    def __init__(self, parent, controller: 'PalabrasEncadenadas'):
        """
        Esta clase crea la vista correspondiente a 'ScoreTable'.
        :param parent: Clase de la que hereda componentes.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        """
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

class AddTheme(tk.Frame):
    def __init__(self, parent, controller: 'PalabrasEncadenadas'):
        """
        Constructor de la vista correspondiente a 'AddTheme'.
        :param parent: Clase de la que hereda componentes.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Nuevo tema", font=LARGE_FONT)
        title.pack(pady=15)

        # Name frame
        name_frame = ttk.Frame(self)
        name_frame.pack(pady=10)

        name_lbl = ttk.Label(name_frame, text="Nombre:", width=15)
        name_lbl.pack(side="left")

        self.name_entry = ttk.Entry(name_frame)
        self.name_entry.pack(fill="x")

        # Disclaimer
        disclaimer = ttk.Label(self, text="Ingrese las palabras separadas SOLO por espacios")
        disclaimer.pack()

        # Words frame
        words_frame = ttk.Frame(self)
        words_frame.pack(pady=15)

        words_lbl = ttk.Label(words_frame, text="Palabras:", width=15)
        words_lbl.pack(side="left")

        self.words_entry = tk.Text(words_frame, height=3, width=18)
        self.words_entry.pack()

        # Navigation buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(pady=25)

        save_btn = ttk.Button(buttons_frame, text="Guardar tema", command=lambda:
                                                                            self.save_theme(self.name_entry.get(), self.words_entry.get('1.0', 'end'), controller))
        save_btn.pack(side="left")

        cancel_btn = ttk.Button(buttons_frame, text="Cancelar", command=lambda: controller.show_frame(GameMode))
        cancel_btn.pack(padx=10)

    def save_theme(self, name: str, words: str, controller: 'PalabrasEncadenadas') -> None:
        """
        Esta función llama a la función encargada de almacenar el tema en la base de datos.
        :param name: Nombre del tema.
        :param words: Palabras del tema.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada.
        """
        words = words.split()
        response = create_theme(name, words)

        if response == 1:
            messagebox.showinfo("Palabras Encadenadas", "El tema ha sido creado correctamente!")
            controller.show_frame(GameMode)
        elif response == 2:
            messagebox.showerror("Palabras Encadenadas", "Algo ha fallado, inténtalo nuevamente.")
            controller.show_frame(AddTheme)
        elif response == 3:
            messagebox.showerror("Palabras Encadenadas", "El nombre del tema es inválido.")
            controller.show_frame(AddTheme)
        elif response == 4:
            messagebox.showerror("Palabras Encadenadas", "El tema ya está registrado en el sistema.")
            controller.show_frame(AddTheme)

        self.name_entry.delete(0, tk.END)
        self.words_entry.delete('1.0', tk.END)

        print(get_themes())

class AddWord(tk.Frame):
    def __init__(self, parent, controller: 'PalabrasEncadenadas'):
        """
        Constructor de la clase encargada de crear la vista correspondiente a 'AddWord'.
        :param parent: Clase de la que hereda componentes.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        """
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Agrega la palabra!", font=LARGE_FONT)
        title.pack(pady=15)

        # Theme combo
        theme_frame = ttk.Frame(self)
        theme_frame.pack(pady=10)

        theme_lbl = ttk.Label(theme_frame, text="¿A qué tema pertenece la palabra?", width=32)
        theme_lbl.pack(side="left")

        self.theme_combo = ttk.Combobox(theme_frame,  values=game.get_themes())
        self.theme_combo.pack(fill="x")

        # Refresh button
        refresh_btn = ttk.Button(self, text="Refrescar datos", command=self.refresh_themes)
        refresh_btn.pack(pady=5)

        # Word frame
        word_frame = ttk.Frame(self)
        word_frame.pack(pady=15)

        word_lbl = ttk.Label(word_frame, text="Palabra:", width=32)
        word_lbl.pack(side="left")

        self.word = ttk.Label(word_frame, text=game.get_last_word())
        self.word.pack(fill="x")

        # Navigation buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(pady=20)

        add_btn = ttk.Button(buttons_frame, text="Agregar palabra", command=lambda: [self.add_word(controller)])
        add_btn.pack(side="left")

        return_btn = ttk.Button(buttons_frame, text="Volver", command=lambda: [self.verify_return(controller)])
        return_btn.pack(padx=10)

    def refresh_themes(self) -> None:
        """
        Esta función se encarga de refrescar los temas del ComboBox.
        :return: Nada.
        """
        if "Todos los temas" in game.get_themes():
            all_themes = get_themes()
            all_themes.remove("Agregar tema")
            all_themes.remove("Todos los temas")
            self.theme_combo['values'] = all_themes
        else:
            self.theme_combo.set(game.get_themes()[0])
            self.theme_combo['values'] = game.get_themes()

        self.word['text'] = game.get_last_word().title()

    def verify_return(self, controller: PalabrasEncadenadas) -> None:
        """
        Esta clase se encarga de verificar el deseo del usuario de salir de la ventana.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada.
        """
        res = messagebox.askyesno("Palabras Encadenadas", "¿Seguro desea regresar? \nLos cambios no serán guardados.")

        if res:
            controller.show_frame(OnGame)
        else:
            controller.show_frame(AddWord)

    def add_word(self, controller: PalabrasEncadenadas) -> None:
        """
        Esta función se encarga de hacer la llamada a la función que insertará la nueva palabra en la base de datos.
        :param controller: Clase controladora, 'PalabrasEncadenadas' en este caso.
        :return: Nada.
        """
        if self.theme_combo.get() == "":
            messagebox.showerror("Palabras Encadenadas", "¡Debe escoger un tema!")
        else:
            word = game.get_last_word()
            response = self.verify_end_begin_word(word)

            if response == 1:
                res = add_word_db(word, self.theme_combo.get())
                words_already_played.append(word.title())
                print("RES: {}".format(res))
                if res == 1:
                    messagebox.showinfo("Palabras Encadenadas", "Palabra añadida exitosamente. \n"
                                                                "Has sumado {} puntos".format(word_points(word)))
                    game.set_last_valid_word(word)
                    controller.show_frame(OnGame)
                elif res == 2:
                    controller.show_frame(AddWord)

    def verify_end_begin_word(self, word) -> int:
        """
        Esta función se encarga de revisar si la palabra ingresada inicia por la última letra
        de la última letra jugada.
        :param word: Palabra ingresada por el usuario.
        :return: 1. Si la palabra es válida, 2. Si la palabra es inválida.
        """
        if len(words_already_played) == 0:
            return 1
        else:
            last_word = game.get_last_valid_word()
            last_valid_letter = last_word[-1].title()
            first_letter = word[0].title()

            if last_valid_letter == first_letter:
                return 1
            else:
                game.give_up_player(game.get_currently_playing_id())

