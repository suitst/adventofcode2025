test_strings = ['987654321111111',
                '811111111111119',
                '234234234234278',
                '818181911112111'
]
test_answer = 357
def find_biggest_number(string):
    max_ten = 0
    max_ten_pos = 0
    max_one = 0

    trimmed_string = string[:-1]

    for char in trimmed_string:
        if int(char) > max_ten:
            max_ten = int(char)
            max_ten_pos = string.find(char)

    truncated_string = string[max_ten_pos + 1:]
    for char in truncated_string:
        if int(char) > max_one:
            max_one = int(char)

    chars = [max_ten, max_one]
    joltage = ''.join(str(char) for char in chars)

    return joltage


if __name__ == "__main__":

    total_joltage = 0
    for string in test_strings:
        joltage = find_biggest_number(string)
        print(string, joltage)
        total_joltage += int(joltage)
    
    print(f'test joltage:{total_joltage}')
    print(f'test answer: {test_answer}')

    problem_joltage = 0
    with open('/Users/tim/Downloads/aoc2025/d3_input.txt', 'r') as f:
        for line in f:
            string = line.strip()
            joltage = find_biggest_number(string)
            print(string, joltage)
            problem_joltage += int(joltage)

    print(f'problem joltage: {problem_joltage}')

    


