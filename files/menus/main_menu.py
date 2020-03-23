"""
Menú principal:

1. Agregar jugadores --
2. Escoger tema --
3. Seleccionar modo de juego --
4. Iniciar Juego
5. Volver

"""
from data.data import sep, title, main_menu
from menus.menu_players import setup as menu_players
from menus.menu_mode import setup as menu_mode
from menus.menu_topic import setup as menu_topic

def setup() -> None:
    """
    Simple function that displays the main menu of the game.
    :return:
    """
    line()

    print(title)
    print(main_menu)
    line()
    select()

def select() -> None:
    """
    Function used as input for navigating the main menu.
    :return:

    """
    while True:
        try:
            option = int(input("Ingrese el número de la acción que desea ejecutar: "))
            if option >= 1 and option <= 5: # Verify if the number is in the right range

                # Create some space for the next console
                for i in range(50):
                    print()

                # Print the new console
                navigate(option)
                break
            else:
                print("Número inválido, intentelo nuevamente.")
        except:
            print("Número inválido, intentelo nuevamente.")

def navigate(option) -> None:
    if option == 1:
        while True:
            menu_players()
    if option == 2:
        menu_topic()
    if option == 3:
        menu_mode()
    if option == 1:
        pass
    if option == 1:
        pass


def line() -> None:
    print(sep)