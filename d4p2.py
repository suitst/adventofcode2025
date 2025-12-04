def check_liftable_roll(above, middle, below, index):
    if index < 0 or index >= len(middle):
        return False 

    #define 3x3 search grid
    found_rolls = 0
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            col_idx = index + col_offset

            if col_idx < 0 or col_idx >= len(middle):
                continue

            if row_offset == -1:
                current_row = above
            elif row_offset == 0:
                current_row = middle
            else:
                current_row = below

            if current_row[col_idx] == "@":
                found_rolls += 1

    if middle[index] == "@" and found_rolls < 5:
        return True, index
    else:
        return False, None

    
def count_liftable_rolls_in_row(above, middle, below):
    count = 0
    found_indexes = []
    for i in range(len(middle)):
        status, found_roll_index = check_liftable_roll(above, middle, below, i)
        if status:
            count += 1
            found_indexes.append(found_roll_index)

    for index in found_indexes:
        middle = middle[:index] + "." + middle[index + 1:]
    return count, middle


def count_liftable_rows(row_list, dummy_row):
    count = 0
    list_len = len(row_list)
    for i in range(list_len):
        if i == 0:
            above, below = dummy_row, row_list[i + 1]
        elif i == list_len - 1:
            above, below = row_list[i - 1], dummy_row
        else:
            above, below = row_list[i - 1], row_list[i + 1]
        found_rolls, row_list[i] = count_liftable_rolls_in_row(above, row_list[i], below)
        count += found_rolls
    return count


if __name__ == "__main__":
    test_input = [
        '..@@.@@@@.',
        '@@@.@.@.@@',
        '@@@@@.@.@@',
        '@.@@@@..@.',
        '@@.@@@@.@@',
        '.@@@@@@@.@',
        '.@.@.@.@@@',
        '@.@@@.@@@@',
        '.@@@@@@@@.',
        '@.@.@@@.@.'
    ]
    test_answer = 13
    test_dummy_row = ".........."
    test_count = count_liftable_rows(test_input, test_dummy_row)
    print(test_count, test_answer, test_count == test_answer)

    dummy_row = "."*135
    problem_list = []
    with open('/Users/tim/Downloads/aoc2025/d4_input.txt', 'r') as f:
        for line in f:
            string = line.strip()
            problem_list.append(string)
    
    all_removed = False
    total_removed = 0
    while not all_removed:
        problem_count = count_liftable_rows(problem_list, dummy_row)
        if problem_count > 0:
            total_removed += problem_count
        else:
            all_removed = True

    print(total_removed)



