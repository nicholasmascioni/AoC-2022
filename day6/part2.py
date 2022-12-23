datastream = []
message = []

def no_duplicates(list):
    if len(list) == len(set(list)): 
        return True
    else:
        return False

with open("day6/input.txt") as f:
    datastream = list(f.read().rstrip())

for i in range(len(datastream)):
    message.append(datastream[i])

    if len(message) == 14: # Only real change for this part
        if no_duplicates(message):
            print(i+1)
            break
        else:
            message.pop(0) 