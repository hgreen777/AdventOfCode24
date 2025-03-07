# Day 15
# Part 2 : 1547508 < x > 1552537 > 1571055, x = 1550677.0
# O(n)
# Cannot change read file to map onto signle blocks due to pushing move. However read will have to be changed
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
                row = list(current_line[1:len(current_line) - 2])

                new_row = row.copy()
                i = 0
                while i < len(new_row):
                    element = new_row[i]
                    if element == '#':
                        new_row.insert(i,'#')
                    elif element == '.':
                        new_row.insert(i,'.')
                    elif element == 'O':
                        new_row[i] = ']'
                        new_row.insert(i,'[')
                    elif element == '@':
                        new_row.insert(i+1,'.')
                    i += 2



                board.append(new_row)
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
    #print(moves)
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
    global blocks_to_move

    for i,move in enumerate(moves):
        selected_direction = directions[move]
        ny = current_pos[0] + selected_direction[0]
        nx = current_pos[1] + selected_direction[1]
        if ny < 0 or nx < 0 or ny >= bounds[0] or nx >=bounds[1]:
            continue
        blocks_to_move = []
        try:
            if checkNextPosition(ny, nx, selected_direction):
                # Update current_pos
                warehouse_layout[current_pos[0]][current_pos[1]] = '.'
                current_pos[0] += selected_direction[0]
                current_pos[1] += selected_direction[1]
                warehouse_layout[current_pos[0]][current_pos[1]] = '@'
                # move all the tiles in list
                moveTiles(selected_direction)
        except Exception as e:
            for i,row in enumerate(warehouse_layout):
                print(''.join(row))
            print()
            print(i)
            print(move)
            print(ny,nx)
            #return


        #if move == '^':
        #print(move)
        #print(blocks_to_move)
        #for row in warehouse_layout:
        #    print(''.join(row))
        #print()

def checkNextPosition(y, x, current_direction):

    # check bounds 
    if y < 0 or x < 0 or y >= bounds[0] or x >=bounds[1]:
        return False
    elif warehouse_layout[y][x] == '#':
        return False
    elif warehouse_layout[y][x] == '.':
        return True
    
    elif warehouse_layout[y][x] == '[': 
        if current_direction[1] != 0: # Horizontal
            # Has to be right
            blocks_to_move.append([y,x])
            if checkNextPosition(y,x + 2*current_direction[1], current_direction):
                return True
        elif current_direction[0] != 0: # Vertical
            blocks_to_move.append([y,x])
            if checkNextPosition(y+current_direction[0],x, current_direction) and checkNextPosition(y+current_direction[0],x+1, current_direction):
                return True
    elif warehouse_layout[y][x] == ']':
        if current_direction[1] != 0: # Horizontal
            blocks_to_move.append([y,x - 1])
            if checkNextPosition(y,x +2*current_direction[1] , current_direction):
                return True
        elif current_direction[0] != 0: # Vertical
            blocks_to_move.append([y,x-1])
            if checkNextPosition(y+current_direction[0],x, current_direction) and checkNextPosition(y+current_direction[0],x-1, current_direction):
                return True
        
    return False


def moveTiles(current_direction):

    blocks_to_move.reverse()
    for block in blocks_to_move:
        # [y,x]

        warehouse_layout[block[0]][block[1]] = '.'
        warehouse_layout[block[0]][block[1]+1] = '.'

        warehouse_layout[block[0] + current_direction[0]][block[1] + current_direction[1]] = '['
        warehouse_layout[block[0] + current_direction[0]][block[1] + current_direction[1] + 1] = ']'


def calculateGPS():
    total = 0

    for y,row in enumerate(warehouse_layout):
        for x,element in enumerate(row):
            if element == '[' and warehouse_layout[y][x+1] == ']':
                total += (100 * (y + 1)) + (x + 2)

    return total

def main():
    global warehouse_layout, bounds
    warehouse_layout, moves = readFile(FILE)
    bounds = [len(warehouse_layout), len(warehouse_layout[0])]
    for row in warehouse_layout:
        print(''.join(row))
    print()
    processMoves(moves)
    for row in warehouse_layout:
        print(''.join(row))
    print()
    part1_total = calculateGPS()
    print(f"Part 2 total: {part1_total}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")