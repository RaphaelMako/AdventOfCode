import re

def solution1():
    with open('daythree.txt', 'r') as f:
        lines = f.read()
    lines.strip()

    lines = lines.splitlines()

    count = 0
    for line in lines:
        count += multiplyMatches1(line)

    return count
def multiplyMatches1(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, line)

    results = []
    for match in matches:
        print(match)
        num1, num2 = map(int, match)  # Convert matched strings to integers
        results.append(num1 * num2)
    
    return sum(results)

# print(solution1())

def solution2():
    with open('daythree.txt', 'r') as f:
        lines = f.read()
    lines.strip()

    count = multiplyMatches2(lines)

    return count

def multiplyMatches2(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    matches = list(re.finditer(pattern, line))

    multiplications = []
    
    # Traverse the matches
    previous_type = "do"  # Keep track of the last encountered match type
    for match in matches:
        if match.group(0) == "do()":
            previous_type = "do"
        elif match.group(0) == "don't()":
            previous_type = "don't"
        elif match.group(1) and match.group(2):  # It's a mul(X,Y)
            x, y = int(match.group(1)), int(match.group(2))
            if previous_type == "do":  # Check if it follows a do()
                multiplications.append((x * y))
    return sum(multiplications)
    

print(solution2())

#Time to complete both 44:08