import os
from collections import Counter

cwd = os.path.dirname(__file__)
rel_path = "..\Inputs\Day1.txt"
ListLeft = []
ListRight= []

with open(os.path.join(cwd, rel_path), 'r') as inputfile:
    for line in inputfile.readlines():
        L, R = line.split()
        ListLeft.append(int(L))
        ListRight.append(int(R))

sortedListLeft = ListLeft.copy()
sortedListLeft.sort()
sortedlistRight = ListRight.copy()
sortedlistRight.sort()

Total_distance = 0
for pair in zip(sortedListLeft,sortedlistRight):
    Total_distance+=abs(pair[0]-pair[1])

print(f"Day1-1: Total Distance is: {Total_distance}")

occurencesRightList = Counter(ListRight)

similarityScore = 0
for number in ListLeft:
    a = number*occurencesRightList[number]
    similarityScore+=a

print(f"Day1-2: Similarity score is: {similarityScore}")



