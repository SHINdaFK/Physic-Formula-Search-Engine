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
        self.allZero()
        self.startSolution()



    def allZero(self):
        for i in range(9):
            for j in range(9):
                if retrieve_input[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    retrieve_input[i][j].set(0)



    def startSolution(self, i=0, j=0):
        i,j = self.findNextCellToFill(i, j)


        if i == -1:
            return True
        for e in range(1,10):
            if self.isValid(i,j,e):
                retrieve_input[i][j].set(e)
                if self.startSolution(i, j):
                    return True

                retrieve_input[i][j].set(0)
        return False


    def findNextCellToFill(self, i, j):

        for x in range(i,9):
            for y in range(j,9):
                if retrieve_input[x][y].get() == '0':
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if retrieve_input[x][y].get() == '0':
                    return x,y

        return -1,-1


    def isValid(self, i, j, e):

        for x in range(9):
            if retrieve_input[i][x].get() == str(e):
                return False

        for x in range(9):
            if retrieve_input[x][j].get() == str(e):
                return False
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if retrieve_input[x][y].get() == str(e):
                    return False
        
        return True





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
                retrieve_input[x][y].set("")



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
