def num_timelines(input_data: str) -> int:
    manifold_rows = input_data.splitlines()
    manifold_grid = [list(row) for row in manifold_rows]
    rows = len(manifold_grid)
    cols = len(manifold_grid[0])

    # Create a grid to store the count of timelines reaching each cell
    timelines = [[0 for _ in range(cols)] for _ in range(rows)]

    # Find starting point 'S' and set its timeline to 1
    starting_row = 0
    for row in range(rows):
        for col in range(cols):
            if manifold_grid[row][col] == "S":
                timelines[row][col] = 1
                starting_row = row

    # Process each row
    for row in range(starting_row, rows-1):
        for col in range(cols):
            paths_to_cell = timelines[row][col]
            if paths_to_cell == 0:
                continue

            curr_char = manifold_grid[row][col]

            # If a splitter is found, add a beam to the left and right
            if curr_char == "^":
                # The left and right cells inherit the paths it took to get there
                timelines[row+1][col-1] += paths_to_cell
                timelines[row+1][col+1] += paths_to_cell
            else:
                # If there is no splitter, the cell below inherits the paths of the cell above
                timelines[row+1][col] += paths_to_cell

    # Return the number of paths of each cell in the final row
    return sum(timelines[rows-1])

if __name__ == "__main__":
    input_filename = "level_7_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(num_timelines(file_content))
