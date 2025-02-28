# Day 14
# Part 1 : 222901875
# O(n)

from datetime import datetime
from re import findall
start_time = datetime.now()

FILE = f"input.txt"
bounds = [101,103] # x,y

class Guard:
    def __init__(self, position, velocity): # [], []
        self.pos = position
        self.vel = velocity
        self.final_pos = self.pos

def readFile(file):
    all_guards = []

    with open(file, 'r') as f:
        for line in f:
            pos = findall(r"(p=)([0-9]+,[0-9]+)", line)[0][1].split(',')
            pos = [int(x) for x in pos]

            vel = findall(r"(v=)([0-9,-]+,[0-9,-]+)", line)[0][1].split(',')
            vel = [int(x) for x in vel]
            
            guard = Guard(pos,vel)
            all_guards.append(guard)

    return all_guards

def calculatePosition(guards, dt):

    for guard in guards:
        guard.final_pos[0] = (guard.pos[0] + (guard.vel[0] * dt)) % bounds[0]
        guard.final_pos[1] = (guard.pos[1] + (guard.vel[1] * dt)) % bounds[1]

def calculateSafetyFactor(guards):
    q1,q2,q3,q4 = 0,0,0,0

    x_line = int(bounds[0] / 2)
    y_line = int(bounds[1] / 2)

    for guard in guards:
        if   guard.final_pos[0] < x_line and guard.final_pos[1] < y_line:
            q1 += 1
        elif guard.final_pos[0] > x_line and guard.final_pos[1] < y_line:
            q2 += 1
        elif guard.final_pos[0] < x_line and guard.final_pos[1] > y_line:
            q3 += 1
        elif guard.final_pos[0] > x_line and guard.final_pos[1] > y_line:
            q4 += 1

    return q1 * q2 * q3 * q4

def main():
    guards = readFile(FILE)
    calculatePosition(guards, 100)
    total = calculateSafetyFactor(guards)
    print(f"Part 2 total: {total}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")