import os
import readchar
import random
import time


class Game:# Clase juego
    def __init__(self, filename):# constructor de Game
        self.WALL = "#"
        self.PATH = "."
        self.PLAYER = "P"
        self.px = 0
        self.py = 0
        self.maze, self.width, self.height, self.px, self.py = self.load_maze(filename)
        self.GOAL = (self.width , self.height)
        
    def start(self):# Funcion de inicio
        while True:# Bucle hasta ingresar nombre
            player = input("Cual es tu nombre: ")
            if player:# Condicion para que el usuario ingrese nombre
                break
        print(f'Hola {player}, preparate para la aventura.')
        print("\nINSTRUCCIONES:")
        print("\tUsa las flechas para moverte, q para salir")
        time.sleep(3)# Espera de 3 segundos
        
    def load_maze(self, filename):# Funcion carga el mapa y leer alto y ancho
        with open(filename, "r") as f:
            px, py, width, height = map(int, f.readline().strip().split())# Lee las coordenadas y dimensiones del laberinto desde la primera línea
            maze = list(map(list, map(str.strip, f.readlines())))# Carga el laberinto en una lista de listas
                        
        return maze, width, height, px, py

    def print_maze(self):# Imprime el mapa
        for row in self.maze:
            print(" ". join(row))# Convierte cada fila del laberinto en una cadena, uniendo los elementos con un espacio
    
    def get_goal_position(self):# Ubicacion de la meta
        return self.GOAL
    
    def get_map_data(self):# Obtiene los datos del mapa
        map_data = ""
        for row in self.maze:
            map_data += "".join(row) + "\n"# Convierte cada fila del laberinto en una cadena y agrega un salto de línea al final

        return map_data.strip()
    
    def get_dimensions(self): # Optener las dimensiones
        return self.width, self.height
                  
    def place_player(self, x, y, dx, dy):# Coloca al jugador en una nueva posición
        maze_width = self.width + 1
        maze_height = self.height + 1
        
        if x + dx < 0 or x + dx >= maze_width or y + dy < 0 or y + dy >= maze_height:# Verifica si la nueva posición está fuera de los límites del laberinto
            return
        
        if (x + dx, y + dy) == self.get_goal_position():# Verifica si la nueva posición es la meta (posición final del laberinto)
            print("\n\n\t\tG A N A S T E\n\n")
            exit()# Sale del programa
        
        if self.maze[y + dy][x + dx] == self.PATH:# Verifica si la nueva posición es un camino libre en el laberinto
            self.maze[y][x] = self.PATH# Restaura la posición anterior del jugador a un camino libre
            self.maze[y + dy][x + dx] = self.PLAYER# Coloca al jugador en la nueva posición
            self.px = x + dx# Actualiza la coordenada x del jugador
            self.py = y + dy# Actualiza la coordenada y del jugador
        
    def run(self):# Funcion principal que ejecuta el juego
        self.start()# Pide el nombre del jugador y imprime las instrucciones
        while True:# Bucle principal del juego
            os.system('cls' if os.name == 'nt' else 'clear')# Limpia la consola
            
            self.print_maze()# Imprime el estado actual del laberinto
            
            print(f"Jugador: ({self.px}, {self.py})")# Muestra la posición actual del jugador
            goal_position = self.get_goal_position()
            print(f"Meta: ({goal_position})") # Muestra la posición de la meta
            
            width, height = self.get_dimensions()
            print(f"Ancho: {width}, Alto: {height}")# Muestra las dimensiones del laberinto
            key = readchar.readkey()# Lee la tecla presionada por el jugador

            if key == "q":# Si el jugador presiona 'q', sale del bucle y termina el juego
                break
            elif key.lower() == "a" or key == readchar.key.LEFT:# Si el jugador presiona 'a' o la flecha izquierda, mueve al jugador a la izquierda
                self.place_player(self.px, self.py, -1, 0)
            elif key.lower() == "s" or key == readchar.key.DOWN:# Si el jugador presiona 's' o la flecha abajo, mueve al jugador hacia abajo
                self.place_player(self.px, self.py, 0, 1)
            elif key.lower() == "d" or key == readchar.key.RIGHT:# Si el jugador presiona 'd' o la flecha derecha, mueve al jugador a la derecha
                self.place_player(self.px, self.py, 1, 0)
            elif key.lower() == "w" or key == readchar.key.UP:# Si el jugador presiona 'w' o la flecha arriba, mueve al jugador hacia arriba
                self.place_player(self.px, self.py, 0, -1)

class GameFiles(Game):# Clase GameFiles que hereda de la clase base Game
    def __init__(self, filenames):
        selected_filename = random.choice(filenames)# Selecciona aleatoriamente un archivo de la lista de nombres de archivos
        super().__init__(selected_filename)# Llama al constructor de la clase base Game con el archivo seleccionado como argumento
        
def main():
    game = GameFiles(["map1.txt", "map2.txt"])# Crea una instancia de la clase GameFiles con una lista de nombres de archivos
    game.run()# Ejecuta el juego utilizando el método run() de la clase GameFiles

if __name__ == "__main__":
    main()
