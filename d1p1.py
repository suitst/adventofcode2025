import re
import csv

def rotate(commands):
    counts = 0
    position = 50
    for command in commands:
        direction = re.search('[a-zA-Z]', command).group().lower()
        amount = int(re.search(r'([0-9]+)', command).group())
        if direction == 'r':
            position += amount
        elif direction == 'l':
            position -= amount
        position = position % 100
        
        if position == 0:
            counts += 1
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