"""
Hello from database_feature
"""

from files.db_operations.connection import users
from files.data_operations.verifications import validate_email

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
                'games_played': 0,
                'games_won': 0,
                'actual_points': 0,
                'total_points': 0
            }

            try:
                users.insert_one(user)
                print("Usuario creado satisfactoriamente!")
                return 1
            except:
                print("Hemos tenido un problema, inténtalo nuevamente!")
                return 2

        else:
            print("Lo sentimos, el nombre de usuario o el email ya se encuentra en nuestra base de datos.")
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
            return 2
    return 3

def search_user_by_username(username: str) -> tuple:
    """
    Esta función busca el username en la base de datos.
    :param email: String con el username ingresado por el usuario.
    :return: (1. El username se encontró, 2. El username no está en la BD, diccionario con el usuario (si lo hay))
    """
    usernames = list(users.find({'username': username}))

    if len(usernames) == 1:
        return 1, usernames[0]
    return 2

def get_user_db(data: str) -> dict:
    data = data.lower().strip()
    if '@' in data:
        print("ITS AN EMAIL")
        user = list(users.find({'email': data}))[0]
    else:
        print("its an username")






