from tkinter import *

class PixelApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
    
        cell_length = 50
        grid_width = 20
        grid_height = 10
        
        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column = 0, row = 0, sticky = (N, E, S, W))
        
        self.cells = []
        for i in range(0, grid_height):
            for j in range(0, grid_width):
                cell = Frame(self.drawing_grid, width = cell_length, height = cell_length, bg = "white", highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
                cell.grid(column = j, row = i)
                cell.bind('<Button-1>', self.tap_cell)
                self.cells.append(cell)
        
        #-----Control-Panel-----
                
        # Creates the control bar frame on the bottom.
        control_bar = Frame(self.root, height = cell_length)
        control_bar.grid(column = 0, row = 1, sticky = (N, E, S, W))
        
        # Button to create a new drawing.
        new_button = Button(control_bar, text = "New")
        new_button.grid(column = 0, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to save the current drawing.
        save_button = Button(control_bar, text = "Save")
        save_button.grid(column = 2, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to switch to the pen tool.
        pen_button = Button(control_bar, text = "Pen")
        pen_button.grid(column = 8, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to switch to the erase tool.
        erase_button = Button(control_bar, text = "Erase")
        erase_button.grid(column = 10, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Box displaying the currently selected color.
        selected_color_box = Frame(control_bar, borderwidth = 2, relief = "raised", bg = "white")
        selected_color_box.grid(column = 15, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 7, pady = 7)
        
        # Button to pick a new color.
        pick_color_button = Button(control_bar, text = "Pick Color")
        pick_color_button.grid(column = 17, row = 0, columnspan = 3, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        cols, rows = control_bar.grid_size()
        for col in range(cols):
            control_bar.columnconfigure(col, minsize = cell_length)
        control_bar.rowconfigure(0, minsize = cell_length)
        
        
    # Event method for when a cell is pressed.
    def tap_cell(self, event):
        print("Cell Tapped")
        
root = Tk()
PixelApp(root)
root.mainloop()