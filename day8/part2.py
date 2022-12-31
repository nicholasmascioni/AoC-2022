trees = []
scenic_score = []

def check_above(tree_x, tree_y, height):
    above_trees = []
    score = 0

    for i in range(tree_x): # Above tree
        above_trees.append(int(trees[i][tree_y]))

    above_trees.reverse() # Order trees from closest to target tree to furthest

    for x, _ in enumerate(above_trees):
        if int(height) > above_trees[x]:
            score += 1
        elif int(height) == above_trees[x]:
            score += 1
            break
        else:
            score += 1
            break

    return score

def check_below(tree_x, tree_y, height):
    below_trees = []
    score = 0

    for i in range(tree_x + 1, len(trees)): # Below tree
        below_trees.append(int(trees[i][tree_y]))

    # No reverse necessary as trees are in correct order

    for x, _ in enumerate(below_trees):
        if int(height) > below_trees[x]:
            score += 1
        elif int(height) == below_trees[x]:
            score += 1
            break
        else:
            score += 1
            break

    return score

def check_left(tree_x, tree_y, height):
    left_trees = []
    score = 0

    for i in range(tree_y): # Left of tree
        left_trees.append(int(trees[tree_x][i]))

    left_trees.reverse() # Order trees from closest to target tree to furthest

    for x, _ in enumerate(left_trees):
        if int(height) > left_trees[x]:
            score += 1
        elif int(height) == left_trees[x]:
            score += 1
            break
        else:
            score += 1
            break

    return score

def check_right(tree_x, tree_y, height):
    right_trees = []
    score = 0

    for i in range(tree_y + 1, len(trees[0])): # Right of tree
        right_trees.append(int(trees[tree_x][i]))

    # No reverse necessary as trees are in correct order

    for x, _ in enumerate(right_trees):
        if int(height) > right_trees[x]:
            score += 1
        elif int(height) == right_trees[x]:
            score += 1
            break
        else:
            score += 1
            break

    return score

with open("day8/input.txt") as f:
    for line in f:
        trees.append(line.strip())

for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        if (i != 0 and i != len(trees) - 1) and (j != 0 and j != (len(trees[0]) - 1)): # Only check interior trees since edge trees will have a score of 0
            scenic_score.append((check_above(i, j, tree) * check_below(i, j, tree) * check_left(i, j, tree) * check_right(i, j, tree)))

print(max(scenic_score))