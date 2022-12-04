PRIORITIES = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 

    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,  
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, 
}

badges = []
counter = 0
input = []

total_priority = 0

def common_items(line1, line2, line3):
    bag1, bag2, bag3 = set((line1)), set((line2)), set((line3))
    common = bag1.intersection(bag2, bag3)
    badge = list(common)[0] # Access common item in sets since sets are not indexed
    return badge

with open("/Users/nicholas/AoC2022/day3/input.txt") as f:
    for line in f: 
        line = line.strip()
        input.append(line)
        counter += 1
        if counter == 3: # Logic to find common item for every 3 bags
            badges.append(common_items(input[0], input[1], input[2])) 
            input.clear() # Empty list for next 3 elves bags
            counter = 0

for i in range(len(badges)):
    total_priority += PRIORITIES[badges[i]]

print(total_priority)