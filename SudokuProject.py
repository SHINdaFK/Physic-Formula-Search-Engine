from tkinter import *
import random
import sys
import os
import numpy as np
root = Tk()
root.geometry("800x600")

class JIWOO:
    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,6],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    def possible(y,x,n):
        global grid
        for i in range(0,9):
            if grid[y][i] == n:
                return False
        for i in range(0,9):
            if grid[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == n:
                    return False
        return True

    def solve():
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1,10):
                        if possible(y,x,n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0
                    return
        print(np.matrix(grid))
        input("MOrE? ")

    solve()

class SudokuGUI:
    def __init__(self, hello):
        hello.title("Sudoku_Solver")
        my_font = ("Airal", 18)
        self.entry_box = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,6],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

        for i in range(9):
            for j in range (9):
                self.entry_box[i][j] = Entry(hello, font = my_font, bg = "white", highlightcolor = "yellow", borderwidth = 1, width = 2, cursor = 'star', highlightthickness = 1, highlightbackground = 'black', textvariable = retrieve_input[i][j])
                self.entry_box[i][j].grid(row = [i], columnn = [j])
                self.entry_box[i][j].bind('<Motion>', self.correctGrid)
                self.entry_box[i][j].bind('<FocusIn>', self.correctGrid)
                self.entry_box[i][j].bind('<Button-1>', self.correctGrid)
                self.entry_box[i][j].grid(row=i, column=j)


        menu = Menu(hello)
        file = Menu(menu)
        file.add_command(hello, label = "Reset", command= self.restart_program)
        file.add_command(hello, label = "Solve", command= self.solve_sudoku)
        file.add_command(hello, label = "Quit the game", command = hello.quit)
        menu.add_cascade(hello, label = "Menu", menu=file)
        main.config(menu=menu)

    def restart_program(self):
        for x in range (0, 10):
            for y in range (0, 10):
                retrieve_input[i][j].set("")
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() == '':
                    continue
                if len(savedNumbers[i][j].get()) > 1 or savedNumbers[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    savedNumbers[i][j].set('')


    def solve_sudoku(self):
        solution = JIWOO()

retrieve_input = [        
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]
for i in range (0, 10):
    for j in range (0, 10):
        retrieve_input = StringVar(root)

b = SudokuGUI(root)
root.mainloop()
