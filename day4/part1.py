redundancy = 0
input = []

def redundancy_check(a, b, c, d):
    # Input in form of a-b,c-d
    if (a <= c and b >= d) or (c <= a and d >= b):
        return True

with open("/Users/nicholas/AoC2022/day4/input.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        input.append(line)

for i in range(len(input)):
    assignment1 = str(input[i][0]).split('-')
    assignment2 = str(input[i][1]).split('-')

    if redundancy_check(int(assignment1[0]), int(assignment1[1]), int(assignment2[0]), int(assignment2[1])):   
        redundancy += 1

print(redundancy)