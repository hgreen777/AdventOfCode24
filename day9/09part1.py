#Day 9
#Part 1 : 
# O(<3n) -> O(n)
# Not very memory efficient requiring alot of contiguous memory but only 1char per array spacing
from datetime import datetime
start_time = datetime.now()

FILE = 'test_input.txt'

def readfile():
    # O(n)
    array = []
    with open(FILE, 'r') as file:
        for line in file:
            for char in line:
                array.append(char)
    return array

def processInput(disk_input):
    # TODO : Expand the input out into its designated format with spaces (or consider a way to stop this)
    # O(n)
    # Might be able to ignore if when "moving files" just remember, odd indexes are files, even is spacing '.'
    return 0 

def moveFiles(disk):
    # Assumes non-empty input
    # TODO : move the files until there are no free gaps between the files
    #O(<n)
    # Have pointer at start and end move these closer, collapsing the gap until first ends up after the last/no files ledt
    # Once file at end has been moved, add a fullstop after it meaning that the even spot is free space.

    # TODO : Calculate how many files there are (number of odd spots in the array)
    # 10:= 0[file] 1[space], 2[f] 3[s] 4[f] 5[s] 6[f] 7[s] 8[f] 9[s]
    # next_file_index = 0
    # current_file_id = 0
    # l <- array.length //len(disk)
    # if l mod 2 == 0 then  // Ie even
    #   files <- l / 2
    #   last_file_index <- l - 2
    # else
    #   files <- (l / 2) + 1
    #   last_file_index <- l - 1 
    # last_file_id = files - 1
    # TODO : Start at the first even spot (open disk spacing)
    #for i <- 0 to l do:
    #   if i == next_file_index then:
    #       disk[i] <- f"{next_file_id}:{disk[i]}"
    #       current_file_id ++
    #       next_file_index += 2
    #   else:
    #       // Move the last file into all the current space (if left over edit the last location with a new space sizing ) 

    #   if current_file_id >= last_file_id then
    #       // Insert break character
    #       disk[i+1] <- '-1'
    #       break // End of block has been found
    # move through the open spots moving each file
    # check that the pointer to the current open spot is not after the next file to move. 
    # need to add id to all the files ID:SPACE -> generate id 

    return disk

def checksum(input):
    # Check if input valud
    # O(n)
    total = 0
    # for i <- 0 to input.length do
    #   // Check for stopping key
    #   if input[i] == '-1':
    #        return total
    #   total += i * input[i]

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