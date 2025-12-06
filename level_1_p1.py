def count_zero_dials(input_data: str)  -> int:
    dial_position = 50
    turns = input_data.splitlines()
    zero_count = 0

    for turn in turns:
        dial_position = turn_dial(dial_position, turn)
        if dial_position == 0:
            zero_count += 1

    return zero_count
            
def turn_dial(dial_position: int, turn: str) -> int:
    turn_direction = turn[0]
    turn_count = int(turn[1:])
    
    # If we turn left, subtract the turn_count from the dial position
    if turn_direction == "L":
        dial_position -= turn_count
    # If we turn right, add the turn_count to the dial position
    elif turn_direction == "R":
        dial_position += turn_count

    return dial_position % 100


if __name__ == "__main__":
    input_filename = 'level_1_input.txt'
    with open(input_filename, 'r') as file:
        file_content = file.read()
        print(count_zero_dials(file_content))
