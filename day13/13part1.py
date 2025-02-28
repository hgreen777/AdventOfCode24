# Day 13
# Part 1 : 26810
# Part 2: 108713182988244
# O(n)

from datetime import datetime
from re import findall
start_time = datetime.now()

FILE = f"input.txt"

def readFile(file):
    equations = []
    with open(file, 'r') as f:
        while True:
            lines = [f.readline().strip() for _ in range(4)][:3]
            if not any(lines):
                break
            equations.append(lines)

    
    return equations

def extractData(equations):
    extracted_equations = []
    # [(x,y,a),(x,y,a)]

    for eq in equations:
        extracted_data = []
        extracted_data.append((int(findall(r"(X\+)+([0-9]+)",eq[0])[0][1]), int(findall(r"(X\+)+([0-9]+)",eq[1])[0][1]), int(findall(r"(X=)+([0-9]+)",eq[2])[0][1]) + 10000000000000))
        extracted_data.append((int(findall(r"(Y\+)+([0-9]+)",eq[0])[0][1]), int(findall(r"(Y\+)+([0-9]+)",eq[1])[0][1]), int(findall(r"(Y=)+([0-9]+)",eq[2])[0][1]) + 10000000000000))

        extracted_equations.append(extracted_data)
    
    return extracted_equations

def solveEquations(simultaneous_equations):
    solutions = []
    for equations in simultaneous_equations:
        # Cramers rules
        original_matrix = [equations[0][0],equations[0][1]],[equations[1][0], equations[1][1]]
        det_original = original_matrix[0][0] * original_matrix[1][1] - original_matrix[0][1] * original_matrix [1][0]

        a = (equations[0][2] * equations[1][1] - equations[0][1] * equations[1][2]) / det_original
        b = (equations[0][0] * equations[1][2] - equations[0][2] * equations[1][0]) / det_original


        if a % 1 == 0 and b % 1 == 0:
            solutions.append([a,b])

    return solutions

def calculateTokens(results):
    total = 0 
    for result in results:
        total += result[0] * 3 + result[1]
    
    return total

def main():
    raw_equations = readFile(FILE)
    extracted_equations = extractData(raw_equations)
    results = solveEquations(extracted_equations)
    total_tokens = calculateTokens(results)
    print(f"Part 2 total: {total_tokens}")

main()

end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
print(f"Execution time: {execution_time} seconds")