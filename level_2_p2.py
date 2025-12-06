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

    # Check for repeated substrings starting with half the number
    for substr_length in range(len(str_id)//2, 0, -1):
        # If the ID isn't divisible by the substring length, skip it
        if len(str_id) % substr_length != 0:
            continue

        # Check if the substring makes up the entire string
        substr = str_id[0:substr_length]
        num_repetitions = str_id.count(substr)
        # If the substring makes up the string entirely, it is invalid
        if (len(str_id) == (substr_length*num_repetitions)):
            return True
    return False

if __name__ == "__main__":
    input_filename = "level_2_input.txt"
    with open(input_filename, 'r') as file:
        input_data = file.read()
        print(add_invalid_ids(input_data))