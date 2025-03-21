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

# [set(),0]
def analyseRegion(current_region_letter, y,x, perimeter_area): # perimeter_area = [ [ [[y,x],'TOP'],[] ] , x]   'TOP','BOTTOM','LEFT','RIGHT'
    garden_map[y][x] = garden_map[y][x].lower()
    perimeter_area[1] += 1

# 'Location':(y,x),'border_type':'UP'
    for dir_index,dir in enumerate(directions):
        ny = y + dir[0]
        nx = x + dir[1]

        if ny < 0:
            # Top Border
            perimeter_area[0].add((y, x, 'UP'))
            continue
        elif ny >= max_length:
            perimeter_area[0].add((y, x, 'BOTTOM'))
            continue
        elif nx < 0:
            perimeter_area[0].add((y, x, 'LEFT'))
            continue
        elif nx >= max_width:
            perimeter_area[0].add((y, x, 'RIGHT'))
            continue

        next_character = garden_map[ny][nx]

        if current_region_letter.lower() == next_character:
            # No border, another region.
            continue
        elif current_region_letter.upper() == next_character:
            # No border, another letter in region.
            perimeter_area = analyseRegion(next_character, ny, nx, perimeter_area)
        elif current_region_letter.upper() != next_character.upper():
            # Differentiate the region_perimeter types
            if dir_index == 0: # UP
                perimeter_area[0].add((y,x,'UP'))
            elif dir_index == 1:
                perimeter_area[0].add((y,x,'RIGHT'))
            elif dir_index == 2:
                perimeter_area[0].add((y,x,'BOTTOM'))
            elif dir_index == 3:
                perimeter_area[0].add((y,x,'LEFT'))

    return perimeter_area



def calculateSides(region_perimeter):
    total_region_sides = 0
    region_perimeter = sorted(list(region_perimeter), key=lambda x: (x[2], x[0], x[1]))

    # Divide and conquer to make if n/2 for n =len(region_perimeter)

    while len(region_perimeter) > 0:
        cy, cx, type = region_perimeter[0]
        region_perimeter.remove(region_perimeter[0])
        
        if type in ['UP', 'BOTTOM']:
            nx = cx + 1
            while nx <= max_width:
                if (cy, nx, type) in region_perimeter:
                    region_perimeter.remove((cy, nx, type))
                    nx += 1
                else:
                    total_region_sides += 1
                    break
        elif type in ['LEFT', 'RIGHT']:
            ny = cy + 1
            while ny <= max_length:
                if (ny, cx, type) in region_perimeter:
                    region_perimeter.remove((ny, cx, type))
                    ny += 1
                else:
                    total_region_sides += 1
                    break
    

        # Need to organise and get the next smallest 

    return total_region_sides


def analyseMap(map):
    dimensions = []

    for y,line in enumerate(map):
        for x,char in enumerate(line):
            if char != char.lower(): # is char is not lowercase (ie not visited)
                perimeter_area = analyseRegion(char,y,x,[set(),0])
                sides = calculateSides(perimeter_area[0])
                dimensions.append([sides,perimeter_area[1]])

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
    print(f"Part 2 total: {total_price}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")