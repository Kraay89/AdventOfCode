# ============================================================================#
# IMPORTS.....................................................................#
# ============================================================================#
import os, sys, re
from pathlib import Path
# ============================================================================#
# FINDING AND READING DAY-INPUT INTO A LIST OF INPUT LINES....................#
# Based on filename of current day python file................................#
# ============================================================================#

cwd = os.path.dirname(__file__)
rel_path = Path(cwd) / "Inputs" / "Day4.txt"

crossword = []
with open(rel_path) as f:
    for line in f.readlines():
        crossword.append([i for i in line.strip()])

# ============================================================================#
# Part One....................................................................#
# ============================================================================#
XMASs=0
size = len(crossword[0])
for i in range(4):
    for y in range(size):
        for x in range(size):
            try:
                if all([crossword[y][x]=='X',crossword[y][x+1]=='M',crossword[y][x+2]=='A',crossword[y][x+3]=='S']):
                    XMASs+=1
                if all([crossword[y][x]=='X',crossword[y+1][x+1]=='M',crossword[y+2][x+2]=='A',crossword[y+3][x+3]=='S']):
                    XMASs+=1
            except IndexError:
                pass
    crossword = list(zip(*crossword[::-1]))
    
print(f"Day4-1: {XMASs}")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
XMASs=0
size = len(crossword[0])
for i in range(4):
    for y in range(1,size-1):
        for x in range(1,size-1):
            if crossword[y][x] == 'A':        
                try:
                    if all([crossword[y-1][x-1]=='M', crossword[y-1][x+1]=='M',crossword[y+1][x-1]=='S',crossword[y+1][x+1]=='S']):
                        XMASs+=1
                        print(crossword[y-1][x-1],crossword[y-1][x],crossword[y-1][x+1])
                        print(crossword[y][x-1],crossword[y][x],crossword[y][x+1])
                        print(crossword[y+1][x-1],crossword[y+1][x],crossword[y+1][x+1])
                        print("-----")
                except IndexError:
                    pass
    crossword = list(zip(*crossword[::-1]))


print(f"Day4-2: {XMASs}")



