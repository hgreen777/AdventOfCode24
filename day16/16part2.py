# Day 16 Part 2
# Plan on using Yen's K Shortest Path Algorithm
from datetime import datetime
import time
from re import findall
import os
import sys 
import heapq

start_time = datetime.now()

FILE = f"test1_input.txt"

#Store Maze as a theoretical.
V = [] # Set of vertices -> Only available spots. 
dist = []
pred = []
line_length = 0
s = -1 # Start vector
e = -1 # Destination vector

#region reading_locating_start
with open(FILE, 'r') as f:
    lines = f.readlines()
    
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
    -1                  # left
]


def dijkstras(V,s,e):
    V = set(V)
    dist = {}
    predecessors = {}
    priority_queue = []

    for d in directions:
        dist[(s,d)] = 0
        predecessors[(s,d)] = [None]
        heapq.heappush(priority_queue, (0,s,d))

    # Single-source : Finds shortest path to all nodes.

    #dist = {node:float('inf') for node in V}
    #predecessors = {node: [] for node in V}

    
    while priority_queue:
        current_dist, current_node, current_dir = heapq.heappop(priority_queue)

        #if current_dist > dist[current_node]:
        #    continue
        if dist[(current_node, current_dir)] < current_dist:
            continue
    
        # Neighbours 
        for d in directions:
            if d == current_dir:
                new_dist = current_dist + 1
            else:
                new_dist = current_dist + 1001

            neighbour = d + current_node

            # Check if neighbour exist:
            if neighbour not in V:
                continue

            
            state = (neighbour,d)
            if state not in dist or new_dist < dist[state]:
                dist[state] = new_dist
                predecessors[state] = [(current_node,current_dir)]
                heapq.heappush(priority_queue, (new_dist, neighbour, d))
            elif new_dist == dist[state]:
                predecessors[state].append((current_node,current_dir))
            
    min_cost = float('inf')
    end_states = []
    for d in directions:
        state = (e, d)
        if state in dist:
            if dist[state] < min_cost:
                min_cost = dist[state]
                end_states = [state]
            elif dist[state] == min_cost:
                end_states.append(state)
           
    
    # Backtrack to find the shortest paths from start to end
    all_paths = []
    def find_paths(state, path):
        node, direction = state
        if node == s:
            all_paths.append([s] + path)
            return
        
        for pred in predecessors[state]:
            if pred is not None:
                find_paths(pred, [node] + path)
    
    for end_state in end_states:
        find_paths(end_state, [])
    return all_paths, min_cost


        
def printing_path(path):
    with open(FILE, 'r') as f:
        lines = f.readlines()
        write_str = ""
        
        x = 0
        for l in lines:
            line_length = len(l)
            for char in l:
                if x in path:
                    write_str += 'A'
                else:
                    write_str += char

                x += 1
        
    return write_str
                



def main():
    all_paths,cost = dijkstras(V,s,e)    
    print(all_paths)

    print(printing_path(all_paths[0]))
    print(cost)
    total = 0
    print(f"Part 2 total: {total}")

if __name__ == "__main__":
    main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")
