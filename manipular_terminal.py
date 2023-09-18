import os
import readchar

numero = 1


#funcion limpiar terminal
def limpiar():
  
  os.system('cls' if os.name == 'nt' else 'clear')
  print(numero)

#funcion leer tecla 
def leer_tecla():
  global numero
  
  tecla = readchar.readkey()
  if tecla == "n":
    numero += 1
    return
  else:
    return tecla


while True:
  
  limpiar()

  # Leer la tecla
  tecla = leer_tecla()

  # Si la tecla es "n", incrementa el contador.
  if tecla == "n":
    print(numero)
  # Si el contador es igual a 50, termina el programa.
  if numero == 51:
    print('Fin del programa.')
    break