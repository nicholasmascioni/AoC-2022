redundancy = 0
input = []

def redundancy_check(a, b, c, d):
    # Input in form of a-b,c-d
    pair1, pair2 = [], []
    i, j = a, c
    '''
    Fill in the numbers between the two end points of each pair
    For example 3-6 will return 3,4,5,6
    '''
    if a != b:
        while i < b: 
            pair1.append(i)
            i += 1
        pair1.append(b)
    else:
        pair1 = [a, b]    

    if c != d:
        while j < d:
            pair2.append(j)
            j += 1
        pair2.append(d)
    else:
        pair2 = [c, d]

    set_pair1, set_pair2 = set((pair1)), set((pair2)) # Create sets to utilize the intersection method
    overlap = set_pair1.intersection(set_pair2)

    overlap = list(overlap)

    if overlap != []: # Intersection will be empty if there is no overlap
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