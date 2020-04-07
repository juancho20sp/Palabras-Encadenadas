import tkinter as tk
from tkinter import ttk

# Variables
LARGE_FONT = ("Verdana", 19)
NORMAL_FONT = ("Verdana", 14)

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
        for view in (StartPage, GameMode):
            # Pass the container to the frame
            frame = view(container, self)

            # Add the FULL frame to the dictionary
            self.frames[view] = frame

            # Frame config
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the default window
        self.show_frame(StartPage)

    def show_frame(self, view) -> None:
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
    def __init__(self, parent, controller):
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

        data_btn = ttk.Button(self, text="Ver Datos")
        data_btn.pack()

        exit_btn = ttk.Button(self, text="Salir", command=controller.end_game)
        exit_btn.pack(pady=35)

class GameMode(tk.Frame):
    def __init__(self, parent, controller):
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
        boton = ttk.Button(self, text="Print!", command=lambda: self.print_players(num_players_spinbox.get()))
        boton.pack()
        # -------------------

        # Theme
        theme_frame = tk.Frame(self)
        theme_frame.pack(pady=15)

        theme = ttk.Label(theme_frame, text="¿Qué temas van a usar?", width=30)
        theme.pack(side="left")

        theme_combo = ttk.Combobox(theme_frame, values=["One", "Two", "Three"])
        theme_combo.pack(fill="x")

        # Theme test combobox
        btn2 = ttk.Button(self, text="print", command=lambda:self.print_theme(theme_combo.get()))
        btn2.pack()
        # -------------------

        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=20)

        next_btn = ttk.Button(buttons_frame, text="Siguiente")
        next_btn.pack(side="left")
        back_btn = ttk.Button(buttons_frame, text="Atrás", command=lambda:controller.show_frame(StartPage))
        back_btn.pack(padx=15)

    def print_players(self, num):
        """
        Esta función imprime el número de jugadores ingresado por el usuario a través del Spinbox.
        :param num: Valor seleccionado en el Spinbox.
        :return: Nada.
        """
        print(num)

    def print_theme(self, theme):
        """
        Esta función imprime el valor seleccionado por el usuario a través del ComboBox de temas.
        :param theme: El tema seleccionado en el Combobox.
        :return: Nada.
        """
        print(theme)

class UsrRegisteredSelection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title
        title = ttk.Label(self, text="¡Preparemos el juego!", font=LARGE_FONT)
        title.pack

class UsrRegistered(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, controller)

class UsrNotRegistered(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, controller)

class MenuData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, controller)

class ThemeData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, controller)

class PlayerData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, controller)
