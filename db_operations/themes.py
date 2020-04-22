from db_operations.connection import dictionary

# Variables
words_on_game = []
words_already_played = []

def create_theme(name: str, words: list) -> int:
    """
    Esta es la función encargada de crear un nuevo tema en el juego.
    :param name: Nombre del tema.
    :param words: Palabras incluídas en el tema.
    :return: 1. Creado correctamente, 2. Problema de inserción, 3. Nombre inválido, 4.Tema ya creado
    """
    valid_theme = True
    valid_theme &= True if "".join(name.strip().split()).isalpha() and len(name) > 1 else False

    theme_names = list(dictionary.find({'name': name.strip().title()}))

    valid_theme &= True if len(theme_names) == 0 else False

    # Verificamos las palabras ingresadas
    valid_words = []

    for word in words:
        valid = True
        valid &= True if word.strip().isalpha() else False
        valid &= True if len(word) > 1 else False

        if valid:
            ready_word = word.strip().title()
            valid_words.append(ready_word)

    if len(theme_names) == 0:
        if valid_theme:
            theme = {
                'name': name.strip().title(),
                'words': valid_words,
                'times_used': 0
            }

            try:
                dictionary.insert_one(theme)
                return 1
            except:
                return 2
        else:
            return 3
    else:
        return 4


def get_themes() -> list:
    """
    Esta función trae todos los temas de la base de datos.
    :return: Una lista con los nombres de cada tema.
    """
    themes = ['Agregar tema', 'Todos los temas']
    all_themes = list(dictionary.find())

    for theme in all_themes:
        themes.append(theme['name'])

    return themes


def setup_words(themes: list) -> None:
    """
    Esta función se encarga de crear un arreglo de forma local con todas las palabras
    traídas de la base de datos correspondientes a los temas activos del juego actual.
    :param themes: Una lista con los nombres de los temas en juego.
    :return: Nada
    """
    if "Todos los temas" in themes:
        all_themes = list(dictionary.find())
        for theme in all_themes:
            for word in theme['words']:
                words_on_game.append(word)
    else:
        db_themes = list(dictionary.find())
        for theme in db_themes:
            if theme['name'] in themes:
                for word in theme['words']:
                    words_on_game.append(word)


def check_word(word: str) -> int:
    """
    Verifica si la palabra recibida está dentro de las palabras jugadas.
    :param word: Palabra ingresada por el usuario.
    :return: 1. Palabra ya jugada, 2. Palabra no jugada.
    """
    if word.title() in words_on_game:
        return 1
    else:
        return 2


def is_word_played(word: str) -> int:
    """
    Esta función recibe una palabra y verifica si dicha palabra ya fue usada en el juego.
    :param word: Palabra ingresada por el jugador
    :return: 1. Palabra no usada, 2. Palabra usada.
    """
    if word.title() in words_already_played:
        return 2
    else:
        return 1


def add_word_db(word: str, theme: str) -> int:
    """
    Esta función añade la palabra a la base de datos del tema ingresado.
    :param word: Palabra ingresada por el usuario.
    :param theme: Tema elegido por el usuario.
    :return: 1. Inserción exitosa, 2. Inserción fallida.
    """


    db_theme = list(dictionary.find({'name': theme}))[0]
    previous_length = len(db_theme['words'])

    word = word.title()
    dictionary.update(
        {'name': theme},
        {'$push': {'words': word}}
    )

    db_theme = list(dictionary.find({'name': theme}))[0]
    after_length = len(db_theme['words'])

    if after_length == (previous_length + 1):
        return 1
    return 2


def get_words(theme: str) -> list:
    """
    Esta función buscará en la base de datos el tema que recibe por parámetro
    y devuelve una lista con las palabras encontradas.
    :param theme: Nombre del tema a buscar.
    :return: Lista con las palabras encontradas.
    """
    my_theme = list(dictionary.find({'name': theme}))[0]

    return my_theme['words']


def update_word_db(prev_word: str, after_word: str, theme:str) -> int:
    """
    Esta función se encargará de modificar la palabra dada en la base de datos.
    :param prev_word: Palabra seleccionada de la base de datos por el usuario.
    :param after_word: Palabra editada y válida que se ingresará a la base de datos reemplazando el valor de prev_word.
    :param theme: Tema que contiene la palabra que se va a editar.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """


    try:
        dictionary.update(
            {'name': theme, 'words': prev_word},
            {'$set': {'words.$': after_word}}
        )
        return 1
    except:
        return 2


def delete_word_db(word: str, theme: str) -> int:
    """
    Esta función se encarga de eliminar una palabra de la base de datos.
    :param word: Palabra a eliminar.
    :param theme: Tema del que será eliminada la palabra.
    :return: 1. Transacción exitosa, 2. Transacción fallida.
    """

    try:
        dictionary.update(
            {'name': theme},
            {'$pull': {'words': word}}
        )
        return 1
    except:
        return 2









