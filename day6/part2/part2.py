#Day 6 part 2
import copy
moves = [
    ['^',[-1,0]],
    ['>',[0,1]],
    ['v',[1,0]],
    ['<',[0,-1]]
]

def readBoard():

    board = []
    
    with open('testInput.txt','r') as file:
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
                    with open('output.txt', 'a') as file:
                        for lines in updated_board:
                            line_str = ""
                            for x in lines:
                                line_str += str(x)
                            line_str += '\n'
                            file.write(line_str)
                        file.write('\n')
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

    with open('output.txt', 'w') as file:
        for lines in board:
            line_str = ""
            for x in lines:
                line_str += str(x)
            line_str += '\n'
            file.write(line_str)
        file.write('\n')

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

    print(f"Part 2: {loops}/{len(potential_obstructions) + 1} <- Should be 6")

main()
