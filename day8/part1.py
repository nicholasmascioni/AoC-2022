trees = []
visible_trees = []

def check_above(tree_x, tree_y, height):
    above_trees, confirmed_trees = [], []

    for i in range(tree_x): # Above tree
        above_trees.append(trees[i][tree_y])

    for tree in above_trees:
        if height > tree:
            confirmed_trees.append(tree)

    if len(confirmed_trees) == len(above_trees): # Current tree is taller than all trees above it
        return True

def check_below(tree_x, tree_y, height):
    below_trees, confirmed_trees = [], []

    for i in range(tree_x + 1, len(trees)): # Below tree
        below_trees.append(trees[i][tree_y])

    for tree in below_trees:
        if height > tree:
            confirmed_trees.append(tree)

    if len(confirmed_trees) == len(below_trees): # Current tree is taller than all trees below it
        return True

def check_left(tree_x, tree_y, height):
    left_trees, confirmed_trees = [], []

    for i in range(tree_y): # Left of tree
        left_trees.append(trees[tree_x][i])

    for tree in left_trees:
        if height > tree:
            confirmed_trees.append(tree)

    if len(confirmed_trees) == len(left_trees): # Current tree is taller than all trees to the left of it
        return True

def check_right(tree_x, tree_y, height):
    right_trees, confirmed_trees = [], []

    for i in range(tree_y + 1, len(trees[0])): # Right of tree
        right_trees.append(trees[tree_x][i])

    for tree in right_trees:
        if height > tree:
            confirmed_trees.append(tree)

    if len(confirmed_trees) == len(right_trees): # Current tree is taller than all trees to the right of it
        return True

with open("day8/input.txt") as f:
    for line in f:
        trees.append(line.strip())

for i, row in enumerate(trees):
    if i == 0 or i == (len(trees) - 1): # Top or bottom edge
        visible_trees.extend(row)
    for j, tree in enumerate(row):
        if (i != 0 and i != (len(trees) - 1)) and (j == 0 or j == (len(row) - 1)): # Left or right edge
            visible_trees.append(tree)
        elif (i != 0 and i != len(trees) - 1) and (j != 0 and j != (len(trees[0]) - 1)): # Interior trees
            if check_above(i, j, tree) or check_below(i, j, tree) or check_left(i, j, tree) or check_right(i, j, tree):
                visible_trees.append(tree)
            
print(len(visible_trees))