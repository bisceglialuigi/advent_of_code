import re

def part1(lines):
    ans = 0
    for x,y in lines:
        ans += x * y
    return ans


def part2(lines):
    memory = ''.join(lines)

    mul_enabled = True
    total_sum = 0

    # Regex to match mul(X, Y) and do() / don't()
    pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'

    matches = re.finditer(pattern, memory)

    for match in matches:
        if match.group(1) is not None and match.group(2) is not None:
            x = int(match.group(1))
            y = int(match.group(2))

            if mul_enabled:
                total_sum += x * y
        elif match.group(0) == 'do()':
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False

    return total_sum



def parse_input_part1(file_path):
    # Regex to match mul(x, y) and extract x and y
    pattern = r"mul\((\d+),\s*(\d+)\)"

    with open(file_path, 'r') as file:
        content = file.read()

    matches = re.findall(pattern, content)
    return [(int(x), int(y)) for x, y in matches]

def parse_input_part2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines


INPUT_PATH = "input.txt"
input_structure = parse_input_part1(INPUT_PATH)

solution1 = part1(input_structure)
print("The solution of part 1 is: {}".format(solution1))

input_structure = parse_input_part2(INPUT_PATH)
solution2 = part2(input_structure)

print("The solution of part 2 is: {}".format(solution2))