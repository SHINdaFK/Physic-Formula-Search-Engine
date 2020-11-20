from tkinter import *
import random
import sys
import os
import numpy as np
root = Tk()
root.geometry("800x600")

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
for i in range (0, 9):
    for j in range (0, 9):
        retrieve_input[i][j] = StringVar(root)

class JIWOO():
    def __init__(self):
        self.possible
        self.solve

    def possible(self):
        global retrieve_input
        for i in range(0,9):
            if retrieve_input[y][i] == n:
                return False
        for i in range(0,9):
            if retrieve_input[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if retrieve_input[y0+i][x0+j] == n:
                    return False
        return True

    def solve(self):
        global retrieve_input
        for y in range(9):
            for x in range(9):
                if retrieve_input[y][x] == 0:
                    for n in range(1,10):
                        if possible(y,x,n):
                            retrieve_input[y][x] = n
                            solve()
                            retrieve_input[y][x] = 0
                    return
        print(np.matrix(retrieve_input))

class SudokuGUI():
    def __init__(self, hello):

        self.hello = hello
        hello.title("SODUKU SOLVING MACHINE")
        my_font = ("Times New Roman", 20)
        px, py = 0, 0


        self.entry_box = [
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

        for i in range(0, 9):
            for j in range (0, 9):
                self.entry_box[i][j] = Entry(hello, font = my_font, bg = "white", highlightcolor = "yellow", bd = 1, width = 4, cursor = 'star', highlightthickness = 1, highlightbackground = 'black', textvariable = retrieve_input[i][j])
                self.entry_box[i][j].bind('<Motion>', self.correctGrid)
                self.entry_box[i][j].bind('<FocusIn>', self.correctGrid)
                self.entry_box[i][j].bind('<Button-1>', self.correctGrid)
                self.entry_box[i][j].grid(row=i, column=j)


        menu = Menu(hello)
        file = Menu(menu)
        file.add_command(label = "Reset", command= self.restart_program)
        file.add_command(label = "Solve", command= self.solve_sudoku)
        file.add_command(label = "Quit the game", command = hello.quit)
        menu.add_cascade(label = "Menu", menu=file)
        hello.config(menu=menu)

    def restart_program(self):
        for x in range (9):
            for y in range (9):
                retrieve_input[i][j].set("")



    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if retrieve_input[i][j].get() == '':
                    continue
                if len(retrieve_input[i][j].get()) > 1 or retrieve_input[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    retrieve_input[i][j].set('')


    def solve_sudoku(self):
        solution = JIWOO()



b = SudokuGUI(root)
root.mainloop()
