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
                color = "black" if matrix[i][j] == 1 else "white"
                self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

    def update_matrix(self, new_matrix):
        self.matrix = new_matrix
        self.canvas.delete("all")  # Clear the canvas
        # Populate the canvas with rectangles representing the updated bit matrix
        for i in range(self.rows):
            for j in range(self.cols):
                color = "black" if new_matrix[i][j] == 1 else "white"
                self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

def show_bit_matrix(matrix):
    root = tk.Tk()
    app = BitMatrixGUI(root, matrix)
    root.mainloop()
