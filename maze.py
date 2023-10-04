import readchar
import os

WALL = "#"
PATH = "."
PLAYER = "P"

px = 0
py = 0

def print_instructions():
	print("\nINSTRUCCIONES: ")
	print("\tUsa las flechas para moverte, q para salir")

def print_maze(maze):
	for row in maze:
		print("".join(row))
	
	print_instructions()
		
def place_player(maze, x, y, dx, dy):
	global px, py
	maze_width = len(maze[0])
	maze_height = len(maze)
	
	if x + dx < 0 or x + dx >= maze_width or y + dy < 0 or y + dy >= maze_height:
		return 
	
	if y + dy == maze_height - 1 and x + dx == maze_width - 1:
		print("\n\n\t\tG A N A S T E\n\n")
		exit()

	if maze[y + dy][x + dx] == PATH:
		maze[y][x] = PATH
		maze[y + dy][x + dx] = PLAYER
		px = x + dx
		py = y + dy
		
with open("maze.txt", "r") as f:
	maze = list(map(lambda x: list(x), f.read().splitlines()))
	place_player(maze, px, py, 0, 0)

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print_maze(maze)
		key = readchar.readkey()
		
		if key == "q":
			break
		elif key.lower() == "a" or key == readchar.key.LEFT:
			place_player(maze, px, py, -1, 0)
		elif key.lower() == "s" or key == readchar.key.DOWN:
			place_player(maze, px, py, 0, 1)
		elif key.lower() == "d" or key == readchar.key.RIGHT:
			place_player(maze, px, py, 1, 0)
		elif key.lower() == "w" or key == readchar.key.UP:
			place_player(maze, px, py, 0, -1)
