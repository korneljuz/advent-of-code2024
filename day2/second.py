def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe(report):
        return True 
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

file = open("D:/PythonProjects/advent-of-code/day2/input.txt", 'r')

data = file.read()

reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

safe = sum(is_safe_with_dampener(report) for report in reports)

print(safe)
