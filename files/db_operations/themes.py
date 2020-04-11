from files.db_operations.connection import dict

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

    theme_names = list(dict.find({'name': name.strip().title()}))

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
            print(theme)
            try:
                dict.insert_one(theme)
                print("Tema creado correctamente")
                return 1
            except:
                print("Hemos tenido un problema, inténtalo nuevamente!")
                return 2
        else:
            print("Nombre de tema inválido")
            return 3
    else:
        print("Tema ya creado")
        return 4

def get_themes() -> list:
    themes = ['Agregar tema', 'Todos los temas']
    all_themes = list(dict.find())

    for theme in all_themes:
        themes.append(theme['name'])

    return themes

def setup_words(themes: list) -> int:
    if "Todos los temas" in themes:
        all_themes = list(dict.find())
        for theme in all_themes:
            for word in theme['words']:
                words_on_game.append(word)
    else:
        db_themes = list(dict.find())
        for theme in db_themes:
            if theme['name'] in themes:
                for word in theme['words']:
                    words_on_game.append(word)

    print("WORDS ON GAME:")
    print(words_on_game)
    print("")

def check_word(word: str) -> int:
    """
    Verifica si la palabra recibida está dentro de las palabras jugadas.
    :param word: Palabra ingresada por el usuario.
    :return: 1. Palabra ya jugada, 2. Palabra no jugada.
    """
    if word.title() in words_on_game:
        print("PALABRA EN JUEGO: {}".format(word.title()))
        return 1
    else:
        print("PALABRA NO JUGADA: {}".format(word.title()))
        return 2

def is_word_played(word: str) -> int:
    """
    Esta función recibe una palabra y verifica si dicha palabra ya fue usada en el juego.
    :param word: Palabra ingresada por el jugador
    :return: 1. Palabra no usada, 2. Palabra usada.
    """
    if word.title() in words_already_played:
        print("")
        print("")
        print("Already played:")
        print(words_already_played)
        print("")
        print("")
        return 2
    else:
        print("")
        print("")
        print("Already played:")
        print(words_already_played)
        print("")
        print("")
        return 1




def add_word(word: str, theme: str) -> int:
    print("Palabra: {}".format(word))
    print("Tema: {}".format(theme))


    db_theme = list(dict.find({'name': theme}))[0]
    previous_length = len(db_theme['words'])

    print("Previous length: {}".format(previous_length))
    print("DB THEME: {}".format(db_theme))

    word = word.title()
    dict.update(
        {'name': theme},
        {'$push': {'words': word}}
    )

    db_theme = list(dict.find({'name': theme}))[0]
    print(db_theme)



