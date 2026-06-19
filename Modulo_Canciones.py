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

# 1.- Agregar Canción-


def agregar_cancion():
    titulo = str(input("Ingrese el Titulo de la Canción: ")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese el Titulo de la Canción: ")).strip()

    artista = str(input("Ingrese nombre del Artista: ")).strip()
    while not validar_texto_vacio(artista):
        artista = str(input("Ingrese nombre del Artista: ")).strip()

    while True:
        try:
            duracion = int(input("Ingrese la Duración de la Canción: "))
            while not validar_duracion(duracion):
                duracion = int(input("Ingrese la Duración de la Canción: "))
            break
        except:
            print("Error, debe ingresar un Número.")

    cancion = {
        "Titulo": titulo,
        "Artista": artista,
        "Duración": duracion,
        "Favorita": False,
    }

    canciones_list.append(cancion)
    print("- Registro Almacenado Correctamente. -")


# 2.- -Buscar Canción-

# 3.- -Eliminar Canción-

# 4.- -Marcar Como Favorita-

# 5.- -Mostrar Canciones-
