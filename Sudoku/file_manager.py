import os
import numpy as np
from re import search

class file_handled:
    def __init__(self):
        solutions_path, problems_path = "C:\\Users\\Morga\\Desktop\\PYTHON PROJECTS\\Sudoku Git Test\\Sudoku\\SudokuText", "C:\\Users\\Morga\\Desktop\\PYTHON PROJECTS\\Sudoku Git Test\\Sudoku\\SudokuText"
        allPaths = [problems_path, solutions_path]

        self.allText = [[], []]
        self.correspondingNames = [[], []]
        count = 0
        for path in allPaths:

            numOfFiles = 0
            os.chdir(path)

            def read_text_file_toArray(file_path):
                with open(file_path, 'r') as f:
                    newline = ""
                    for line in f:
                        for character in line:
                            if character.isdigit():
                                newline += str(character)
                    self.allText[count].append(newline)
                    self.correspondingNames[count].append(file_path)

            for file in os.listdir():
                # Check whether file is in text format or not
                if file.endswith(".txt"):
                    file_path = f"{path}\{file}"
                    numOfFiles += 1
            
                    # call read text file function
                    
                    read_text_file_toArray(file_path)
            count += 1
        #print(self.allText[1][27:30])
        #print(self.correspondingNames[1][27:30])
#f = file_handled()


