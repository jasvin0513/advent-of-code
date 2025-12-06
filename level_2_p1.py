def add_invalid_ids(input_data: str) -> int:
    # Split the text ranges by their delimiter
    split_ranges = input_data.split(',')
    
    # For each range, create a list of the integers between them
    invalid_ids = []
    for str_range in split_ranges:
        start, end = str_range.split('-')
        start_num = int(start)
        end_num = int(end)

        ids = range(start_num, end_num+1)
        
        for id in ids:
            if is_invalid_id(id):
                invalid_ids.append(id)

    return sum(invalid_ids)

def is_invalid_id(id: int) -> bool:
    str_id = str(id)

    # An ID is invalid if the first half is the same as the second half
    left_half = str_id[0:len(str_id)//2]
    right_half = str_id[len(str_id)//2:len(str_id)]
    return left_half == right_half

if __name__ == "__main__":
    input_filename = "level_2_input.txt"
    with open(input_filename, 'r') as file:
        input_data = file.read()
        print(add_invalid_ids(input_data))