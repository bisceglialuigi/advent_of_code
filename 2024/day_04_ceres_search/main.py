
def part1(grid):
    word = "XMAS"

    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Define directions for searching (dx, dy)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Down-right diagonal
        (1, -1),  # Down-left diagonal
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Up-left diagonal
        (-1, 1)   # Up-right diagonal
    ]

    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True


    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1

    return count


def part2(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0


    def is_xmas(x, y):
        try:
            top_left1, top_left2 = x-1, y-1
            top_right1, top_right2 = x-1, y+1
            bottom_left1, bottom_left2 = x+1, y-1
            bottom_right1, bottom_right2 = x+1, y+1

            if grid[x][y] != 'A':
                return False

            # Pattern 1: M . S
            #            . A .
            #            M . S
            if grid[top_left1][top_left2] == 'M' and grid[top_right1][top_right2] == 'S' and \
               grid[bottom_left1][bottom_left2] == 'M' and grid[bottom_right1][bottom_right2] == 'S':
                return True

            # Pattern 2: M . M
            #            . A .
            #            S . S
            if grid[top_left1][top_left2] == 'M' and grid[top_right1][top_right2] == 'M' and \
               grid[bottom_left1][bottom_left2] == 'S' and grid[bottom_right1][bottom_right2] == 'S':
                return True

            # Pattern 3: S . M
            #            . A .
            #            S . M
            if grid[top_left1][top_left2] == 'S' and grid[top_right1][top_right2] == 'M' and \
               grid[bottom_left1][bottom_left2] == 'S' and grid[bottom_right1][bottom_right2] == 'M':
                return True

            # Pattern 4: S . S
            #            . A .
            #            M . M
            if grid[top_left1][top_left2] == 'S' and grid[top_right1][top_right2] == 'S' and \
               grid[bottom_left1][bottom_left2] == 'M' and grid[bottom_right1][bottom_right2] == 'M':
                return True


        except IndexError:
            return False

        return False


    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if is_xmas(i, j):
                count += 1

    return count


def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid


INPUT_PATH = "input.txt"
input_structure = parse_input(INPUT_PATH)


solution1 = part1(input_structure)
print("The solution of part 1 is: {}".format(solution1))

solution2 = part2(input_structure)
print("The solution of part 2 is: {}".format(solution2))