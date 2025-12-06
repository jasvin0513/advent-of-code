def max_joltage(input_data: str) -> int:
    # Split the input into separate battery banks.
    banks = input_data.splitlines()

    # Iterate through each bank and add the largest batteries to the list.
    max_bank_voltages = [
        find_max_joltage(bank)
        for bank in banks
    ]
    
    return sum(max_bank_voltages)

def find_max_joltage(bank: str) -> int:
    # Store the largest 12 battery indices in an array.
    largest_battery_indices = [0] * 12
    # Track which battery we're picking.
    for battery_num in range(12):
        batteries_remaining = 12 - battery_num
        search_end_index = len(bank) - (batteries_remaining - 1)

        # Assume we have the largest battery at first.
        search_start_index = 0
        if battery_num > 0:
            # The next search must start immediately after the previous selected digit.
            search_start_index = largest_battery_indices[battery_num - 1] + 1
        largest_battery_indices[battery_num] = search_start_index

        # Search for a battery starting from the last chosen battery position while saving X spots from the end for other batteries.
        for i in range(search_start_index, search_end_index):
            current_digit = int(bank[i])
            largest_digit = int(bank[largest_battery_indices[battery_num]])
            if (current_digit > largest_digit):
                largest_battery_indices[battery_num] = i
                largest_digit = current_digit

    # Concatenate the values to get the joltage.
    largest_joltage_str = "".join(bank[i] for i in largest_battery_indices)

    return int(largest_joltage_str)

if __name__ == "__main__":
    input_filename = "level_3_input.txt"
    with open(input_filename, "r") as file:
        input_data = file.read()
        print(max_joltage(input_data))