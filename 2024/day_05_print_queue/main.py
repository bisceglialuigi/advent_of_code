from collections import defaultdict, deque

def part1(rules, updates):
    valid_updates = []

    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)

    middle_sum = 0
    for update in valid_updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]

    return middle_sum


def part2():
    invalid_updates = []

    for update in updates:
        if not is_update_valid(update, rules):
            invalid_updates.append(update)

    middle_sum = 0
    for update in invalid_updates:
        sorted_update = sort_update(update, rules)
        middle_index = len(sorted_update) // 2
        middle_sum += sorted_update[middle_index]

    return middle_sum


def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split('\n\n')

    rules = [tuple(map(int, line.split('|'))) for line in content[0].split('\n')]
    updates = [list(map(int, line.split(','))) for line in content[1].split('\n')]

    return rules, updates

def is_update_valid(update, rules):
    for before, after in rules:
        if before in update and after in update:
            if update.index(before) > update.index(after):
                return False
    return True

def sort_update(update, rules):

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)


    for before, after in rules:
        if before in pages and after in pages:
            graph[before].append(after)
            in_degree[after] += 1

    for page in update:
        if page not in in_degree:
            in_degree[page] = 0

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


INPUT_PATH = "input.txt"
rules, updates = parse_input(INPUT_PATH)

solution1 = part1(rules, updates)
print("The solution of part 1 is: {}".format(solution1))

solution2 = part2()
print("The solution of part 2 is: {}".format(solution2))