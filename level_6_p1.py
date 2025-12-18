def sum_all_problems(input_data: str) -> int:
    grid = input_data.splitlines()
    
    # Each operator is in the last row
    operators = grid[-1].split()
    # Convert the rest of the grid to numbers
    number_grid = []
    for row in range(len(grid) - 1):
        grid_row = (grid[row].split())
        num_row = [int(num) for num in grid_row]
        number_grid.append(num_row)

    # For each operator, apply the column's operator to each row in the column
    col_results = 0
    for col, operator in enumerate(operators):
        column_data = [row[col] for row in number_grid]

        if operator == "+":
            result = sum(column_data)
        elif operator == "*":
            result = 1
            for val in column_data:
                result *= val
            
        col_results += result
    
    return col_results

if __name__ == "__main__":
    input_filename = "level_6_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(sum_all_problems(file_content))
