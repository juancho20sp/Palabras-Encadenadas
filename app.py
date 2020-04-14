
# Se escoge un tema
# Cada usuario dice una palabra
# El juego arranca -> El programa dice cualquier palabra
# el primer jugador debe decir una palabra que inicie con la última letra de la palabra del programa

# Se pierde si:
# Se repite palabra.
# Si palabra no es del tema.
# Si la palabra no sigue las normas de las palabras.
# El jugador se rinde

# Modos de juego:
# Un solo tema.
# Varios temas.
# Incluyendo las palabras de todos los temas.

# Decidir ganador:
# Cuando solo queda un jugador.
# Se suman los puntos de las palabras que dijo cada jugador:
# Vocales: 1 punto
# Consonantes: 2 puntos
# ñ: 5 puntos

# Máx 10 jugadores
# ¿La palabra existe? -> ya en la base de datos del sistema
# ¿No existe? -> Preguntar si es válida
# Si es válida -> Agregar para nuevos juegos
# No es válida -> Terminar juego


# Classes
from views.views import PalabrasEncadenadas
from db_operations.users import end_all_games, end_all_turns
from db_operations.connection import close_connection

def main() -> None:
    game = PalabrasEncadenadas()
    game.mainloop()

    # Operaciones en la base de datos
    end_all_games()
    end_all_turns()
    close_connection()

main()
