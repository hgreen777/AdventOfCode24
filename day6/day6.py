# Day 6
# Part 1: 4515
# Part 2:
from datetime import datetime
start_time = datetime.now()

board = []

with open('testInput.txt','r') as file:
    for line in file:
        board.append([char for char in line.strip()])


i=0
j=0
current_location = [i,j]
distinct_positions = 0
loop_obstructions = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '^':
            current_location = [i,j]
            i = len(board)
            break

print(f"Current Location of guard: {current_location}")

# All different directions for guards including how that effects their next move.
type_effect = [
    ['^',[-1,0]],
    ['>',[0,1]],
    ['v',[1,0]],
    ['<',[0,-1]]
]
# Selects the current way the guard is facing and where it will move next.
effect_selector = 0

# Change to symbols with stronger semantic alternative.
y = current_location[0]
x = current_location[1]

# Remove the "^" from board to elimitate any error edge cases -> is not needed as it replaced with effect slector.
board[y][x] = '^'
distinct_positions += 1

# Whilsts guard is on board
# > 550
while (True):
    try:
        if board[y][x] == '^' or board[y][x] == '>' or board[y][x] == 'v' or board[y][x] =='<':
            # Not distinct, move to next square.     
            y += type_effect[effect_selector][1][0]
            x += type_effect[effect_selector][1][1]

            # Suggests a loop
            if board[y][x] == type_effect[effect_selector][0]:
                loop_obstructions += 1
        elif board[y][x] == '.':
            # Distinct space.
            distinct_positions +=1
            board[y][x] = type_effect[effect_selector][0]
            y += type_effect[effect_selector][1][0]
            x += type_effect[effect_selector][1][1]
        elif board[y][x] == '#':
            # Rotate on new direction
            y -= type_effect[effect_selector][1][0]
            x -= type_effect[effect_selector][1][1]
            effect_selector = (effect_selector + 1) % 4
        else:
            print("Error" + board[y][x])
            
    except Exception as e:
        # Error is most likely out of bounds and therefore guard has left area.
        print(f"Y:{y},X:{x} and {e}")
        break

# Go through again or go back 
with open('output.txt', 'w') as file:
    for lines in board:
        line_str = ""
        for x in lines:
            line_str += str(x)
        line_str += '\n'
        file.write(line_str)
    
#look for perpendicular lines

print(f"Part 1: {distinct_positions}")
print(f"Part 2: {loop_obstructions}")
current_location = [y,x]
print(f"Current Location of guard (where they left board): {current_location}")
    

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")