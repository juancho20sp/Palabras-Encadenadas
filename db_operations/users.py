"""
Hello from database_feature
"""

from db_operations.connection import users
from data_operations.verifications import validate_email

def create_user(name: str, lastname: str, username: str, email: str) -> int:
    """
    Esta es la función que crea y almacena un usuario nuevo en la base de datos.

    :param name: Nombre del usuario.
    :param lastname: Apellido del usuario.
    :param nickname: Username del usuario..
    :param email: Email del usuario.
    :return: 1: Usuario insertado correctamente, 2: Problema de inserción, 3: Usuario ya encontrado en la base de datos, 4: Email inválido
    """

    # Verify if data inputs are valid
    valid_user = True
    valid_user &= True if "".join(name.strip().split()).isalpha() and "".join(lastname.strip().split()).isalpha() else False
    valid_user &= validate_email(email)

    usernames = list(users.find({'username': username}))
    emails = list(users.find({'email': email}))

    valid_user &= True if len(usernames) == 0 else False
    valid_user &= True if len(emails) == 0 else False

    if validate_email(email):
        if valid_user:
            user = {
                'name': name.title(),
                'lastname': lastname.title(),
                'username': username,
                'email': email,
                'is_on_game': False,
                'is_on_turn': False,
                'games_played': 0,
                'games_won': 0,
                'actual_points': 0,
                'total_points': 0
            }

            try:
                users.insert_one(user)
                return 1
            except:
                return 2

        else:
            return 3
    else:
        return 4


def search_user_by_email(email: str) -> tuple:
    """
    Esta función busca el email en la base de datos.
    :param email: String con el email ingresado por el usuario.
    :return: (1. El email se encontró, 2. El email no está en la BD, 3. Email inválido, diccionario con el usuario (si lo hay))
    """
    if validate_email(email):
        emails = list(users.find({'email': email}))

        if len(emails) == 1:
            return 1, emails[0]
        else:
            return 2, None
    return 3, None


def search_user_by_username(username: str) -> tuple:
    """
    Esta función busca el username en la base de datos.
    :param email: String con el username ingresado por el usuario.
    :return: (1. El username se encontró, 2. El username no está en la BD, diccionario con el usuario (si lo hay))
    """
    usernames = list(users.find({'username': username}))

    if len(usernames) == 1:
        return 1, usernames[0]
    return 2, None


def get_user(key: str) -> dict:
    """
    Esta función retorna un usuario de acuerdo al parámetro recibido.
    :param key: Email o username del usuario.
    :return: Diccionario con los datos del usuario.
    """
    if '@' in key:
        my_user = list(users.find({'email': key}))[0]
        return my_user
    else:
        my_user = list(users.find({'username': key}))[0]
        return my_user


def start_game_to_user(player: dict) -> dict:
    """
    Esta función se encarga de poner la casilla is_on_game en True.
    :param player: Diccionario con los datos del jugador.
    :return: El diccionario actualizado
    """

    users.update(
        {'username' : player['username']},
        {'$set': {'is_on_game': True}}
    )

    refresh_user = list(users.find({'username': player['username']}))[0]

    return refresh_user


def begin_turn(player: dict) -> int:
    """
    Está función inicia el turno del jugador recibido
    :param player: Diccionario con los datos del jugador.
    :return: 1. Si la transacción se realizó correctamente, 2. Si la transacción falló.
    """

    username = player['username']

    users.update(
        {'username': username},
        {'$set': {'is_on_turn': True}}
    )
    refresh_user = list(users.find({'username': player['username']}))[0]
    return refresh_user


def end_turn(player: dict) -> int:
    """
    Esta función termina el turno del jugador recibido.
    :param player: Diccionario con los datos del jugador.
    :return: 1. Si la transacción fue exitosa, 2. Si la transacción falló.
    """

    username = player['username']

    users.update(
        {'username': username},
        {'$set': {'is_on_turn': False}}
    )

    refresh_user = list(users.find({'username': player['username']}))[0]

    return refresh_user


def end_all_games():
    players = list(users.find({'is_on_game': True}))
    for player in players:
        users.update(
            {'username': player['username']},
            {'$set': {'is_on_game': False}}
        )

    players_points = list(users.find({'actual_points': {'$gt': 0}}))
    for player in players_points:
        reset_actual_points_db(player['_id'])


def end_all_turns():
    """
    Esta función se encarga de terminar todos los turnos de los jugadores activos.
    :return: Nada
    """
    active_players = list(users.find({'is_on_turn': True}))
    for player in active_players:
        users.update(
            {'username': player['username']},
            {'$set': {'is_on_turn': False}}
        )


