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


def generate_beams(input_list, splitter_dict):
    source = 0
    timelines = 0
    for index, value in enumerate(input_list[0]):
        if value == "S":
            source = index
    
    beam_locs = [source]
    for key in splitter_dict.keys():
        was_split = []
        num_splits = 0
        for beam in sorted(beam_locs):
            if beam in splitter_dict[key]:
                num_splits += 1
                was_split.append(beam)
                if beam+1 not in beam_locs:
                    beam_locs.append(beam+1)
                if beam-1 not in beam_locs:
                    beam_locs.append(beam-1)
                beam_locs.remove(beam)
        was_not_split = [beam for beam in beam_locs if beam not in was_split]
        if len(splitter_dict[key]) > 0:
            timelines += (2 * num_splits)
            #print(splitter_dict[key])
            #print(sorted(beam_locs))
            #print(timelines)

    return sorted(beam_locs), num_splits, timelines


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

