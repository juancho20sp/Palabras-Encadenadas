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
    :return: 1: Usuario insertado correctamente, 2: Problema de inserción, 3: Usuario ya encontrado en la base de datos. 4: Email inválido
    """

    # Verify if data inputs are valid
    valid_user = True
    valid_user &= True if "".join(name.split()).isalpha() and "".join(lastname.split()).isalpha() else False
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
                # ELIMINAR COMENTARIO
                # users.insert_one(user)
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


