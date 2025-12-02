import re

INPUT = "385350926-385403705,48047-60838,6328350434-6328506208,638913-698668,850292-870981,656-1074,742552-796850,4457-6851,138-206,4644076-4851885,3298025-3353031,8594410816-8594543341,396-498,1558-2274,888446-916096,12101205-12154422,2323146444-2323289192,37-57,101-137,46550018-46679958,79-96,317592-341913,495310-629360,33246-46690,14711-22848,1-17,2850-4167,3723700171-3723785996,190169-242137,272559-298768,275-365,7697-11193,61-78,75373-110112,425397-451337,9796507-9899607,991845-1013464,77531934-77616074"

id_list = INPUT.split(",")


def check_single_number(number, invalid_numbers):
    num_str = str(number)
    first_char = num_str[0]
    if num_str == first_char*len(num_str):
        if num_str not in invalid_numbers:
            invalid_numbers.add(number)
            print(f'{number} INVALID DETECTED: SINGLE NUMBER REPEAT: {str(number)[0]}')


def compare_fragments(s, frag_length):
    parts = [s[i:i+frag_length] for i in range(0, len(s), frag_length)]
    if parts[0] == parts[1]:
        check_part = parts[0]
    else:
        return None
        
    all_match = True
    match_counter = 0

    for part in parts:
        if part != check_part:
            all_match = False
        else:
            match_counter += 1
    
    if all_match:
        return s
    else:
        return None


def check_for_repeat(id, invalid_numbers):
    numbers = id.split('-')
    for number in range(int(numbers[0]), int(numbers[1]) + 1):
        num_len = len(str(number))
        for frag_len in range(2, num_len+1):
            if num_len == frag_len:
                check_single_number(number, invalid_numbers)
            else:
                invalid_num = compare_fragments(str(number), frag_len)
                if invalid_num is not None:
                    if invalid_num not in invalid_numbers:
                        print(f'{number} INVALID DETECTED WITH REPEAT LENGTH {frag_len}')
                        invalid_numbers.add(invalid_num)
    return invalid_numbers


def sum_nums_from_strings(num_list):
    tally = 0
    for number in num_list:
        num = int(number)
        tally += num
    return tally


def find_invalids(number_list):
    invalids = set()
    for number in number_list:
        invalid_repeats = check_for_repeat(number, invalids)
        if invalid_repeats is not None:
            for num in invalid_repeats:
                invalids.add(num)
    tally = sum_nums_from_strings(invalids)
    print(f'Invalid ID sum: {tally}')
    return tally


if __name__ == "__main__":
    test_str = '10101010-10101011'
    example_str = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    example_list = example_str.split(',')
    example_answer = 4174379265

    example_tally = find_invalids(example_list)
    print(f'correct answer: {example_answer}')
    print(example_tally==example_answer)

    answer = find_invalids(id_list)
