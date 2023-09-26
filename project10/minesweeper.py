""""
Yazan Bawaqna
CS152-B
December 4th 2022

This program is the minesweeper game main function, the program sets the codes together and draws the graphics
To run this program just click on the run button (make sure the terminal is clear)
"""
from tkinter import *
import setup
import utility
from cell import Cell

#Display a window
window = Tk()
#organizng the window dimensions
window.geometry(f'{setup.width}x{setup.height}')
#giving a title for the window
window.title('Minesweeper game')
window.resizable(False, False)
#background color setu
window.configure(bg = 'silver')

#creating a seperate section for the title at the top of the page
top_section = Frame(window, bg = 'gold', width= setup.width, height = utility.height_percantage(25))
#placing the section into the desired space
top_section.place(x = 0, y = 0 )


#setting a title at the top of the page
title = Label(top_section, bg='black', fg='white', text='Minesweeper Game', font=('', 48))
title.place(x=utility.width_percantage(25), y=0)


#creating a seperate section for the left bar of the screen and placing it
sideBar_section = Frame(window, bg = 'black', width = utility.width_percantage(25) , height = utility.height_percantage(75))
sideBar_section.place(x =0, y = utility.height_percantage(25))


#creating the game frame and placing it
game_section = Frame(window, bg = 'white', width =utility.width_percantage(75), height = utility.height_percantage(75))
game_section.place(x =utility.width_percantage(25), y = utility.height_percantage(25))

 
#creating cells (the buttons which the players click during the game trying to avoid the mines)
#for every row
for xcells in range(setup.grid):
    #for every coloumn
    for ycells in range(setup.grid):
        cell = Cell(xcells, ycells)
        #creat a button as a cell
        cell.creat_button(game_section)
        #place the button
        cell.cell_btn_object.grid(column = xcells, row = ycells) 

Cell.creat_label(sideBar_section)
Cell.count_label_object.place(x = 0 , y= 0)
Cell.creat_mine()

#keep the window running
window.mainloop()
