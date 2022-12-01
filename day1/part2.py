calories = []
current_calories = 0

top3 = []

with open("/Users/nicholas/AoC2022/day1/input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "": # empty lines to seperate elves
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)

for _ in range(3):
    top3.append(max(calories))
    calories.remove(max(calories)) # remove previous maximum value to find the next one

print(sum(top3))