#------ Problem 1 ------

inputFile = open("input.txt", "r")

leftSide = []
rightSide = []

lines = inputFile.readlines()
inputFile.close()
numOfLines = 0

for line in lines:
    line = line.strip()
    if line:  # Skip empty lines
        numOfLines += 1
        x = line.split("   ")  # Split by three spaces
        if len(x) == 2:  # Ensure there are two parts
            leftSide.append(int(x[0].strip()))
            rightSide.append(int(x[1].strip()))


leftSide.sort()
rightSide.sort()


sum = 0

for i in range(numOfLines):
    sum += abs(leftSide[i] - rightSide[i])

print("Problem 1 Answer: ", sum)


#------ Problem 2 ------

sum = 0
for i in range(numOfLines):
    count = rightSide.count(leftSide[i])
    sum += (count *  leftSide[i])

print("Problem 1 Answer: ", sum)
