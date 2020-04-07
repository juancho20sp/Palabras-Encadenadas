from files.db_operations.connection import users
from files.data_operations.verifications import validate_email

def create_user(name: str, lastname: str, username: str, email: str) -> None:
    """
    This is the function that creates and inserts a new user into the DataBase.

    :param name: Name of the user.
    :param lastname: Last name of the user.
    :param nickname: Nickname of the user.
    :param email: Email of the user.
    :return: Nothing
    """

    # Verify if data inputs are valid
    valid_user = True
    valid_user &= True if "".join(name.split()).isalpha() and "".join(lastname.split()).isalpha() else False
    valid_user &= validate_email(email)

    usernames = list(users.find({'username': username}))
    emails = list(users.find({'email': email}))

    valid_user &= True if len(usernames) == 0 else False
    valid_user &= True if len(emails) == 0 else False

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
        except:
            print("Hemos tenido un problema, inténtalo nuevamente!")

    else:
        print("Lo sentimos, el nombre de usuario o el email ya se encuentra en nuestra base de datos.")

