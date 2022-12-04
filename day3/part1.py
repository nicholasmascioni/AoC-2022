PRIORITIES = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 

    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,  
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52, 
}

total_priority = 0

def in_half(line): # Split each line into 2 halves
    half1, half2 = line[:(len(line)//2)], line[(len(line)//2):]
    return half1, half2

def common_items(pocket1, pocket2):
    common = ''
    for item in pocket1:
        if item in pocket2 and not item in common:
            common += item
    return common

with open("/Users/nicholas/AoC2022/day3/input.txt") as f:
    for line in f:
        line = line.strip()
        pocket1, pocket2 = in_half(line)[0], in_half(line)[1]
        item = common_items(pocket1, pocket2)

        total_priority += PRIORITIES[item]

print(total_priority)