datastream = []
packet = []

def no_duplicates(list):
    if len(list) == len(set(list)): # Lengths will be the same if all characters are unique
        return True
    else:
        return False

with open("day6/input.txt") as f:
    datastream = list(f.read().rstrip())

for i in range(len(datastream)):
    packet.append(datastream[i])

    if len(packet) == 4:
        if no_duplicates(packet):
            print(i+1) # Add 1 to get the character after the first marker
            break
        else:
            packet.pop(0) # Remove the first element to continue checking 4 characters at a time