import re

INPUT = "385350926-385403705,48047-60838,6328350434-6328506208,638913-698668,850292-870981,656-1074,742552-796850,4457-6851,138-206,4644076-4851885,3298025-3353031,8594410816-8594543341,396-498,1558-2274,888446-916096,12101205-12154422,2323146444-2323289192,37-57,101-137,46550018-46679958,79-96,317592-341913,495310-629360,33246-46690,14711-22848,1-17,2850-4167,3723700171-3723785996,190169-242137,272559-298768,275-365,7697-11193,61-78,75373-110112,425397-451337,9796507-9899607,991845-1013464,77531934-77616074"

id_list = INPUT.split(",")


def halve_string(s):
    s1, s2 = s[:len(s)//2 + len(s)%2], s[len(s)//2 + len(s)%2:]
    return s1, s2


def check_for_repeat(id):
    invalid_numbers = []
    numbers = id.split('-')
    for number in range(int(numbers[0]), int(numbers[1]) + 1):
        if len(str(number)) % 2 == 0:
            s1, s2 = halve_string(str(number))
            if s1 == s2:
                print(f'{number} REPEAT DETECTED')
                invalid_numbers.append(number)
    return invalid_numbers


def sum_nums_from_strings(num_list):
    tally = 0
    for number in num_list:
        num = int(number)
        tally += num
    return tally


if __name__ == "__main__":
    invalids = []
    for id in id_list:
        invalid_repeats = check_for_repeat(id)
        if invalid_repeats is not None:
            for num in invalid_repeats:
                invalids.append(num)

    print(invalids)

    tally = sum_nums_from_strings(invalids)
    print(f'Invalid ID sum: {tally}')