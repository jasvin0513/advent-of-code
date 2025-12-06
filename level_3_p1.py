def max_joltage(input_data: str) -> int:
    # Split the input into separate battery banks
    banks = input_data.splitlines()

    # Iterate through each bank and add the largest batteries to the list
    max_bank_voltages = []
    for bank in banks:
        max_bank_voltage = find_max_joltage(bank)
        max_bank_voltages.append(max_bank_voltage)
    
    return sum(max_bank_voltages)

def find_max_joltage(bank: str) -> int:
    # First find the largest tens digit (excluding the final index)
    largest_ten_index = 0
    for i in range(0, len(bank) - 1):
        digit = int(bank[i])
        largest_tenth_digit = int(bank[largest_ten_index])
        if (digit > largest_tenth_digit):
            largest_ten_index = i
            largest_tenth_digit = digit
    
    # Now find the largest ones digit after the tens digit
    largest_one_index = largest_ten_index + 1
    for i in range(largest_ten_index + 1, len(bank)):
        digit = int(bank[i])
        largest_one_digit = int(bank[largest_one_index])
        if (digit > largest_one_digit):
            largest_one_index = i
            largest_one_digit = digit

    # Concatenate the values to get the joltage
    largest_joltage = str(largest_tenth_digit) + str(largest_one_digit)
    return int(largest_joltage)

if __name__ == "__main__":
    input_filename = "level_3_input.txt"
    with open(input_filename, "r") as file:
        input_data = file.read()
        print(max_joltage(input_data))