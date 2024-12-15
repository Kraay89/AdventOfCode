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
rel_path = Path(cwd) / "Inputs" / "Day3.txt"

Input=""
with open(rel_path) as f:
    for line in f.readlines():
        Input += line


# ============================================================================#
# Part One....................................................................#
# ============================================================================#

total = 0

regex = re.compile("(?:mul\((\d{1,3}),(\d{1,3})\))")
matches = re.findall(regex, Input)
for instruction in matches:
    total += int(instruction[0])*int(instruction[1])


print(f"day 3-1: the sum of all multiplications is {total}")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
total = 0
doing = True
regex = re.compile("(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")
matches = re.findall(regex, Input)
for instruction in matches:
    if instruction[2]=="do()":
        if not doing:
            print(f"found {instruction}, multiplying again.")
        doing = True
    elif instruction[3]=="don't()":
        if doing:
            print(f"found {instruction}, stopping.")
        doing=False
    else:
        if doing:
            print(f"using: {instruction}")
            total += int(instruction[0])*int(instruction[1])
        else:
            print(f"Skipping: {instruction}")
            
    

print(f"day 3-2: the sum of all multiplications, taking 'do' and 'don\"t' in regard is: {total}")



