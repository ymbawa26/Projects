""""
Yazan Bawaqna
CS152-B
December 4th 2022
This function performs all the algorithms of the minesweeper game 
"""
from tkinter import *
import setup
import random
import ctypes
import sys
import time


class Cell:

    #initalizing an empty list
    all = []
    count_label = None
    cell_count = setup.grid_dimensions


    def __init__(self, xcells, ycells, mine = False):
        self.is_mine = mine
        self.cell_btn_object = None
        self.x = xcells
        self.y = ycells
        self.is_flag = False
        self.is_opened = False

        #creating the mines using random allocation
        chance = setup.mines / (setup.grid_dimensions * setup.grid_dimensions)
        if(random.random() < chance):
            self.is_mine = True

        #adding all the cells into the Cells list
        Cell.all.append(self)


    def creat_button(self, location):
        """This function create button swhich will function as the cells"""
        #creating the button
        button1 = Button(location, width = 12 , height = 4)
        self.cell_btn_object = button1
        button1.bind('<Button-1>', self.left_click ) # Left Click
        button1.bind('<Button-3>', self.right_click ) # Right Click
        self.cell_btn_object = button1

    @staticmethod 
    def creat_label(location):
        """This function creats a label that counts the nujmber of cells left to be clicked"""

        #setup the label text, widht, height, background color etc...
        label1 = Label(location, text=f"Cells left = {Cell.cell_count}",bg = 'silver', fg= 'black', width=20, height =10, font = ("", 18))
        #return the label
        Cell.count_label_object = label1


    def left_click(self, event):
        """This function shows the cell when the user clicks on the cell with left click"""
        #if it is mine, call the show_mine function
        if self.is_mine:
            self.show_mine()
        #else, call the show_cell function
        else:
            if self.mine_counter == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()

        if Cell.cell_count == setup.mines:
            ctypes.windll.user32.MessageBoxW(0, 'You Won', 'Congratulations! You beated the game', 2)

        # Once already open, unbind the left and right clicks
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')   


    def cell_axis(self, x, y):
        for myCell in Cell.all:
            if myCell.x == x and myCell.y == y:
                return myCell
   

    @property #turning this function an attribute
    def surrounding_cells(self):
        """This function allocates all the surrounding cells for a cell"""

        #allocating all the cells next to each cell
        cells = [
            self.cell_axis(self.x - 1, self.y -1),
            self.cell_axis(self.x - 1, self.y),
            self.cell_axis(self.x - 1, self.y + 1),
            self.cell_axis(self.x, self.y - 1),
            self.cell_axis(self.x + 1, self.y - 1),
            self.cell_axis(self.x + 1, self.y),
            self.cell_axis(self.x + 1, self.y + 1),
            self.cell_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells
    

    @property
    def mine_counter(self):
        """This function counts the number of mines surrounding the cell"""
        count = 0
        #for evey cell in the surrounding cells, count the number of mines
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count +=1
        #return the count number
        return count


    def show_cell(self):
        """ this function shows the cell if the cell does not have a mine"""
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.mine_counter)
            if Cell.count_label_object:
                    Cell.count_label_object.configure (text=f"Cells Left:{Cell.cell_count}")
            self.cell_btn_object.configure(bg='SystemButtonFace')
        # Mark the cell as opened
        self.is_opened = True


    def timer(self, time_limit):
        """This function uses recrusion to create a timer for the game"""
        seconds = time.time()
        if time_limit > seconds:
            print("time_over")
        else:
            return self.timer(time_limit-1)


	

    def show_mine(self):
        """This function showsthe mine when the mine is clicked displays a loss messege"""
        #change the color of the cell to red
        self.cell_btn_object.configure(bg = 'red')
        #print a messega from ctypes library titeled Game Over and with a text "you clicked on a mine"
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 2)
        sys.exit()


    def right_click(self, event):
        """This function turns the unmarked cell into a flag if the the user uses right click to click on it, the opposite is done if the cell is already a flag"""
        #if already not flagged
        if not self.is_flag:
            #call the button coloring method
            self.cell_btn_object.configure(bg='orange')
            #it is now a flag
            self.is_flag = True
        #else,
        else:
            #call the button coloring method
            self.cell_btn_object.configure(bg='systemButtonFace')
            #it is not a flag now
            self.is_flag = False


    @staticmethod
    def creat_mine():
        """This function randomly creat mine cells"""
        #randomly take a smaple from the cells list and elect the mines according the mines count assigned in the setup file
        mine_cells = random.sample( Cell.all, setup.mines)
        #changing mymine to True
        for my_mine in mine_cells:
            my_mine.is_mine = True
        print(type(mine_cells))

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"


#tests
#print(Cell.creat_mine())
