def total_accessible_rolls(input_data: str) -> int:
    # Convert the input into a 2D string array
    grid = [list(row_str) for row_str in input_data.splitlines()]
    # Set the boundaries
    last_row = len(grid) - 1
    last_col = len(grid[0]) - 1
    # Set a coordinate system relative to each node
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Only check the surroundings of a cell that has a roll of paper
            if grid[row][col] == "@":
                roll_count = 0
                for direction_row, direction_col in DIRECTIONS:
                    neighbor_row = row + direction_row
                    neighbor_col = col + direction_col

                    # Compare the neighbor if it within bounds
                    if (0 <= neighbor_row <= last_row) and (0 <= neighbor_col <= last_col):
                        if grid[neighbor_row][neighbor_col] == "@":
                            roll_count += 1
                
                if roll_count < 4:
                    accessible_rolls += 1

    return accessible_rolls
            
if __name__ == "__main__":

    input_filename = "level_4_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(total_accessible_rolls(file_content))