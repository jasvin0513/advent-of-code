def countZeroDials(input: str)  -> int:
    dialPosition = 50
    turns = input.splitlines()
    zeroCount = 0

    for turn in turns:
        dialPosition = turnDial(dialPosition, turn)
        if dialPosition == 0:
            zeroCount += 1

    return zeroCount
            
def turnDial(dialPosition: int, turn: str) -> int:
    turnDirection = turn[0]
    turnCount = int(turn[1:])
    
    # If we turn left, subtract the turnCount from the dial position
    if turnDirection == "L":
        dialPosition -= turnCount
        # Handle underflow by looping back to 99
        while (dialPosition < 0):
            dialPosition += 100
    # If we turn right, add the turnCount to the dial position
    elif turnDirection == "R":
        dialPosition += turnCount
        # Handle overflow by looping back to 0
        while (dialPosition > 99):
            dialPosition -= 100

    return dialPosition


if __name__ == "__main__":
    input_filename = 'level_1_input.txt'
    with open(input_filename, 'r') as file:
        file_content = file.read()
        print(countZeroDials(file_content))
