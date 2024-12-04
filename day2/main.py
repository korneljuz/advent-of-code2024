file = open("D:/PythonProjects/advent-of-code/day2/input.txt", 'r')

data = file.read()


data = data.strip().split("\n")
data = [list(map(int, sub.strip().split())) for sub in data]

safe = 0

for line in data:
    decreasing = True
    increasing = True
    inrange = True
    n = len(line)
    
    for num in range(n - 1):
        first = line[num]
        second = line[num + 1]

        if(first == second): # jak to samo to wywal
            inrange = False

        if first < second:
            decreasing = False
        if first > second:
            increasing = False
        
        if abs(first - second) > 3:
            inrange = False

    #print(f"Report: {line}, Increasing: {increasing}, Decreasing: {decreasing}, In Range: {inrange}, max: {inrange and (increasing or decreasing)}")

    if (inrange and (increasing or decreasing)):
        safe += 1

print(safe)