from views.views import PalabrasEncadenadas
from db_operations.users import end_all_games, end_all_turns, reset_all_actual_points
from db_operations.connection import close_connection


def main() -> None:
    game = PalabrasEncadenadas()
    game.mainloop()

    # Operaciones en la base de datos
    end_all_games()
    end_all_turns()
    close_connection()


main()
