score = 0

def rock_paper_scissors(line):
    score = 0

    if line[0] == 'A' and line[2] == 'X': # rock vs rock
        score += 3 # for a draw
        score += 1 # for choosing rock
    elif line[0] == 'B' and line[2] == 'X': # paper vs rock
        score += 1 # 0 points for loss, 1 for choosing rock
    elif line[0] == 'C' and line[2] == 'X': # scissors vs rock
        score += 6 # for a win
        score += 1 # for choosing rock

    elif line[0] == 'A' and line[2] == 'Y': # rock vs paper
        score += 6 # for a win
        score += 2 # for choosing paper
    elif line[0] == 'B' and line[2] == 'Y': # paper vs paper
        score += 3 # for a draw
        score += 2 # for choosing paper
    elif line[0] == 'C' and line[2] == 'Y': # scissors vs paper
        score += 2 # 0 points for loss, 2 for choosing paper

    elif line[0] == 'A' and line[2] == 'Z': # rock vs scissors
        score += 3 # 0 points for loss, 3 for choosing scissors
    elif line[0] == 'B' and line[2] == 'Z': # paper vs scissors
        score += 6 # for a win
        score += 3 # for choosing scissors
    elif line[0] == 'C' and line[2] == 'Z': # scissors vs scissors
        score += 3 # for a draw
        score += 3 # for choosing scissors
    
    return score

with open("/Users/nicholas/AoC2022/input.txt") as f:
    for line in f:
        line = line.strip()
        score += rock_paper_scissors(line)

print(score)