def get_active_players_db():
    """
    Esta función trae los usuarios con partida activa de la BD.
    :return: Lista con los jugadores.
    """
    users_db = list(users.find({'is_on_game': True}))
    return users_db


def is_on_game_db(player: dict) -> bool:
    """
    Esta función verifica si el jugador está en juego.
    :param player: Diccionario con los datos del jugador.
    :return: True si está en juego, False de lo contrario.
    """
    my_player = list(users.find({'username': player['username']}))[0]

    if my_player['is_on_game']:
        return True
    return False


def is_on_turn_db(player: dict) -> bool:
    """
    Esta función verifica si el jugador está en turno juego.
    :param player: Diccionario con los datos del jugador.
    :return: True si está en turno, False de lo contrario.
    """
    my_player = list(users.find({'username': player['username']}))[0]

    if my_player['is_on_turn']:
        return True
    return False


def get_all_users() -> list:
    """
    Esta función trae todos los jugadores de la base de datos.
    :return: Lista trae los diccionarios correspondientes a cada jugador.
    """
    players = list(users.find())
    return players


def update_player(username: str, name: str, lastname: str) -> int:
    """
    Esta función se encarga de modificar el nombre y apellido del usuario especificado
    en la base de datos.
    :param username: String con el username por el que se identificará el usuario a modificar.
    :param name: Nombre que será actualizado en la base de datos.
    :param lastname: Apellido que será actualizado en la base de datos.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """
    try:
        users.update(
            {'username': username},
            {'$set': {'name': name, 'lastname': lastname}}
        )
        return 1
    except:
        return 2


def delete_user_db(username: str) -> int:
    """
    Esta función se encarga de eliminar el registro del usuario en la base de datos.
    :param username: Username usado para encontrar al usuario en la base de datos.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """
    try:
        users.remove({'username': username})
        return 1
    except:
        return 2


def add_points_db(id: str, points: int) -> int:
    """
    Esta función se encarga de sumar los puntos al jugador, usando su ObjectID como localizador.
    :param id: ObjectID del jugador en cuestión.
    :param points: Puntos a sumar al usuario.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """

    try:
        users.update(
            {'_id': id},
            {'$inc': {'actual_points': points}}
        )
        return 1
    except:
        return 2


def reset_actual_points_db(user_id: str) -> int:
    """
    Esta función se encarga de agregar los 'puntos actuales' a los 'puntos totales'
    y re-establecer los puntos actuales a 0.
    :param user_id: Atributo por el que localizaremos al usuario en la base de datos.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """
    my_user = list(users.find({'_id': user_id}))[0]

    # Obtenemos el total de puntos
    actual_points = my_user['actual_points']

    # Los sumamos a los puntos totales en la base de datos
    try:
        users.update(
            {'_id': user_id},
            {'$inc': {'total_points': actual_points}}
        )
    except:
        print("Algo ha fallado!")

    # Reseteamos los puntos actuales
    try:
        users.update(
            {'_id': user_id},
            {'$set': {'actual_points': 0}}
        )
    except:
        print("Algo ha fallado reseteando!")


def reset_all_actual_points() -> None:
    active = list(users.find({'is_on_game': True}))

    for user in active:
        reset_actual_points_db(user['_id'])


def get_winners() -> list:
    """
    Esta función trae todos los puntajes actuales de los jugadores.
    :return: Lista con el o los jugadores con mayor puntaje actual.
    """
    scores = []

    my_users = list(users.find({'actual_points': {'$gt': 0}}))

    for user in my_users:
        scores.append(user['actual_points'])

    if len(my_users) != 0:
        max_score = max(scores)

        winners = list(users.find({'actual_points': max_score}))

        for winner in winners:
            update_times_won(winner['_id'])

        return winners
    else:
        return ["Empate!"]


def update_times_played(user_data: str) -> None:
    """
    Esta función se encarga de sumarle 1 a las veces que cada jugador ha entrado al juego.
    :param user_data: Información con la que localizaremos al usuario, puede ser un email o un username.
    :return: Nada.
    """
    if '@' in user_data:
        users.update(
            {'email': user_data['email']},
            {'$inc': {'games_played': 1}}
        )
    else:
        users.update(
            {'username': user_data['username']},
            {'$inc': {'games_played': 1}}
        )


def update_times_won(user_id: str) -> None:
    """
    Esta función actualiza las veces que ha ganado un jugador.
    :param user_id: ObjectID con el que se identifica el usuario.
    :return: Nada.
    """

    users.update(
        {'_id': user_id},
        {'$inc': {'games_won': 1}}
    )










