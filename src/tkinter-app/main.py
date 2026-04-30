from tkinter import *
import tkinter.colorchooser
import os

# Obtain file paths for control bar icons.
images_dir = os.path.dirname(__file__)
pencil_path = "./icons/pencil.png"
eraser_path = "./icons/eraser.png"
pencil_abs_path = os.path.join(images_dir, pencil_path)
eraser_abs_path = os.path.join(images_dir, eraser_path)

class PixelApp:
    
    def __init__(self, root):
        
        # Create the root window.
        self.root = root
        self.root.title("Pixel Art")
    
        #--Grid-Options--  
        cell_length = 50
        grid_width = 20
        grid_height = 10
        
        # Create the color picker.
        self.color_picker = tkinter.colorchooser.Chooser(self.root)
        self.chosen_color = None
        
        # Initialize the drawing grid.
        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column = 0, row = 0, sticky = (N, E, S, W))
        
        # Populate the display window with grid squares.
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
        new_button = Button(control_bar, text = "New", command = self.press_new_button)
        new_button.grid(column = 0, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to save the current drawing.
        save_button = Button(control_bar, text = "Save", command = self.press_save_button)
        save_button.grid(column = 2, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to switch to the pen tool.
        self.pencil_image = PhotoImage(file = pencil_abs_path).subsample(2, 3)
        pencil_button = Button(control_bar, text = "Pencil", image = self.pencil_image, command = self.press_pencil_button)
        pencil_button.grid(column = 8, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Button to switch to the erase tool.
        self.eraser_image = PhotoImage(file = eraser_abs_path).subsample(2, 3)
        eraser_button = Button(control_bar, text = "Eraser", image = self.eraser_image, command = self.press_eraser_button)
        eraser_button.grid(column = 10, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        # Box displaying the currently selected color.
        self.selected_color_box = Frame(control_bar, borderwidth = 2, relief = "raised", bg = "white")
        self.selected_color_box.grid(column = 15, row = 0, columnspan = 2, sticky = (N, E, S, W), padx = 5, pady = 8)
        
        # Button to pick a new color.
        pick_color_button = Button(control_bar, text = "Pick Color", command = self.press_pick_color_button)
        pick_color_button.grid(column = 17, row = 0, columnspan = 3, sticky = (N, E, S, W), padx = 5, pady = 5)
        
        cols, rows = control_bar.grid_size()
        for col in range(cols):
            control_bar.columnconfigure(col, minsize = cell_length)
        control_bar.rowconfigure(0, minsize = cell_length)
             
    # Event method for when a cell is pressed.
    def tap_cell(self, event):
        print("Cell Tapped")
        
    # Event method for when "New" button is pressed. 
    def press_new_button(self):
        print("New Button Pressed.")
        
    # Event method for when the "Save" button is pressed.
    def press_save_button(self):
        print("Save Button Pressed.")
        
    # Event method for when the "Pen" button is pressed.
    def press_pencil_button(self):
        print("Pencil Button Pressed.")
        
     # Event method for when the "Erase" button is pressed.
    def press_eraser_button(self):
        print("Erase Button Pressed.")
        
    # Event method for when the "Pick Color" button is pressed.
    def press_pick_color_button(self):
        color_info = self.color_picker.show()
        chosen = color_info[1]
        if chosen != None:
            self.chosen_color = chosen
            self.selected_color_box["bg"] = self.chosen_color
        
root = Tk()
PixelApp(root)
root.mainloop()