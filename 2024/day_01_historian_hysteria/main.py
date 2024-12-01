import heapq
from collections import defaultdict

def part1(list1, list2):
    ans = 0
    heapq.heapify(list1)
    heapq.heapify(list2)
    while list1 and list2:
        ans += abs(heapq.heappop(list1)-heapq.heappop(list2))

    return ans


def part2(list1, list2):
    ans = 0
    list2_map = defaultdict(int)

    for num in list2:
        list2_map[num] += 1

    for num in list1:
        ans += num * list2_map[num]

    return ans


def parse_two_columns(file_path):
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                col1, col2 = map(int, line.split())
                list1.append(col1)
                list2.append(col2)

    return list1, list2


INPUT_PATH = "input.txt"
list1, list2 = parse_two_columns(INPUT_PATH)

solution1 = part1(list1.copy(), list2.copy())
print("The solution of part 1 is: {}".format(solution1))

solution2 = part2(list1.copy(), list2.copy())
print("The solution of part 2 is: {}".format(solution2))