import datetime
import os
from pathlib import Path
import re


def getToday():
    return datetime.datetime.today().day

def getPuzzleFiles():
    basepath = Path(os.getcwd())
    puzzleFolder = basepath /"PuzzleSolutions"
    pattern = re.compile('Day\d+\.py')
    return [f for f in os.listdir(puzzleFolder) if os.path.isfile(os.path.join(puzzleFolder, f)) and pattern.match(f)]

def getInputFiles():
    basepath = Path(os.getcwd())
    puzzleFolder = basepath /"PuzzleInputs"
    pattern = re.compile('Day\d+\.py')
    return [f for f in os.listdir(puzzleFolder) if os.path.isfile(os.path.join(puzzleFolder, f)) and pattern.match(f)]

def startNewDay():
    pass

def newInputFile():
    pass

def newPuzzleFile():
    pass
