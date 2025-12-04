def check_liftable_roll(above, middle, below, index):
    if index < 0 or index >= len(middle):
        return False 

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

    return middle[index] == "@" and found_rolls < 5

    
def count_liftable_rolls_in_row(above, middle, below):
    count = 0
    for i in range(len(middle)):
        if check_liftable_roll(above, middle, below, i):
            count += 1
    return count


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
        count += count_liftable_rolls_in_row(above, row_list[i], below)
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

    problem_count = count_liftable_rows(problem_list, dummy_row)
    print(problem_count)



