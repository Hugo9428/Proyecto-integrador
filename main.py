import readchar
import os
import random
import time

WALL = "#"
PATH = "."
PLAYER = "P"

class Game:
    def __init__(self, maze_filenames):
        self.maze_filenames = maze_filenames
        self.maze = None
        self.px = 0
        self.py = 0

    def start(self):
        while True:
            player = input("Cual es tu nombre: ")
            if player:
                break
        print(f'Hola {player}, preparate para la aventura.')
        print("\nINSTRUCCIONES:")
        print("\tUsa las flechas para moverte, q para salir")
        time.sleep(3)

    def place_player(self, x, y, dx, dy):
        maze_width = len(self.maze[0])
        maze_height = len(self.maze)

        if x + dx < 0 or x + dx >= maze_width or y + dy < 0 or y + dy >= maze_height:
            return

        if y + dy == maze_height - 1 and x + dx == maze_width - 1:
            print("\n\n\t\tG A N A S T E\n\n")
            exit()

        if self.maze[y + dy][x + dx] == PATH:
            self.maze[y][x] = PATH
            self.maze[y + dy][x + dx] = PLAYER
            self.px = x + dx
            self.py = y + dy

class FileGame(Game):
    def __init__(self, path_map):
        super().__init__(path_map)
        self.map_data = None

    def load_maze(self):
        with open(random.choice(self.maze_filenames), "r") as f:
            self.maze = list(map(lambda x: list(x), f.read().splitlines()))

    def print_maze(self):
        for row in self.maze:
            print(" ".join(row))
    
    def get_map_data(self):
        map_data = ""
        for row in self.maze:
            map_data += "".join(row) + "\n"

        map_data += f"Inicio: ({self.px}, {self.py})\n"
        map_data += f"Fin: ({len(self.maze[0]) - 1}, {len(self.maze) - 1})"

        self.map_data = map_data.strip()
        return self.map_data

    def run(self):
        self.start()
        self.load_maze()
        self.place_player(self.px, self.py, 0, 0)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_maze()
            key = readchar.readkey()
            if key == "q":
                break
            elif key.lower() == "a" or key == readchar.key.LEFT:
                self.place_player(self.px, self.py, -1, 0)
            elif key.lower() == "s" or key == readchar.key.DOWN:
                self.place_player(self.px, self.py, 0, 1)
            elif key.lower() == "d" or key == readchar.key.RIGHT:
                self.place_player(self.px, self.py, 1, 0)
            elif key.lower() == "w" or key == readchar.key.UP:
                self.place_player(self.px, self.py, 0, -1)

maze_filenames = ["map1.txt", "map2.txt"]
game = FileGame(maze_filenames)
game.run()