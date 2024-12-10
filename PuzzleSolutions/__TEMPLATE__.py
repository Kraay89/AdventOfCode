# ============================================================================#
# IMPORTS.....................................................................#
# ============================================================================#
import os, sys

# ============================================================================#
# FINDING AND READING DAY-INPUT INTO A LIST OF INPUT LINES....................#
# Based on filename of current day python file................................#
# ============================================================================#

cwd = os.path.dirname(__file__)
day = os.path.basename(os.path.normpath(__file__)).strip(".py")
if day == "__TEMPLATE__":
    pass
    
print(f"Advent of Code: {day}")
rel_path = f"..\Inputs\{day}.txt"
inputPath = os.path.join(cwd, rel_path)

InputLines = []

try:
    with open(inputPath) as f:
        print(f"Getting input from: {inputPath}")
        InputLines.append(line for line in f.read())
except FileNotFoundError:
    #If no input file exists for this day, create it.
    open(inputPath, 'a').close()
    print(f"No input file found, created \"{inputPath}\"")
    sys.exit()

# ============================================================================#
# Part One....................................................................#
# ============================================================================#
print(f"{day}-1: PLACEHOLDER")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
print(f"{day}-2: PLACEHOLDER")



