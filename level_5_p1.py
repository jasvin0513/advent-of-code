def count_fresh_ingredients(input_data: str) -> int:
    data = input_data.splitlines()

    # Separate the data into a list of fresh ingredient ranges and a list of ingredient IDs
    split_point = data.index("")
    ingredient_str_ranges = data[:split_point]
    ingredient_ids = [int(id) for id in data[split_point+1:]]

    # Place all ingredients in the ranges into a tuple range to save memory
    fresh_ingredients_ranges = []
    for str_range in ingredient_str_ranges:
        start, end = map(int, str_range.split("-"))
        fresh_ingredients_ranges.append((start, end))

    total_fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        for id_range in fresh_ingredients_ranges:
            start, end = id_range
            if start <= ingredient_id <= end:
                total_fresh_ingredients += 1
                break
    
    return total_fresh_ingredients


if __name__ == "__main__":
    input_filename = "level_5_input.txt"
    with open(input_filename, "r") as file:
        file_content = file.read()
        print(count_fresh_ingredients(file_content))