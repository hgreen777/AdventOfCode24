#Day 6 part 2:1309
# 44 seconds for execution 
import copy
from datetime import datetime
start_time = datetime.now()

file_name = 'input.txt'

moves = [
    ['^',[-1,0]],
    ['>',[0,1]],
    ['v',[1,0]],
    ['<',[0,-1]]
]

def readBoard():

    board = []
    
    with open(file_name,'r') as file:
        for line in file:
            board.append([char for char in line.strip()])

    return board

def findStartPosition(board):
    # Returns y,x
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '^':
                return [i,j]

def mapAroute(board, start_position):
    route_coordinates = []
    selector = 0
    y = start_position[0]
    x = start_position[1]
    board[y][x] = 'X'
    while(True):
        try:
            if board[y][x] == 'X':
                y += moves[selector][1][0]
                x += moves[selector][1][1]
            elif board[y][x] == '.':
                board[y][x] = 'X'
                route_coordinates.append([y,x])
                y += moves[selector][1][0]
                x += moves[selector][1][1]
            elif board[y][x] == '#':
                y -= moves[selector][1][0]
                x -= moves[selector][1][1]
                selector = (selector + 1) % 4
            else:
                print(f"Error: {board[y][x]}")

        except Exception as e:
            print(f"Y:{y},X:{x} and {e} -> Exited the board")
            return route_coordinates

def checkLoop(updated_board, start_position):
    y = start_position[0]
    x = start_position[1]
    selector = 0
    y += moves[selector][1][0]
    x += moves[selector][1][1]

    while(True):
        try:
            if x < 0 or x >= len(updated_board[0]) or y < 0 or y >= len(updated_board):
                return False
            if updated_board[y][x] == '^' or updated_board[y][x] == '>' or updated_board[y][x] == 'v' or updated_board[y][x] =='<':

                y += moves[selector][1][0]
                x += moves[selector][1][1]
                if updated_board[y][x] == moves[selector][0]:
                    return True
            elif updated_board[y][x] == '.':

                updated_board[y][x] = moves[selector][0]
                y += moves[selector][1][0]
                x += moves[selector][1][1]
            elif updated_board[y][x] == '#':
                y -= moves[selector][1][0]
                x -= moves[selector][1][1]
                selector = (selector + 1) % 4

        except Exception as e:
            print(f"Y:{y},X:{x} and {e} -> Exited the board")
            return False


def main():
    board = readBoard()
    print(len(board),len(board[0]))
    loops = 0
    start_position = findStartPosition(board)

    board_copy = copy.deepcopy(board)
    potential_obstructions = mapAroute(board_copy, start_position)


    for obstruction in potential_obstructions:
        try:
            new_board = copy.deepcopy(board)
            new_board[obstruction[0]][obstruction[1]] = '#'
            if checkLoop(new_board, start_position):
                loops += 1
        except Exception as e:
            print(f"{e}, {obstruction}")

    print(f"Part 2: {loops}/{len(potential_obstructions) + 1}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")