# -Base de Datos-

canciones_list = []

# -Validaciones-


def validar_texto_vacio(texto):
    if len(texto.strip()) == 0:
        print("Error, el texto no puede estar vacio.")
        return False

    return True


def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        print("La canción debe tener una duración de más de 0 segundos.")
        return False


def imprimir_cancion(cancion):

    es_favorita = "Si" if cancion["Favorita"] == True else "No"

    print(f"""
    -------- Canción -------
    |Titulo: {cancion["Titulo"]}
    |Artista: {cancion["Artista"]}
    |Duración:{cancion["Duracion"]} Segundos
    |Favorita: {es_favorita}
    -----------------------""")


# -Transacciones-
