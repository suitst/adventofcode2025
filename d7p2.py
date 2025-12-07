import numpy as np


def find_splitters(input_list):
    splitter_dict = {}

    for list_index, value in enumerate(input_list):
        splitters = []
        for index, char in enumerate(value):
            if char == "^":
                splitters.append(index)
        splitter_dict[list_index] = splitters
    return splitter_dict


def count_timelines(input_list, splitter_dict):
    beam_array = np.zeros((len(input_list), len(input_list[0])))

    for index, value in enumerate(input_list[0]):
        if value == "S":
            beam_array[0][index] = 1

    for key, index in enumerate(splitter_dict.keys()):
        for splitter in splitter_dict[key]:
            for pos in range(index, len(input_list[0])+1):
                beam_array[pos][splitter-1] += beam_array[index-2][splitter]
                beam_array[pos][splitter+1] += beam_array[index-2][splitter]
                beam_array[pos][splitter] = 0
    
    return  sum(beam_array[-2])


def get_input_list(path):
    input_list = []
    with open(path, 'r') as f:
        for line in f:
            string = line.strip()
            input_list.append(string)
    return input_list


if __name__ == "__main__":

    test_input = [
        '.......S.......',
        '.......|.......',
        '.......^.......',
        '...............',
        '......^.^......',
        '...............',
        '.....^.^.^.....',
        '...............',
        '....^.^...^....',
        '...............',
        '...^.^...^.^...',
        '...............',
        '..^...^.....^..',
        '...............',
        '.^.^.^.^.^...^.',
        '...............',
    ]

    test_splitters = find_splitters(test_input)
    test_timelines = count_timelines(test_input, test_splitters)
    print(test_timelines)

    problem_input_list = get_input_list('/Users/tim/Downloads/aoc2025/d7_input.txt')
    problem_splitters = find_splitters(problem_input_list)
    problem_timelines = count_timelines(problem_input_list, problem_splitters)
    print(problem_timelines)

