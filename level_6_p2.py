def sum_all_problems(input_data: str) -> int:
    grid = input_data.splitlines()
    # Store the max number of rows in a problem
    max_problem_height = len(grid) - 1
    OPERATOR_ROW = max_problem_height

    total_result = 0
    curr_problem_nums = []
    curr_op = None

    # Iterate through the grid by columns first going backwards
    for col_num in range(len(grid[0])-1, -1, -1):
        # If a column is empty, skip it
        curr_col = [row[col_num] for row in grid]
        
        # If a seperator is found, calculate the block result
        if all(val == " " for val in curr_col) and curr_op:
            if curr_problem_nums:
                total_result += problem_set_result(curr_problem_nums, curr_op)
                curr_problem_nums = []
                curr_op = None
            continue

        # Filter out spaces 
        digits = [val for val in curr_col[:-1] if val != " "]
        if digits:
            combined_col = "".join(digits)
            curr_problem_nums.append(combined_col)

        # Store the operator if found
        op_char = grid[OPERATOR_ROW][col_num]
        if op_char in ("+", "*"):
            curr_op = op_char

    if curr_problem_nums and curr_op:
        total_result += problem_set_result(curr_problem_nums, curr_op)

    return total_result

def problem_set_result(problem_nums: list[str], operator: str) -> int:
    if operator == "+":
        res = 0
        for num in problem_nums:
            res += int(num)
    else:
        res = 1
        for num in problem_nums:
            res *= int(num)

    return res


if __name__ == "__main__":
    input_filename = "level_6_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(sum_all_problems(file_content))
