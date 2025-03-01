# Day 15
# Part 1 : 
# O(n)

from datetime import datetime
from re import findall
start_time = datetime.now()

FILE = f"input.txt"

def readFile(file):
    board = []
    moves = []

    with open(file, 'r') as f:
        # Read Board
        f.readline()
        
        current_line = f.readline()
        while current_line != "":
            if len(findall(r"(#){5,}",current_line)) == 0:
                board.append(list(current_line[1:len(current_line) - 2]))
            
                current_line = f.readline()
            else:
                break
        
        # Skip the empty line.
        f.readline()

        current_line = f.readline()
        while current_line != "":
            line_list = list(current_line)
            if '\n' in line_list:
                line_list.remove('\n')
            moves += line_list
            current_line = f.readline()

    return board,moves

def findStartPos():

    for y,row in enumerate(warehouse_layout):
        for x,element in enumerate(row):
            if element == '@':
                return [y,x]

directions = {
    '>':[0,1],
    'v':[1,0],
    '<':[0,-1],
    '^':[-1,0]
}

def processMoves(moves):
    current_pos = findStartPos()

    for move in moves:
        selected_direction = directions[move]
        ny = current_pos[0] + selected_direction[0]
        nx = current_pos[1] + selected_direction[1]
        if checkNextPosition('@',ny, nx, selected_direction):
            # Update current_pos
            warehouse_layout[current_pos[0]][current_pos[1]] = '.'
            #warehouse_layout[ny][nx] = '@'
            current_pos[0] += selected_direction[0]
            current_pos[1] += selected_direction[1]


        #for row in warehouse_layout:
        #    print(''.join(row))
        #print()

def checkNextPosition(current_char, y, x, current_direction):
    # check bounds 
    if y < 0 or x < 0 or y >= bounds[0] or x >=bounds[1]:
        return False
    elif warehouse_layout[y][x] == '#':
        return False
    elif warehouse_layout[y][x] == 'O':
        # Calculate next position
        ny = y + current_direction[0]
        nx = x + current_direction[1]
        if checkNextPosition('O',ny,nx, current_direction):
            warehouse_layout[ny][nx] = 'O'
            warehouse_layout[y][x] = current_char
            return True
    elif warehouse_layout[y][x] == '.':
        warehouse_layout[y][x] = current_char
        return True



def calculateGPS():
    total = 0

    for y,row in enumerate(warehouse_layout):
        for x,element in enumerate(row):
            if element == 'O':
                total += (100 * (y + 1)) + (x + 1)

    return total

def main():
    global warehouse_layout, bounds
    warehouse_layout, moves = readFile(FILE)
    bounds = [len(warehouse_layout), len(warehouse_layout[0])]
    processMoves(moves)
    #print(warehouse_layout)
    part1_total = calculateGPS()
    print(f"Part 1 total: {part1_total}")





main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")