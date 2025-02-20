#Day 9
#Part 2 : 6415163624282
# O(n + (n * n/2) + n*x) -> O(n^2) 
# where x is total pages and n is partitions for the disk.
# O(readfile + move file + checksum)
# use set 
from datetime import datetime
start_time = datetime.now()

FILE = 'input.txt'

def readfile():
    # O(n)
    array = []
    current_file_id = 0 
    with open(FILE, 'r') as file:
        for line in file:
            for index,char in enumerate(line):
                if index % 2 == 0: # File
                    array.append(f"{current_file_id}:{char}")
                    current_file_id += 1
                else:
                    array.append(char)
    return array

def moveFiles(disk):
    # Assumes non-empty input
    #O(n * n/2 -> (n^2)/2)

    next_file_index = 0
    l = len(disk)
    
    if (l % 2) == 0: # Even
        files = l / 2
    else:
        files = (l + 1) / 2

    all_files_left = [i for i in range(int(files))]
    
    all_files_left.reverse()


    for i in range(l):
        
        if len(all_files_left) < 0:
            break

        if ':' in disk[i]:
            # File is fine
            try:
                
                all_files_left.remove(int(disk[i].split(':')[0]))
            except Exception as e:
                print(all_files_left)
                print(f"{disk[i].split(':')[0]} and {e}")
            continue
        else:
            available_space = int(disk[i]) 

            for next_file_index in all_files_left:
                required_space = int(disk[2*next_file_index].split(':')[1])
                if available_space > 0:
                    if required_space > available_space:
                        # Nothing is moved 
                        # Check next file 
                        continue
                    elif required_space < available_space:
                        if ':' in disk[i]:
                            disk[i] += f"{next_file_index}:{required_space},"
                        else:
                            disk[i] = f"{next_file_index}:{required_space},"
                        available_space -= required_space
                        all_files_left.remove(next_file_index)
                        disk[2*next_file_index] = f"{required_space}"
                        # Check all the rest of the files
                    else: # They are equal
                        if ':' in disk[i]:
                            disk[i] += f"{next_file_index}:{required_space},"
                        else:
                            disk[i] = f"{next_file_index}:{required_space},"
                        disk[2*next_file_index] = f"{required_space}"
                        all_files_left.remove(next_file_index)
                        available_space -= required_space # Should be 0
                else:
                    break
            
            if available_space > 0 and ':' in disk[i]:
                disk[i] += f"{available_space}"

    return disk
            
    # Start with the first file, if the disk spot is mean to be a file, write it there [from end of the list] [if it is still in list of files to be written]. Remove from files to be written array.
    # then for each free space 
        # while available space, not finished (need to make sure method works with checksum (ie update all empty space)), list has files in it else add end and exit
        # if available_space < required_space:
        #   Move onto next file 
        # elif availble_space > required_space:
        #   write the file & remove from list
        #   update available space 
        #   move onto next file
        # else # they equal
        #   write file & remove from list
        #   available space = 0 Therefore exiting list 

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
            if part != '' and ':' in part:
                page = part.split(':') # Split id and space_required
                for i in range(int(page[1])):
                    total += current_index * int(page[0])
                    current_index += 1
            elif part != '' and int(part) > 0:
                for i in range(int(part)):
                    current_index += 1


    return total

def main():
    disk_input = readfile()
    updated_disk = moveFiles(disk_input)
    part_2_total = checksum(updated_disk)

    print(f"Part 2 total: {part_2_total}")


main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")