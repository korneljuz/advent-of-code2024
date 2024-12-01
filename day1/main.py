file = open("D:/PythonProjects/advent-of-code/day1/input.txt", 'r')

data = file.read()

data = data.strip().split("\n")

first = []
second = []

for line in data:
    line = line.strip().split(" ")
    first.append(line[0])
    second.append(line[-1])

first = sorted(first)
second = sorted(second)

sum = 0

for i in range(len(first)):
    sum += abs(int(second[i]) - int(first[i]))

print(sum)