def rolls_accessible(input_data: str) -> int:
    accessible_rolls = 0

    # Convert the input into a 2D string array
    grid = input_data.splitlines()
    # Set the boundaries
    last_row = len(grid) - 1
    last_col = len(grid[0]) - 1

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Only check the surroundings of a cell that has a roll of paper
            if grid[row][col] == "@":
                surroundings = ""

                # Get the top row
                top_left = "." if ((row == 0) or (col == 0)) else grid[row-1][col-1]
                top = "." if (row == 0) else grid[row-1][col]
                top_right = "." if ((row == 0) or (col == last_col)) else grid[row-1][col+1]
                surroundings += (top_left + top + top_right)

                # Get the left and right
                left = "." if (col == 0) else grid[row][col-1]
                right = "." if (col == last_col) else grid[row][col+1]
                surroundings += (left + right)

                # Get the bottom row
                bottom_left = "." if ((row == last_row) or (col == 0)) else grid[row+1][col-1]
                bottom = "." if (row == last_row) else grid[row+1][col]
                bottom_right = "." if ((row == last_row) or (col == last_col)) else grid[row+1][col+1]
                surroundings += (bottom_left + bottom + bottom_right)

                # If there are less than 4 rolls in the surroundings, it is accessible
                if (surroundings.count("@") < 4):
                    accessible_rolls += 1

    return accessible_rolls
            

if __name__ == "__main__":

    input_filename = "level_4_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(rolls_accessible(file_content))