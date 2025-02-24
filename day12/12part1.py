# Day 12
# Part 1 : 1473276 

from datetime import datetime
start_time = datetime.now()

FILE = f"input.txt"

def readFile(file):
    map = []

    with open(file,'r') as f:
        for line in f:
            map.append([char for char in line.strip()])
    
    global max_width, max_length
    max_width = len(map[0])
    max_length = len(map)
    return map

directions = [
    [-1, 0],  # Up
    [0, 1],   # Right
    [1, 0],   # Down
    [0, -1]   # Left
]

def findDimension(current_letter, y, x, current_dimension):  # current_dimension = [perimeter, area]
    garden_map[y][x] = garden_map[y][x].lower()
    current_dimension[1] += 1
    for direction in directions:
        new_y = y + direction[0]
        new_x = x + direction[1]
        if new_y < 0 or new_y >= max_length or new_x < 0 or new_x >= max_width:
            # Out of bounds
            current_dimension[0] += 1
            continue

        next_character = garden_map[new_y][new_x]

        if current_letter.lower() == next_character:
            continue
        elif current_letter.upper() == next_character:
            current_dimension = findDimension(next_character, new_y, new_x, current_dimension)
        elif current_letter.upper() != next_character.upper():  # Same as else 
            current_dimension[0] += 1

    return current_dimension


def analyseMap(map):
    dimensions = []

    for y,line in enumerate(map):
        for x,char in enumerate(line):
            if char != char.lower(): # is char is not lowercase
                dimensions.append(findDimension(char,y,x,[0,0]))

    return dimensions

def calculatePrice(dimensions):
    total = 0 

    for dimension in dimensions:
        total += dimension[0] * dimension[1]

    return total

def main():
    global garden_map
    garden_map = readFile(FILE)
    dimensions = analyseMap(garden_map)
    total_price = calculatePrice(dimensions)
    print(f"Part 1 total: {total_price}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")