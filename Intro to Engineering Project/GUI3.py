import tkinter as tk

class MazeGUI:
    def __init__(self, root, maze):
        self.root = root
        self.root.title("Maze GUI")
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

        # Create a canvas to display the maze
        self.canvas = tk.Canvas(root, width=self.cols * 30, height=self.rows * 30)
        self.canvas.pack()

        # Populate the canvas with shapes representing the maze
        for i in range(self.rows):
            for j in range(self.cols):
                shape = self.get_shape(maze[i][j])
                color = self.get_color(maze[i][j])
                if shape == "square":
                    self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)
                elif shape == "rectangle":
                    self.canvas.create_rectangle(j * 30, i * 30, (j + 2) * 30, (i + 1) * 30, fill=color)
                elif shape == "circle":
                    self.canvas.create_oval(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

    def get_shape(self, value):
        if value == "corner":
            return "square"
        elif value == "wall":
            return "rectangle"
        elif value == "position":
            return "circle"
        else:
            return "square"

    def get_color(self, value):
        if value == "corner":
            return "black"
        elif value == "wall":
            return "gray"
        elif value == "position":
            return "white"
        else:
            return "white"

def show_maze(maze):
    root = tk.Tk()
    app = MazeGUI(root, maze)
    root.mainloop()

# Example usage:
if __name__ == "__main__":
    MAZE = [
        ["corner", "wall", "corner", "wall"],
        ["wall", "position", "wall", "position"],
        ["corner", "wall", "corner", "wall"],
        ["wall", "position", "wall", "position"],
    ]

    show_maze(MAZE)
