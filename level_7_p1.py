def num_beam_splits(input_data: str) -> int:
    manifold_rows = input_data.splitlines()
    manifold_grid = [list(row) for row in manifold_rows]
    beam_split_count = 0
    LAST_ROW = len(manifold_grid)-1
    LAST_COL = len(manifold_grid[0])-1

    # Iterate through the 2D grid
    for row_num in range(len(manifold_grid)):
        for col_num in range(len(manifold_grid[0])):
            curr_char = manifold_grid[row_num][col_num]
            above_char = manifold_grid[row_num-1][col_num]

            # If the character is ^, add a beam to the left and right:
            if curr_char == "^":
                if row_num > 0 and manifold_grid[row_num-1][col_num]=="|":
                    beam_split_count += 1
                    # Create a new beam
                    if col_num > 0 and col_num < LAST_COL:
                        manifold_grid[row_num][col_num-1] = "|"
                        manifold_grid[row_num][col_num+1] = "|"

            # If the character is the entrypoint, add a beam below:
            elif curr_char == "S":
                if row_num < LAST_ROW:
                    manifold_grid[row_num+1][col_num] = "|"

            # If the character is a beam, extend it if there is no splitter below it
            elif above_char == "|" and curr_char != "^":
                manifold_grid[row_num][col_num] = "|"


    return beam_split_count

if __name__ == "__main__":
    input_filename = "level_7_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(num_beam_splits(file_content))
