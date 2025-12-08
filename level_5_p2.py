def count_fresh_ingredients(input_data: str) -> int:
    data = input_data.splitlines()

    # Separate the data into a list of fresh ingredient ranges and a list of ingredient IDs
    split_point = data.index("")
    ingredient_str_ranges = data[:split_point]

    # Place all ingredients in the ranges into a tuple range to save memory
    fresh_ingredients_ranges = []
    for str_range in ingredient_str_ranges:
        start, end = map(int, str_range.split("-"))
        fresh_ingredients_ranges.append([start, end])

    # Merge ingredient ranges where possible before adding the lengths of each range
    merged_ranges = merge_ranges(fresh_ingredients_ranges)
    total_fresh_ingredients = sum([end - start + 1 for start, end in merged_ranges])

    return total_fresh_ingredients

def merge_ranges(ranges: list[list]) -> list[list]:
    sorted_ranges = sorted(ranges, key=lambda item: item[0])

    merged_ranges = [sorted_ranges[0]]
    for next_range in sorted_ranges[1:]:
        curr_end = merged_ranges[-1][1]
        next_start, next_end = next_range

        if next_start <= curr_end:
            merged_ranges[-1][1] = max(curr_end, next_end)
        else:
            merged_ranges.append(next_range)

    return merged_ranges

if __name__ == "__main__":
    input_filename = "level_5_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(count_fresh_ingredients(file_content))