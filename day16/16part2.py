# Day 16 Part 2
# Plan on using Yen's K Shortest Path Algorithm
from datetime import datetime
import time
from re import findall
import os
import sys 

start_time = datetime.now()

FILE = f"test1_input.txt"

#Store Maze as a theoretical.
V = [] # Set of vertices -> Only available spots. 
s = -1 # Start vector
e = -1 # Destination vector
E = {} # Edges = ((v1,v2):c) <-- Wort work as turning
G = [V,E]

#region reading_locating_start
def readFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        
        x = 0
        for l in lines:
            for char in l:
                if char == '.':
                    V.append(x)
                elif char == 'S':
                    s = x
                elif char == 'E':
                    e = x

                x += 1
        
        if s == -1 or e == -1:
            print("Error")
            exit()
            



def main():
    readFile(FILE)
    print(V)
    print(s)
    print(e)
    
    total = 0
    print(f"Part 2 total: {total}")

if __name__ == "__main__":
    main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")
