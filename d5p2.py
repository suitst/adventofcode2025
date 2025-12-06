def get_input_list(path):
    input_list = []
    with open(path, 'r') as f:
        for line in f:
            string = line.strip()
            input_list.append(string)
    return input_list


def check_if_extends_range(existing_range, new_range):
    old_first, old_last = existing_range.split('-')
    new_first, new_last = new_range.split('-')

    # check if ranges have overlap
    if int(new_first) < int(old_first) and int(old_first) <= int(new_last) <= int(old_last): # extends left side
        updated_range = new_first + '-' + old_last
    elif int(new_last) > int(old_last) and int(old_first) <= int(new_first) <= int(old_last): # extends right side
        updated_range = old_first + '-' + new_last
    elif int(new_first) < int(old_first) and int(new_last) > int(old_last): # extends both sides
        updated_range = new_range
    else:
        is_updated = False
        return existing_range, is_updated
    is_updated = True
    return updated_range, is_updated


def consolidate_ranges(range_list):
    is_consolidated = False
    while not is_consolidated:
        update_count = 0
        for i in range(len(range_list)):
            for j in range(len(range_list)):
                new_entry, is_updated = check_if_extends_range(range_list[i], range_list[j])
                if is_updated:
                    #print(range_list[i], new_entry)
                    range_list[i] = new_entry  
                    update_count += 1
        if update_count == 0:
            is_consolidated = True            

    unique_list = list(set(range_list)) # removes duplicates
    return unique_list


def count_fresh_ids(range_list):
    count = 0
    for fresh_range in range_list:
        first, last = fresh_range.split('-')
        difference = (int(last) + 1) - int(first)
        count += difference

    return count


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

    consolidated_ranges = consolidate_ranges(test_range)
    test_count = count_fresh_ids(consolidated_ranges)
    print(test_count)

    problem_ranges = get_input_list('/Users/tim/Downloads/aoc2025/d5_ranges.txt')
    consolidated_ranges = consolidate_ranges(problem_ranges)
    problem_count = count_fresh_ids(consolidated_ranges)
    print(problem_count)