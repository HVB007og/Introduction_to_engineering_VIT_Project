# matrix_gui_module.py

import tkinter as tk

class BitMatrixGUI:
    def __init__(self, root, matrix):
        self.root = root
        self.root.title("Bit Matrix GUI")
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        # Create a canvas to display the matrix
        self.canvas = tk.Canvas(root, width=self.cols * 30, height=self.rows * 30)
        self.canvas.pack()

        # Populate the canvas with rectangles representing the bit matrix
        for i in range(self.rows):
            for j in range(self.cols):
                color = self.get_color(matrix[i][j])
                self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

    def update_matrix(self, new_matrix):
        self.matrix = new_matrix
        self.canvas.delete("all")  # Clear the canvas
        # Populate the canvas with rectangles representing the updated bit matrix
        for i in range(self.rows):
            for j in range(self.cols):
                color = self.get_color(new_matrix[i][j])
                self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

    def get_color(self, value):
        if value == 1:
            return "black"
        elif value == 2:
            return "red"
        elif value == 3:
            return "green"
        elif value == 4:
            return "blue"
        else:
            return "white"

def show_bit_matrix(matrix):
    root = tk.Tk()
    app = BitMatrixGUI(root, matrix)
    root.mainloop()

# Example usage:
if __name__ == "__main__":
    MATRIX = [
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    show_bit_matrix(MATRIX)
