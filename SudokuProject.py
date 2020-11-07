from tkinter import *
import random
root = Tk()
root.geometry("800x600")


def do_something():
    outputlabel = Label(text="hello")
    outputlabel.grid(row=3, column=0)


def playagain(self):
    self.game.destroy()
    self.__init__()


menu = Menu(window)
file = Menu(menu)
file.add_command(label="Reset", command=resetAll)
file.add_command(label="Solve", command=do_something)
file.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="Reset the board, Solve or Quit", menu=file)
window.config(menu=menu)

center = Frame(root, bg='white', width=100, height=100, padx=3, pady=3)

root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(9, weight=1)
center.grid(row=1, sticky="nsew")

center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

cell1 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3,  pady=3)
cell2 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell3 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell4 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell5 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell6 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell7 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell8 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)
cell9 = Frame(center, bg='white', highlightbackground="black", highlightcolor="black", highlightthickness=1, width=50, height=50,  padx=3, pady=3)


cell1.grid(row=0, column=0)
cell2.grid(row=0, column=1)
cell3.grid(row=0, column=2)
cell4.grid(row=0, column=3)
cell5.grid(row=0, column=4)
cell6.grid(row=0, column=5)
cell7.grid(row=0, column=6)
cell8.grid(row=0, column=7)
cell9.grid(row=0, column=8)


cells = {}
for row in range(10):
    for column in range(9):
        cell = Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=50, height=50,  padx=3,  pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell

root.mainloop()



# SUDOKU CODE


a = [["0"],["0"],["3"],["0"],["4"],["2"],["0"],["9"],["0"]]
b = [["0"],["9"],["0"],["0"],["6"],["0"],["5"],["0"],["0"]]
c = [["5"],["0"],["0"],["0"],["0"],["0"],["0"],["1"],["0"]]
d = [["0"],["0"],["1"],["7"],["0"],["0"],["2"],["8"],["5"]]
e = [["0"],["0"],["8"],["0"],["0"],["0"],["1"],["0"],["0"]]
f = [["3"],["2"],["9"],["0"],["0"],["8"],["7"],["0"],["0"]]
g = [["0"],["3"],["0"],["0"],["0"],["0"],["0"],["0"],["1"]]
h = [["0"],["0"],["5"],["0"],["9"],["0"],["0"],["2"],["0"]]
i = [["0"],["8"],["0"],["2"],["1"],["0"],["6"],["0"],["0"]]



def startRow(x):
    for y in x:
        if y[0] == "0": 
            if len(y) == 1:
                y.extend(["1","2","3","4","5","6","7","8","9"])
            for z in x:
                if (z[0] != "0" and (z[0] in y)):
                    y.remove(z[0])



def startAllRow():
    startRow(a)
    startRow(b)
    startRow(c)
    startRow(d)
    startRow(e)
    startRow(f)
    startRow(g)
    startRow(h)
    startRow(i)

startAllRow()


def startColumn(row):
    position = 0
    for m in row:
        if m[0] == "0":
            if a[position][0] != "0" and a[position][0] in m and a[position] != m:
                m.remove(a[position][0])
            if b[position][0] != "0" and b[position][0] in m and b[position] != m:
                m.remove(b[position][0])
            if c[position][0] != "0" and c[position][0] in m and c[position] != m:
                m.remove(c[position][0])
            if d[position][0] != "0" and d[position][0] in m and d[position] != m:
                m.remove(d[position][0])
            if e[position][0] != "0" and e[position][0] in m and e[position] != m:
                m.remove(e[position][0])
            if f[position][0] != "0" and f[position][0] in m and f[position] != m:
                m.remove(f[position][0])
            if g[position][0] != "0" and g[position][0] in m and g[position] != m:
                m.remove(g[position][0])
            if h[position][0] != "0" and h[position][0] in m and h[position] != m:
                m.remove(h[position][0])
            if i[position][0] != "0" and i[position][0] in m and i[position] != m:
                m.remove(i[position][0])
        position += 1
def startAllColumn():
    startColumn(a)
    startColumn(b)
    startColumn(c)
    startColumn(d)
    startColumn(e)
    startColumn(f)
    startColumn(g)
    startColumn(h)
    startColumn(i)

startAllColumn()


def removeZero(row):
    for y in row:
        if y[0] == "0" and len(y) == 2:
            y.remove("0")

def removeAllZero():
    removeZero(a)
    removeZero(b)
    removeZero(c)
    removeZero(d)
    removeZero(e)
    removeZero(f)
    removeZero(g)
    removeZero(h)
    removeZero(i)

removeAllZero()


dothewoo = 0

while dothewoo < 100:
    startAllRow()
    startAllColumn()
    removeAllZero()
    dothewoo += 1

box1 = [(a[0]),(a[1]),(a[2]),(b[0]),(b[1]),(b[2]),(c[0]),(c[1]),(c[2])]
box2 = [a[3],a[4],a[5],b[3],b[4],b[5],c[3],c[4],c[5]]
box3 = [a[6],a[7],a[8],b[6],b[7],b[8],c[6],c[7],c[8]]
box4 = [d[0],d[1],d[2],e[0],e[1],e[2],f[0],f[1],f[2]]
box5 = [d[3],d[4],d[5],e[3],e[4],e[5],f[3],f[4],f[5]]
box6 = [d[6],d[7],d[8],e[6],e[7],e[8],f[6],f[7],f[8]]
box7 = [g[0],g[1],g[2],h[0],h[1],h[2],i[0],i[1],i[2]]
box8 = [g[3],g[4],g[5],h[3],h[4],h[5],i[3],i[4],i[5]]
box9 = [g[6],g[7],g[8],h[6],h[7],h[8],i[6],i[7],i[8]]


def solveBox(box):
    for y in box:
        for z in box:
            if (z[0] != "0" and (z[0] in y)):
                y.remove(z[0])

def solveAllBox():
    startRow(box1)
    startRow(box2)
    startRow(box3)
    startRow(box4)
    startRow(box5)
    startRow(box6)
    startRow(box7)
    startRow(box8)
    startRow(box9)

solveAllBox()

dothewoo = 0

while dothewoo < 100:
    startAllRow()
    startAllColumn()
    removeAllZero()
    solveAllBox()
    dothewoo += 1

def doOnlySolution(line):
    allnum = []
    unique = []
    for x in line:
        for y in x:
            allnum.append(y)
    for number in range(1,10):
        if allnum.count(str(number)) == 1:
            unique.append(str(number))
    for x in line:
        if x[0] != "0":
            unique.remove(x[0])
    for x in line:
        for y in x:
            if y in unique:
                

print(a)