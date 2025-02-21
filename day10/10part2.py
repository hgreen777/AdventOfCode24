#Day 10
#Part 2 : 1045
# O(n + 1 + x*9*4) -> O(n + 1 + 36x) -> O(n+ 1 + 1) -> O(n + 1) -> O(n)
# where x is number of trailheads -> finite constant < n

# SO turns out i was solving part 2 for part 1, so the part i was struggling with on part 1 was likely a misunderstanding of the task/edge case.

# DFS with backtracking to optimise
from datetime import datetime
start_time = datetime.now()

FILE = 'input.txt'

def readfile(array):
    # O(n)
    trailheads = []
    with open(FILE, 'r') as file:
        for y,line in enumerate(file):
            line = line.strip()
            map_line = []
            for x,char in enumerate(line):
                map_line.append(int(char))

                if char == '0':
                    trailheads.append([y,x])
            
            array.append(map_line)

    return trailheads

def findBounds(array):
    #Assumes rectangle
    global max_coords
    max_coords = [len(array),len(array[0])]

def findMaximumTrailScore(trailheads):
    total = 0

    # Iterate over every start
    for start in trailheads:
        current_coords = [start[0],start[1]]
        total += checkPosition(current_coords, 0)

    return total


# Outside recursive function to reduce memory trace. 
# Cannot go diagonal
surrounding_positions = [
        [-1,0], # Straight up
        [0,1], # Right
        [1,0], # Down
        [0,-1] # Left
]

def checkPosition(current_coords, counter):

    for move in surrounding_positions:
        next_coords = [current_coords[0] + move[0], current_coords[1] + move[1]]

        if next_coords[0] < 0 or next_coords[0] >= max_coords[0] or \
           next_coords[1] < 0 or next_coords[1] >= max_coords[1]:
            # Co-ords out of range.
            continue

        if map[current_coords[0]][current_coords[1]] == 9:
            return counter + 1

        if map[next_coords[0]][next_coords[1]] == (map[current_coords[0]][current_coords[1]] + 1):
            # Move to next co-ord
            counter = checkPosition(next_coords, counter)

    return counter

        




def main():
    global map # Global so reference isn't passed into every recursive function call
    map = []
    trailheads = readfile(map)
    findBounds(map) # Creates global var so it can be accessed in recursive function without passing reference in each function call
    sum = findMaximumTrailScore(trailheads)

    print(f"Part 2 total: {sum}")

main()


end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")