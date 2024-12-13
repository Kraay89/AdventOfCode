# ============================================================================#
# IMPORTS.....................................................................#
# ============================================================================#
import os, sys, re

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
        for line in f.readlines():
            InputLines.append(line)
except FileNotFoundError:
    #If no input file exists for this day, create it.
    open(inputPath, 'a').close()
    print(f"No input file found, created \"{inputPath}\"")
    sys.exit()

# ============================================================================#
# Part One....................................................................#
# ============================================================================#

total =0
for instructionSubset in InputLines:
    regex = re.compile("(?:mul\((\d{1,3}),(\d{1,3})\))")
    matches = re.findall(regex, instructionSubset)
    for instruction in matches:
        total += int(instruction[0])*int(instruction[1])
        
        


    

print(f"{day}-1: the sum of all multiplications is {total}")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
print(f"{day}-2: PLACEHOLDER")



