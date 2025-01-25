#------ Problem 1 ------

inputFile = open("input.txt", "r")

reports = []

lines = inputFile.readlines()
inputFile.close()

numOfLines = 0

# Process each line from the file
for line in lines:
    line = line.strip()
    if line:
        numOfLines += 1
        x = list(map(int, line.split()))  # Convert elements to integers
        reports.append(x)

safeLines = 0


for line in reports:
    is_increasing = all(line[i] < line[i + 1] and 1 <= line[i + 1] - line[i] <= 3 for i in range(len(line) - 1))
    is_decreasing = all(line[i] > line[i + 1] and 1 <= line[i] - line[i + 1] <= 3 for i in range(len(line) - 1))

    if is_decreasing or is_increasing: safeLines += 1
print(safeLines)

#------ Problem 2 ------

safeLines = 0

for line in reports:
    print(line)
    is_increasing = all(line[i] < line[i + 1] and 1 <= line[i + 1] - line[i] <= 3 for i in range(len(line) - 1))
    is_decreasing = all(line[i] > line[i + 1] and 1 <= line[i] - line[i + 1] <= 3 for i in range(len(line) - 1))

    for i in range(len(line) - 1):
        x = line[i]
        del line[i]
        is_increasing = all(line[i] < line[i + 1] and 1 <= line[i + 1] - line[i] <= 3 for i in range(len(line) - 1))
        is_decreasing = all(line[i] > line[i + 1] and 1 <= line[i] - line[i + 1] <= 3 for i in range(len(line) - 1))
        line.insert(i, x)

        if is_decreasing or is_increasing:
            safeLines += 1
            break
print(safeLines)