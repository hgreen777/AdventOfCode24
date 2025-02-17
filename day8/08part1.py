#Day 8
#Part 1 :
# Wasted memory in hash table.
from datetime import datetime
start_time = datetime.now()

FILE = 'input.txt'

def readfile():
    # Assumes square input.
    nodes = [] # make a hash table
    for _ in range(123):
        nodes.append([])
    
    with open(FILE,'r') as file:
        line_count = 0
        for line in file:
            line_count += 1 # Square input 

            for index,char in enumerate(line.strip()):
                if char != '.':

                    nodes[ord(char)].append([index,line_count])

    return nodes

def find_size():
    with open(FILE,'r') as file:
        line = file.readline().strip()
        return len(line)

# <315
def find_total_antinodes(nodes,size):
    total = 0
    antinode_locations = set()
    for node_set in nodes:
        if len(node_set) != 0:
            for i in range(len(node_set)):
                for j in range(i+1,len(node_set)):
                    if node_set[i] == node_set[j]:
                        continue
                    else:
                        dx = node_set[j][0] - node_set[i][0]
                        dy = node_set[j][1] - node_set[i][1]

                        antinode_1 = [node_set[i][0] - dx, node_set[i][1] - dy]
                        antinode_2 = [node_set[j][0] + dx, node_set[j][1] + dy]

                        if antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] < size and antinode_1[1] < size:
                            if tuple(antinode_1) not in antinode_locations:
                                antinode_locations.add(tuple(antinode_1))
                                total += 1
                        if antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] < size and antinode_2[1] < size:
                            if tuple(antinode_2) not in antinode_locations:
                                antinode_locations.add(tuple(antinode_2))
                                total += 1
    
    return total


def main():
    nodes = readfile()
    size = find_size()
    
    total_antinodes = find_total_antinodes(nodes,size)

    print(f"Part 1 total: {total_antinodes}")


main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")