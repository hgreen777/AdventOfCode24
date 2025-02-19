#Day 9
#Part 1 : 6385338159127
# O(3n) -> O(n)
# Not very memory efficient requiring alot of contiguous memory but only 1char per array spacing
from datetime import datetime
start_time = datetime.now()

FILE = 'input.txt'

def readfile():
    # O(n)
    array = []
    with open(FILE, 'r') as file:
        for line in file:
            for char in line:
                array.append(char)
    return array

def moveFiles(disk):
    # Assumes non-empty input
    #O(n)

    next_file_index = 0
    current_file_id = 0
    l = len(disk)
    
    if (l % 2) == 0: # Even
        files = l / 2
        last_file_index = l - 2
    else:
        files = (l / 2) + 1
        last_file_index = l - 1
    
    print(files)
    last_file_id = int(files) - 1

    for i in range(l):
        if i == next_file_index:
            disk[i] = f"{current_file_id}:{disk[i]}"
            current_file_id += 1
            next_file_index += 2
        else:
            # Empty space 
            # Move the last file into all the current space 
            available_space = int(disk[i])
            disk[i] = ''

            # Keep moving on adding files into the gap until either the break is reached or available space is gone.
            while (current_file_id <= last_file_id and available_space > 0):
                required_space = int(disk[last_file_index])

                if available_space < required_space:
                    disk[i] += f"{last_file_id}:{available_space}"
                    # Update last file to reflect spacing
                    disk[last_file_index] = str(required_space - available_space)
                    break
                elif available_space > required_space:
                    # Firstly, add that file in the gap
                    disk[i] += f"{last_file_id}:{required_space},"
                    available_space -= required_space
                    last_file_id -= 1
                    last_file_index -= 2
                
                else: # available_space == required_space
                    disk[i] += f"{last_file_id}:{available_space}"
                    last_file_id -= 1
                    last_file_index -= 2
                    break
        
        if current_file_id > last_file_id:
            # Insert break character
            disk[i+1] = '-1'
            break # End of block has been found

    return disk

def checksum(input):
    # Check if input valid
    # O(n)
    total = 0
    current_index = 0
    for i in range(len(input)):
        # Check for stopping key
        if input[i] == '-1':
            return total
        
        partition = input[i].split(',') # Split on comma where more then one file is kept in the same partition.
        for part in partition:
            if part != '':
                page = part.split(':') # Split id and space_required
                for i in range(int(page[1])):
                    total += current_index * int(page[0])
                    current_index += 1

    return total

def main():
    disk_input = readfile()
    updated_disk = moveFiles(disk_input)
    part_1_total = checksum(updated_disk)
    print(f"Part 1 total: {part_1_total}")

main()


end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")