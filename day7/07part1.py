# Day 7
# Part 1 : 1399219271639
from datetime import datetime
start_time = datetime.now()

FILE = 'input.txt'

operators = ['+','*']

# Solution brute force with O(n * 2^x) n = input size, x =argument size (technically (O(2n* __) due to file read.))

# Start by a brute force attempt 
def readfile():
    equations = []
    with open(FILE,'r') as file:
        for line in file:
            result = int(line.split(':')[0])
            arguments = line.split(':')[1].replace('\n','').split(' ')[1:]
            {'result':result,'arguments':arguments}
            equations.append({'result':result,'arguments':arguments})
    return equations

def brute_force(equations):
    total = 0

    for equation in equations:
        if equation_possible(equation):
            total += equation['result']
    
    return total
        


def equation_possible(equation):
    iterations = len(equation['arguments']) - 1
    for i in range(2 ** iterations):
        
        bin_num = format(i,f'0{iterations}b')

        current_result = int(equation['arguments'][0])

        for index,argument in enumerate(equation['arguments']):
            if index == 0:
                continue

            if bin_num[index - 1] == '0':
                current_result += int(argument)

            elif bin_num[index - 1] == '1':
                current_result *= int(argument)

            else:
                print(bin_num[index - 1])

            if current_result > equation['result']:
                break

        if current_result == equation['result']:
            return True

    return False
            


def main():
    equations = readfile()

    print(f"Part 1 total: {brute_force(equations)}")


main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")