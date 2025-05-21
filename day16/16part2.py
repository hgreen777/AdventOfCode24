# Day 16 Part 2 > 572 (583)
from datetime import datetime
import time
from re import findall
import os
import sys 
import heapq

start_time = datetime.now()

FILE = f"test1_input.txt"

V = [] # Set of vertices -> Only available spots. 
dist = []
pred = []
line_length = 0
s = -1 # Start vector
e = -1 # Destination vector

#region reading_locating_start
with open(FILE, 'r') as f:
    lines = [line.rstrip('\n') for line in f]
    
    x = 0
    for l in lines:
        line_length = len(l)
        for char in l:
            if char == '.':
                V.append(x)
            elif char == 'S':
                s = x
                V.append(x)
            elif char == 'E':
                e = x
                V.append(x)
            x += 1
    
    if s == -1 or e == -1:
        print("Error")
        exit()         

directions = [
    -line_length,       # up
    1,                  # right
    line_length,        # down
    -1 
]


def dijkstras(V, end, start):
    # Find the optimum path returning the shortest-path-tree

    # Then backwards traverse through this treeto find all pathsthat could have been an optimal path
    return


        
def printing_path(path):
    with open(FILE, 'r') as f:
        lines = f.readlines()
        write_str = ""
        
        x = 0
        for l in lines:
            for char in l:
                if x in path:
                    write_str += 'O'
                else:
                    write_str += char

                x += 1
        
    return write_str
                
def distinct_nodes(all_paths):
    visited = []
    for path in all_paths:
        for v in path:
            if v not in visited:
                visited.append(v)

    return visited, len(visited)


def main():
    all_paths,cost = dijkstras(V,e,s)    
    print(all_paths)

    #for x in all_paths:
        #print(printing_path(x))

    print(cost)

    visited, total = distinct_nodes(all_paths)

    print(printing_path(visited))
    print(f"Part 2 total: {total}")

if __name__ == "__main__":
    main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")
