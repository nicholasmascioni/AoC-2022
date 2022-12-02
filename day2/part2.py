score = 0

def new_rock_paper_scissors(line):
    score = 0
    '''
    X -> need to lose (0 points)
    Y -> need to draw (3 points)
    Z -> need to win (6 points)
    '''

    if line[0] == 'A' and line[2] == 'X': 
        score += 3 # scissors loses to rock
    elif line[0] == 'B' and line[2] == 'X': 
        score += 1 # rock loses to paper
    elif line[0] == 'C' and line[2] == 'X': 
        score += 2 # paper loses to scissors 

    elif line[0] == 'A' and line[2] == 'Y': 
        score += 3 
        score += 1 # rock to draw
    elif line[0] == 'B' and line[2] == 'Y': 
        score += 3 
        score += 2 # paper to draw
    elif line[0] == 'C' and line[2] == 'Y': 
        score += 3 
        score += 3 # scissors to draw

    elif line[0] == 'A' and line[2] == 'Z': 
        score += 6
        score += 2 # paper beats rock
    elif line[0] == 'B' and line[2] == 'Z': 
        score += 6
        score += 3 # scissors beats paper
    elif line[0] == 'C' and line[2] == 'Z': 
        score += 6
        score += 1 # rock beats scissors
    
    return score

with open("/Users/nicholas/AoC2022/input.txt") as f:
    for line in f:
        line = line.strip()
        score += new_rock_paper_scissors(line)

print(score)