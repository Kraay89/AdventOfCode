# ============================================================================#
# IMPORTS.....................................................................#
# ============================================================================#
import os, sys
from pathlib import Path


# ============================================================================#
# FINDING AND READING DAY-INPUT INTO A LIST OF INPUT LINES....................#
# Based on filename of current day python file................................#
# ============================================================================#

cwd = os.path.dirname(__file__)
rel_path = Path(cwd) / "Inputs" / "Day2.txt"

InputLines=[]
with open(rel_path) as f:
    for line in f.readlines():
        InputLines.append(line)

# ============================================================================#
# Part One....................................................................#
# ============================================================================#
safeReports = 0

# class report:
#     def __init__(self, report:list):
#         self.report = report
#         self.ordered = True
#         self.direction = 0 # 1 descending, 2 ascending, 0 undecided
#         self.stepsize = True
    
#     def ordered(self):
#         pos = 0
#         while self.ordered:
#             try:
#                 if self.direction == 0:
#                     pass
                
#             if self.report[0]:
#                 pass
            

reports = []
for line in InputLines:
    report = [int(i) for i in line.split()]
    reports.append(report)

def ordered(report:list):
    return any([report == sorted(report), report == sorted(report, reverse=True)])

def differ(report:list, canDel:bool=True):
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

print(f"Day 2-1: There are {safeReports} safe reports in the total list of reports.")

# ============================================================================#
# Part Two....................................................................#
# ============================================================================#
print(f"day 2-2: PLACEHOLDER")



