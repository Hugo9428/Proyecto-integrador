import readchar

# Bucle principal
while True:
    # Leer la tecla
    tecla = readchar.readkey()

    # Imprimir la tecla
    print(tecla)

    # Si se presionó la tecla UP, salir del bucle
    if tecla == "UP":
        break