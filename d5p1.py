def check_in_range(query, first, last):
    if query in range(int(first), int(last)+1):
        return True
    

def check_if_fresh(query, range_list):
    for num_range in range_list:
        first, last = num_range.split('-')
        is_fresh = check_in_range(query, first, last)
        if is_fresh:
            return True
    return False


def count_fresh_items(input_list, range_list):
    fresh_items = []
    for item in input_list:
        is_fresh = check_if_fresh(int(item), range_list)
        if is_fresh:
            fresh_items.append(int(item))
    return len(fresh_items)


def get_input_list(path):
    input_list = []
    with open(path, 'r') as f:
        for line in f:
            string = line.strip()
            input_list.append(string)
    return input_list


if __name__ == "__main__":
    test_range = [
    '3-5',
    '10-14',
    '16-20',
    '12-18',
    ]

    test_input = [
    '1',
    '5',
    '8',
    '11',
    '17',
    '32',
    ]


test_count = count_fresh_items(test_input, test_range)
print(test_count)


problem_input = get_input_list('/Users/tim/Downloads/aoc2025/d5_input.txt')
problem_ranges = get_input_list('/Users/tim/Downloads/aoc2025/d5_ranges.txt')

problem_count = count_fresh_items(problem_input, problem_ranges)
print(problem_count)