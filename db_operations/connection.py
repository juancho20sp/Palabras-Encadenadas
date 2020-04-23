from pymongo import MongoClient


# Connection to the MongoDB server

# MongoDB on cloud
#client = MongoClient("mongodb+srv://admin:admin@101-dtcph.mongodb.net/test?retryWrites=true&w=majority")

# MongoDB on docker
client = MongoClient("mongodb://localhost:27017/")

# Connection to the database
collections = client['palabras_encadenadas']

# Instances of the collections we are going to use
users = collections['users']
dictionary = collections['dictionaries']
games = collections['games']


def close_connection() -> None:
    """
    Esta función se encarga de cerrar la conexión con la base de datos.
    :return: Nada.
    """
    client.close()

