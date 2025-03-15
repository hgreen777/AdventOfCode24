# Day 16
# Part 1 : 135536
from datetime import datetime
import time
from re import findall
import os
import sys 

start_time = datetime.now()

FILE = f"test1_input.txt"

#region reading_locating_start
def readFile(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            board.append([x for x in line.strip()])
    return board

def findStart(board):
    for y,line in enumerate(board):
        for x,char in enumerate(line):
            if char == 'S':
                return [y,x]
    return None

def findDestination(board):
    for y,line in enumerate(board):
        for x,char in enumerate(line):
            if char == 'E':
                return (y,x)


def findAvailableSpaces(maze):
    spaces = list()
    spaces.append(tuple(findStart(maze)))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '.' or maze[y][x] == 'S' or maze[y][x] == 'E':
                spaces.append((y,x))

    return spaces
#endregion

directions = [
    [-1,0], # ^
    [0,1], # >
    [1,0], # v
    [0,-1] # <
]

def leastUnexploredVertex(explored, distances):
    min_distance = sys.maxsize
    min_index = -1
    for i in range(len(distances)):
        if not explored[i] and distances[i] < min_distance:
            min_distance = distances[i]
            min_index = i
    return min_index

def findFastestRoute(available_spaces, start_pos):
    # Dijiksta's Algorithm kindoff
    # Input set of available spaces (Vertices) 
    # 
    goal = tuple(findDestination(maze))
    queue =  [(0,start_pos,[])] # (cost, node, path)
    print(queue)
    # Distance to that node 
    dist = {}
    dist[tuple(start_pos)] = 0

    # Stores all optimal paths
    paths = {}
    paths[tuple(start_pos)] = [[]]

    while len(queue) != 0:
        #  Find node with the smallest cost (linear search)
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
    
        (current_cost, current_node, current_path) = queue.pop(min_index)

        current_path = current_path + [current_node]

        if current_node == goal:
            continue

        for neighbour in findAvailableAround(available_spaces,available_spaces.index(tuple(current_node))):
            move_cost = calculateCost(available_spaces, available_spaces.index(tuple(current_node)), neighbour)
            new_cost = current_cost + move_cost

            if neighbour not in dist or new_cost < dist[neighbour]:
                dist[neighbour] = new_cost
                queue.append((new_cost,available_spaces[neighbour],     current_path))
                paths[neighbour] = [current_path]
            elif new_cost == dist[neighbour]:
                paths[neighbour].append(current_path)


    return paths[goal]


def findAvailableAround(available, v):
    current = available[v]
    l = list()
    for dir in directions:
        check = (current[0] + dir[0], current[1] + dir[1])
        if check in available:
            l.append(available.index(check))
    return l

def calculate_if_turn(space0,space1, space2): 
    # Input: Space0 = Space before current one, Space1: current space, Space2 := next space, direction := current travel
    # Can be calculated either using "3 nodes to identify corneer"
    # or using direction
    # Get current direction
    dy1 = space1[0] - space0[0]
    dx1 = space1[1] - space0[1]
    dy2 = space2[0] - space1[0]
    dx2 = space2[1] - space1[1]

    if [dy1,dx1] != [dy2,dx2]:
        return 1001
    else:
        return 1


def printBoard(board):
    for line in board:
        print(''.join(line))
    print()   

def printIndexMoves(all_spaces,indexs,board):
    indexs.reverse()
    for i in indexs:
        board[all_spaces[i][0]][all_spaces[i][1]] = '@'

    printBoard(board)
    
def printMoves(moves,board):
    # Accept a copy of the board
    for move in moves:
        board[move[0]][move[1]] = '@'
        printBoard(board)
        time.sleep(0.2)



def main():
    global maze
    maze = readFile(FILE)
    #print("Starting Maze")
    #printBoard(maze)
    #[y,x] = findStart(maze)
    #print(y,x)
    spaces = findAvailableSpaces(maze)
    total = findFastestRoute(spaces, findStart(maze))
    print(maze)
    print(total)
    print(f"Part 1 total: {total}")

if __name__ == "__main__":
    main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")
