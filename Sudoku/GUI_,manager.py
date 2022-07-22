from tkinter import *
from turtle import update, window_width
import file_manager
import GameRunner
from PIL import Image, ImageTk

#Files
f = file_manager.file_handled()

#Data
data = f.allText


#Main Menu Setup
window = Tk()
window.title('Main Menu')
window.geometry("1200x800")

c = Canvas(window,width=600, height=800, bg='blue')
c.pack(expand=YES, fill=BOTH)

#Backdrop and Title || Menu
bg = ImageTk.PhotoImage(file="C:\\Users\\Morga\\Desktop\\PYTHON PROJECTS\\Sudoku Git Test\\Sudoku\\outerspace.gif", format="gif -index 2")
textImg = ImageTk.PhotoImage(file="C:\\Users\\Morga\\Desktop\\PYTHON PROJECTS\\Sudoku Git Test\\Sudoku\\SudokuText.png")

#Menu Buttons
easyButton = Button(c, text="Easy Sudoku", command= lambda : launchGame("Easy"))
mediumButton = Button(c, text="Medium Sudoku", command = lambda : launchGame("Medium"))
hardButton = Button(c, text="Hard Sudoku", command= lambda : launchGame("Hard"))
easyButton.place_configure(relheight=0.075, relwidth=0.1, relx=0.465, rely=0.4)
mediumButton.place_configure(relheight=0.075, relwidth=0.1, relx=0.465, rely=0.5)
hardButton.place_configure(relheight=0.075, relwidth=0.1, relx=0.465, rely=0.6)


def resizeEvent(event=None):
    c.create_image(0, 0, image=bg, anchor=NW)
    c.create_image(c.winfo_width()/1.925, c.winfo_height()/9, image=textImg, anchor=N)

def launchGame(diff):
    game = GameRunner.Sudoku(difficulty=diff)



c.bind('<Configure>', resizeEvent)
window.mainloop()
