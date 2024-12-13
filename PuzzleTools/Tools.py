import datetime
import os
from pathlib import Path
import re


def getToday():
    today = datetime.datetime.today()
    if today.month == 12:
        return today.day
    else:
        raise ValueError

def getPuzzleSolutionsPath(year)-> Path:
    basepath = Path(os.getcwd())
    puzzleFolder = basepath /"Puzzles"/str(year)/"PuzzleSolutions"
    Path.mkdir(puzzleFolder, parents= True, exist_ok=True)
    return puzzleFolder

def getPuzzleInputsPath(year)-> Path: 
    basepath = Path(os.getcwd())
    inputFolder = basepath /"Puzzles"/str(year)/"PuzzleInputs"
    Path.mkdir(inputFolder, parents=True, exist_ok=True)
    return inputFolder
    
def getPuzzleSolutions(year):
    pattern = re.compile('Day\d+\.py')
    return [f for f in os.listdir(getPuzzleSolutionsPath(year)) if os.path.isfile(os.path.join(getPuzzleSolutionsPath(year), f)) and pattern.match(f)]

def getInputFiles(year):
    pattern = re.compile('Day\d+\.py')
    return [f for f in os.listdir(getPuzzleInputsPath(year)) if os.path.isfile(os.path.join(getPuzzleInputsPath(year), f)) and pattern.match(f)]

def newPuzzleInputFile(year, n):
    newFP = os.path.join(getPuzzleInputsPath(year), f"InputDay{n}.txt")
    with open(newFP,'a'):
        pass

def newPuzzleSolutionFile(year, n):
    newFP = os.path.join(getPuzzleSolutionsPath(year), f"Day{n}.py")
    with open(newFP,'a'):
        pass

def setupAdventOfCode(year:int=datetime.datetime.today().year)->None:
    inputs = getInputFiles(year)
    solutions = getPuzzleSolutions(year)
    inputs = [int(re.search(r'\d+', file).group()) for file in inputs]
    solutions = [int(re.search(r'\d+', file).group()) for file in solutions]
    for i in range(1,25):
        if i not in inputs:
            newPuzzleInputFile(year, i)
        if i not in solutions:
            newPuzzleSolutionFile(year, i)
    
if __name__=="__main__":
    setupAdventOfCode(2023)