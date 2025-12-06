def count_zero_dials(input_data: str)  -> int:
    dial_position = 50
    turns = input_data.splitlines()
    zero_count = 0

    for turn in turns:
        dial_position, zeros_hit = turn_dial(dial_position, turn)
        zero_count += zeros_hit

    return zero_count
            
def turn_dial(dial_position: int, turn: str) -> tuple[int, int]:
    turn_direction = turn[0]
    turn_count = int(turn[1:])
    zeros_passed = 0

    # If we start at 0, the next 0 is 100 clicks away
    if dial_position == 0:
        dist_to_first_zero = 100
        if turn_direction == "L":
            total_change = -turn_count
        elif turn_direction == "R":
            total_change = turn_count
    # If we turn left, subtract the turn_count from the dial position
    elif turn_direction == "L":
        # Find the distance to the next zero going left
        dist_to_first_zero = dial_position
        total_change = -turn_count
    # If we turn right, add the turn_count to the dial position
    elif turn_direction == "R":
        # Find the distance to the next zero going right
        dist_to_first_zero = 100 - dial_position
        total_change = turn_count
    
    # Calculate how much more to turn the dial if dial reaches the first zero  
    remaining_turn = turn_count - dist_to_first_zero
    # If the remaining turn is positive, the dial passes 0
    if remaining_turn >= 0:
        zeros_passed += 1
        zeros_passed += remaining_turn // 100

    final_position = (dial_position + total_change) % 100

    return (final_position, zeros_passed)


if __name__ == "__main__":
    input_filename = 'level_1_input.txt'
    with open(input_filename, 'r') as file:
        file_content = file.read()
        print(count_zero_dials(file_content))
