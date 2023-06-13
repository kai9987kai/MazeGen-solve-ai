import random
import tkinter as tk

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0] * width for _ in range(height)]
    
    def generate_maze(self):
        stack = [(0, 0)]
        visited = set()

        while stack:
            current_x, current_y = stack[-1]
            self.maze[current_y][current_x] = 1
            visited.add((current_x, current_y))

            neighbors = []
            if current_x > 1 and (current_x - 2, current_y) not in visited:
                neighbors.append((current_x - 2, current_y))
            if current_x < self.width - 2 and (current_x + 2, current_y) not in visited:
                neighbors.append((current_x + 2, current_y))
            if current_y > 1 and (current_x, current_y - 2) not in visited:
                neighbors.append((current_x, current_y - 2))
            if current_y < self.height - 2 and (current_x, current_y + 2) not in visited:
                neighbors.append((current_x, current_y + 2))

            if neighbors:
                next_x, next_y = random.choice(neighbors)
                self.maze[(current_y + next_y) // 2][(current_x + next_x) // 2] = 1
                stack.append((next_x, next_y))
            else:
                stack.pop()

    def print_maze(self):
        for row in self.maze:
            print(' '.join(['#' if cell == 1 else ' ' for cell in row]))

class MazeCanvas(tk.Canvas):
    def __init__(self, parent, maze, cell_size, canvas_width, canvas_height):
        super().__init__(parent, width=canvas_width, height=canvas_height)
        self.maze = maze
        self.cell_size = cell_size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
    
    def draw_maze(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 1:
                    x1 = x * self.cell_size
                    y1 = y * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.create_rectangle(x1, y1, x2, y2, fill='black')

class Bot:
    def __init__(self, maze):
        self.maze = maze
        self.current_x = 0
        self.current_y = 0
        self.goal_x = len(maze[0]) - 1
        self.goal_y = len(maze) - 1

    def move(self, direction):
        if direction == 'up':
            if self.current_y > 0 and self.maze[self.current_y - 1][self.current_x] == 1:
                self.current_y -= 1
        elif direction == 'down':
            if self.current_y < len(self.maze) - 1 and self.maze[self.current_y + 1][self.current_x] == 1:
                self.current_y += 1
        elif direction == 'left':
            if self.current_x > 0 and self.maze[self.current_y][self.current_x - 1] == 1:
                self.current_x -= 1
        elif direction == 'right':
            if self.current_x < len(self.maze[0]) - 1 and self.maze[self.current_y][self.current_x + 1] == 1:
                self.current_x += 1

    def is_at_goal(self):
        return self.current_x == self.goal_x and self.current_y == self.goal_y

# Maze generation parameters
maze_width = 51
maze_height = 51

# Canvas parameters
cell_size = 10
canvas_width = maze_width * cell_size
canvas_height = maze_height * cell_size

# Generate the maze
maze_generator = MazeGenerator(maze_width, maze_height)
maze_generator.generate_maze()
maze_generator.print_maze()

# Create the maze canvas
root = tk.Tk()
maze_canvas = MazeCanvas(root, maze_generator.maze, cell_size, canvas_width, canvas_height)
maze_canvas.draw_maze()
maze_canvas.pack()

# Create the bot
bot = Bot(maze_generator.maze)

# Move the bot randomly until it reaches the goal
while not bot.is_at_goal():
    directions = ['up', 'down', 'left', 'right']
    random_direction = random.choice(directions)
    bot.move(random_direction)

    # Draw the bot's current position
    x = bot.current_x * cell_size
    y = bot.current_y * cell_size
    maze_canvas.create_oval(x, y, x + cell_size, y + cell_size, fill='red')
    maze_canvas.update()
    maze_canvas.after(100)

root.mainloop()
