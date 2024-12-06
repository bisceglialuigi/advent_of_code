def parse_input(file_path):
    """Parses the input map and locates the guard's initial position and direction."""
    with open(file_path, 'r') as f:
        input_map = f.read()

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    grid = []
    guard_position = None
    guard_direction = None

    for r, line in enumerate(input_map.strip().split('\n')):
        row = []
        for c, char in enumerate(line):
            row.append(char)
            if char in directions:
                guard_position = (r, c)
                guard_direction = directions[char]
        grid.append(row)

    return grid, guard_position, guard_direction


def turn_right(direction):
    """Calculates the new direction when the guard turns right."""
    return {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}[direction]


def simulate_patrol(grid, start_pos, start_dir, max_steps=10000):
    """Simulates the guard's patrol and returns the positions visited with directions."""
    rows, cols = len(grid), len(grid[0])
    visited = []
    position = start_pos
    direction = start_dir

    for _ in range(max_steps):
        visited.append((position, direction))
        next_row, next_col = position[0] + direction[0], position[1] + direction[1]

        # Check boundaries
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break

        # Check if there's an obstacle in the next position
        if grid[next_row][next_col] == '#':
            direction = turn_right(direction)  # Turn right if there's an obstacle
        else:
            position = (next_row, next_col)  # Move forward if the path is clear

    return visited


def part1(grid, start_pos, start_dir):
    """Counts the number of distinct positions visited by the guard."""
    visited = simulate_patrol(grid, start_pos, start_dir)
    return len({pos for pos, _ in visited})


def detect_loop(visited):
    """Detects if the guard's path forms a loop."""
    seen_states = {}
    for step, (pos, direction) in enumerate(visited):
        state = (pos, direction)
        if state in seen_states:
            return True
        seen_states[state] = step
    return False


def part2(grid, start_pos, start_dir):
    """Counts all possible positions for an obstruction that creates a loop."""

    # Simulate the guard's patrol path without any additional obstructions
    patrol_path = simulate_patrol(grid, start_pos, start_dir)

    # Create a set of all positions visited during the patrol
    patrol_positions = {pos for pos, _ in patrol_path}
    loop_positions = 0

    # Test placing an obstruction at each position in the patrol path
    for r, c in patrol_positions:
        if (r, c) == start_pos or grid[r][c] == '#':
            continue

        # Temporarily place an obstruction
        grid[r][c] = '#'

        # Simulate the guard's patrol with the obstruction
        visited = simulate_patrol(grid, start_pos, start_dir)

        # Check if the guard gets stuck in a loop
        if detect_loop(visited):
            loop_positions += 1

        # Remove the temporary obstruction
        grid[r][c] = '.'

    return loop_positions


INPUT_PATH = "input.txt"

grid, start_pos, start_dir = parse_input(INPUT_PATH)

distinct_positions = part1(grid, start_pos, start_dir)
print(f"The solution of part 1 is: {distinct_positions}")

loop_positions = part2(grid, start_pos, start_dir)
print(f"The solution of part 2 is: {loop_positions}")