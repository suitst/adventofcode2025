import re
import csv

def rotate(commands): # this function doesn't work but I gave up
    counts = 0
    position = 50
    for command in commands:
        direction = re.search('[a-zA-Z]', command).group().lower()
        amount = int(re.search(r'([0-9]+)', command).group())
        if direction == 'r':
            position += amount
            crossings = position // 100
            counts += crossings
            position = position % 100
        elif direction == 'l':
            position -= amount
            crossings = abs(position // 100)
            counts += crossings
            position = position % 100
    return counts


if __name__ == "__main__":
    commands = []
    with open('/Users/tim/Downloads/aoc2025/d1p1_input.csv', mode='r', encoding='utf-8-sig') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row:
                commands.append(row[0].lstrip('\ufeff'))
        counts = rotate(commands)
        print(counts)
    
    test_list = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",

]
print(rotate(test_list))  # Expected: 6