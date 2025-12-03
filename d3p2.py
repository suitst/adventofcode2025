test_strings = ['987654321111111',
                '811111111111119',
                '234234234234278',
                '818181911112111'
]
test_answer = 3121910778619

def trim_string(string, cut_site):
    left = string[0:cut_site]
    right = string[cut_site+1:]
    new_string = left + right
    return new_string

def find_biggest_12mer(string):
    while len(string) > 12:
        has_popped = False
        for i in range(len(string) - 1):
            if not has_popped:
                if int(string[i]) < int(string[i+1]):
                    string = trim_string(string, i)
                    has_popped = True
                if i == len(string)-2:
                    if not has_popped:
                        string = string[:-1]
    return string


if __name__ == "__main__":

    total_joltage = 0
    for string in test_strings:
        joltage = find_biggest_12mer(string)
        print(string, joltage)
        total_joltage += int(joltage)
    
    print(f'test joltage:{total_joltage}')
    print(f'test answer: {test_answer}')
    print(test_answer==total_joltage)

    problem_joltage = 0
    with open('/Users/tim/Downloads/aoc2025/d3_input.txt', 'r') as f:
        for line in f:
            string = line.strip()
            joltage = find_biggest_12mer(string)
            print(string, joltage)
            problem_joltage += int(joltage)

    print(f'problem joltage: {problem_joltage}')