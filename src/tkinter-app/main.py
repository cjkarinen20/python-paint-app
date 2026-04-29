from tkinter import *

class PixelApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
    
        cell_length = 50
        grid_length = 20
        grid_height = 10
        
        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column = 0, row = 0, sticky = (N, E, S, W))
        
        self.cells = []
        cell = Frame(self.drawing_grid, width = cell_length, height = cell_length, bg = "white", highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
        cell.grid(column = 0, row = 0)
        self.cells.append(cell)
        
        
root = Tk()
PixelApp(root)
root.mainloop()