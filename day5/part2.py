stacks = [['G', 'D', 'V', 'Z', 'J', 'S', 'B'],      # Stacks 1-9 from bottom to top
          ['Z', 'S', 'M', 'G', 'V', 'P'],
          ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
          ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
          ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
          ['R', 'G', 'C', 'D'],
          ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
          ['P', 'F', 'V'],
          ['D', 'R', 'S', 'T', 'J']]

instructions = []

def crane(amount, position, destination):
    temp_stack = []
    for _ in range(amount):
       temp = stacks[position-1].pop(-1)
       temp_stack.append(temp)

    temp_stack.reverse() # Puts the crates back in their original order

    for i in range(len(temp_stack)):
        stacks[destination-1].append(temp_stack[i])

    return stacks 

with open("/Users/nicholas/AoC2022/day5/input.txt") as f:
    for line in f:
        line = line.strip()
        instructions.append(line)

del instructions[0:10] # Instructions start on line 11

for instruction in instructions:
    instruction = instruction.split()
    crane(int(instruction[1]), int(instruction[3]), int(instruction[5]))

for i in range(9):
    print(stacks[i][-1], end='')