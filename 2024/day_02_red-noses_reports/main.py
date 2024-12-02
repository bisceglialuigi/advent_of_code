import heapq
from collections import defaultdict

def part1(levels):
    ans = 0

    for level in levels:
        if _is_safe(level):
            ans += 1

    return ans


def part2(levels):
    ans = 0

    for level in levels:
        if _is_safe(level):
            ans += 1
            continue

        is_level_safe = False
        for i in range(len(level)):
            modified_level = level[:i] + level[i + 1:]
            if _is_safe(modified_level):
                is_level_safe = True
                break

        if is_level_safe:
            ans += 1

    return ans


def _is_safe(level):
    is_increasing = level[-1] > level[0]
    for i in range(1, len(level)):
        if not _check_pair_safety(level, is_increasing, i, i - 1):
            return False
    return True


def _check_pair_safety(level, is_increasing, i, j):
    difference = level[i] - level[j]
    if abs(difference) > 3 or difference == 0:
        return False
    elif is_increasing and difference < 0:
        return False
    elif not is_increasing and difference > 0:
        return False

    return True


def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [[int(num) for num in line.split()] for line in file]


INPUT_PATH = "input.txt"
levels = parse_input(INPUT_PATH)

solution1 = part1(levels)
print("The solution of part 1 is: {}".format(solution1))

solution2 = part2(levels)
print("The solution of part 2 is: {}".format(solution2))