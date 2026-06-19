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


def buscar_cancion():
    titulo = str(input("Ingrese la Canción a Buscar: ")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese la Canción a Buscar: ")).strip()

    encontrado = False
    for cancion in canciones_list:
        if cancion["Titulo"] == titulo:
            encontrado = True
            imprimir_cancion(cancion)

    if encontrado == False:
        print("No hay Canciones con ese Titulo.")


# 3.- -Eliminar Canción-


def eliminar_cancion():
    pass


# 4.- -Marcar Como Favorita-


def marcar_favorita():
    pass


# 5.- -Mostrar Canciones-


def mostrar_canciones():
    if len(canciones_list) == 0:
        print("No hay ninguna canción registrada.")
    else:
        for cancion in canciones_list:
            imprimir_cancion(cancion)
