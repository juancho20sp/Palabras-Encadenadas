
def word_points(word: str) -> int:
    """
    Esta función retorna los puntos obtenidos al ingresar una palabra.

    :param word: Palabra a verificar, en minúsculas
    :return: La cantidad de puntos adquiridos por ingresar la palabra
    """
    # Vocales: 1
    # Consonantes : 2
    # Ñ: 5

    points = 0
    vowels = ['a','e','i','o','u','á','é','í','ó','ú']
    splitted = list(word)

    for letter in splitted:
        if letter in vowels:
            points += 1
        elif letter == 'ñ':
            points += 5
        else:
            points += 2

    print("Puntaje: {}".format(points))

    return points