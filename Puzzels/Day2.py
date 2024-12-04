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
safeReports = 0


print(InputLines)

reports = []
for line in InputLines:
    report = [int(i) for i in line.split()]
    reports.append(report)

def ordered(report:list):
    return any([report == sorted(report), report == sorted(report, reverse=True)])

def differ(report:list):
    for i in range(len(report)):
        try:
            a, b = report[i:i+2]
            if abs(a-b) not in [1,2,3]:
                return False
        except ValueError:
            break
    return True

safeReports = 0
for report in reports:
    if ordered(report) and differ(report):
        safeReports+=1

print(f"{day}-1: There are {safeReports} safe reports in the total list of reports.")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
print(f"{day}-2: PLACEHOLDER")



