# Day 16
# Part 1 : Clean code add an output, make it more efficient 
from datetime import datetime
import time
from re import findall
import os
import sys 

start_time = datetime.now()

FILE = f"input.txt"

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
            if maze[y][x] == '.':
                spaces.append((y,x))

    return spaces

def calculate_if_turn(space0,space1, space2): 
    direction = None
    # Input: Space0 = Space before current one, Space1: current space, Space2 := next space, direction := current travel
    # Can be calculated either using "3 nodes to identify corneer"
    # or using direction
    if direction and space1 and space2:
        dy = space2[0] - space1[0]
        dx = space2[1] - space1[1]
        if direction != [dy,dx]:
            return 1001
        else:
            return 1
    elif space0 and space1 and space2:
        # Get current direction
        dy1 = space1[0] - space0[0]
        dx1 = space1[1] - space0[1]
        dy2 = space2[0] - space1[0]
        dx2 = space2[1] - space1[1]

        if [dy1,dx1] != [dy2,dx2]:
            return 1001
        else:
            return 1
    else:   
        raise Exception("Invalid Arguments")



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

    destination = findDestination(maze)
    available_spaces.append(start_pos)
    available_spaces.append(destination)
    dist = [sys.maxsize for _ in available_spaces]
    prev = [None for _ in available_spaces]
    explored = [False for _ in available_spaces]

    dist[available_spaces.index(start_pos)] = 0

    while explored[len(explored)-1] == False:
        v = leastUnexploredVertex(explored,dist) # Index of that vertex
        explored[v] = True
        # Get the set of available spaced around it 
        available_around = findAvailableAround(available_spaces,v) # -> indexes of the vertexes around it


        for w in available_around:
            if prev[v] is not None:
                cost = calculate_if_turn(available_spaces[prev[v]], available_spaces[v], available_spaces[w])
            else:
                cost = 1
            #cost = calculateCost(available_spaces, v, w, prev[v], directions[prev[v]] if prev[v] is not None else None)
            if dist[v] + cost < dist[w]:
                dist[w] = dist[v] + cost
                prev[w] = v
    
    path = []
    u = prev[len(prev) - 1] # The one before the final
    while u is not len(prev) -2: #len(prev)-2 is the start
        path.append(u)
        if prev[u] is None:
            break
        u = prev[u]
    
    # Check if the one right next to the start is in available.
    right_space = (start_pos[0],start_pos[1]+1)
    if right_space in available_spaces:
        if available_spaces.index(right_space) not in path:
            dist[len(dist) - 1] += 1000
    else:
        dist[len(dist) - 1] += 1000

    printIndexMoves(available_spaces,path,maze.copy())
    print(dist[len(dist) - 1])
    return dist[len(dist) - 1]

def findAvailableAround(available, v):
    current = available[v]
    l = list()
    for dir in directions:
        check = (current[0] + dir[0], current[1] + dir[1])
        if check in available:
            l.append(available.index(check))
    return l



def calculateCost(available_spaces, v, w, prev=None, direction=None):
    # Calculate the cost
    if prev is not None:
        if calculate_if_turn(available_spaces[prev], available_spaces[v], available_spaces[w], direction):
            return 1001
    return 1


def calculateScore(moves):
    # Calculate turns here.
    for move in moves:
        return 0 


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
    print("Starting Maze")
    printBoard(maze)
    #[y,x] = findStart(maze)
    #print(y,x)
    spaces = findAvailableSpaces(maze)
    findFastestRoute(spaces, findStart(maze))

if __name__ == "__main__":
    main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")