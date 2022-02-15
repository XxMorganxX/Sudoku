import random
from tkinter import *
import file_manager
from math import hypot

class Sudoku:
    def __init__(self, difficulty):
        self.root = Tk()
        self.root.minsize(width=500, height=500)
        self.root.geometry("900x900")
        self.root.title(difficulty + " Sudoku")
        self.root.resizable(False, False)

        self.waitingForKey = False
        self.constantBox = []
        self.boxSelected = None
        self.firstSetUp = True
        
        data = file_manager.file_handled().allText
        self.gameBoardText, self.Solution = self.determinePuzzle(difficulty, data)

        self.gameBoard = self.gameBoardText
        
        self.c = Canvas(self.root, bg='white', highlightthickness=1, highlightbackground="black")
        self.c.pack(fill=BOTH, expand=True)
        self.setupBoard(self.c)

        print(self.Solution)
    
        self.updateBoxAtPoint(0)
        


        self.root.bind("<Key>", self.keyEvent)
        self.root.bind("<Button-1>", self.selectBox)



        self.root.mainloop()
    
    def keyEvent(self, event=None):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        try:
            if (int(event.char) in nums) and (self.boxSelected not in self.constantBox):
                self.updateBoxAtPoint(int(event.char))
                self.checkWin()
        except:
            pass


    def checkWin(self):
        if self.Solution == self.gameBoard:
            print("Game Won")
    


    def updateBoxAtPoint(self, num):
        if self.boxSelected != None:
            index = self.midPointsDict[self.boxSelected]
            self.gameBoard[index] = num
        try:
            self.c.delete("numbers")
        except:
            pass

        count = 0
        for x, y in self.boxMidPoints:
            if self.gameBoard[count] != 0:
                self.c.create_text(x, y, text=self.gameBoard[count], tags="numbers", font=('Helvetica','25','bold'))
                if self.firstSetUp:
                    self.constantBox.append((x, y))
            #else:
                #next
            count += 1


    def determinePuzzle(self, diff, allBoards):
        potentialBoards = []
        boardSolutions = []
        rang = None
        if (diff == "Easy"):
            rang = (27, 30)
        elif (diff == "Medium"):
            rang = (30, 33)
        elif (diff == "Hard"):
            rang = (33, 36)

        for i in range (rang[0], rang[1]):
                potentialBoards.append(allBoards[1][i])
                boardSolutions.append(allBoards[0][i])
        rand = random.randint(0, 2)
        potentialBoard, boardSolution = potentialBoards[rand], boardSolutions[rand]
        boardArray = []
        solutionArray = []
        for word in potentialBoard:
            toAdd = int(word)
            boardArray.append(toAdd)
        for word in boardSolution:
            toAdd = int(word)
            solutionArray.append(toAdd)
        self.firstSetUp = True

        return boardArray, solutionArray
        
    def selectBox(self, event):
        correctionL = 900/18
        self.c.delete("boxSelected")
        Xmouse, Ymouse = event.x, event.y
        vectorDict = {}
        count = 0
        for x, y in self.boxMidPoints:
            vect = hypot(Xmouse - x, Ymouse - y)
            vectorDict[self.boxMidPoints[count]] = vect
            count += 1
        self.boxSelected = self.get_keys_from_value(vectorDict , min(vectorDict.values()))
        self.firstSetUp = False
        currentSelectedBoxOutline = self.c.create_rectangle(self.boxSelected[0]-correctionL, self.boxSelected[1]-correctionL, self.boxSelected[0]+correctionL, self.boxSelected[1]+correctionL, width=2, outline="red", tags="boxSelected")
        


    def get_keys_from_value(self, d, val):
        for k, v in d.items(): 
            if v == val:
                return k    

 
    def setupBoard(self, canvas):
        l = 900
        boxL = int(l/3)
        self.boxMidPoints = []
        self.midPointsDict = {}

        for i in range(0, l, int(l/3)):
            canvas.create_line([(i, 0), (i, l)], tag='grid_line', width=2)
        for i in range(0, l, int(l/3)):
            canvas.create_line([(0, i), (l, i)], tag='grid_line', width=2)
        
        for v in range(0, 9):
            if v % 3 != 0:
                canvas.create_line((int(l/9)*v, 0), (int(l/9)*v, l), tag='grid_line')
        for v in range(0, 9):
            if v % 3 != 0:
                canvas.create_line((0, int(l/9)*v), (l, int(l/9)*v), tag='grid_line')
            
        index = 0
        for row in range(int(l/18), l, int(l/9)):
            for column in range(int(l/18), l, int(l/9)):
                self.boxMidPoints.append((column, row))
                self.midPointsDict[self.boxMidPoints[index]] = index
                index += 1                        


    



        

        