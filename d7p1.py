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
    num_splits = 0
    for index, value in enumerate(input_list[0]):
        if value == "S":
            source = index
    
    beam_locs = [source]

    for key in splitter_dict.keys():
        for beam in sorted(beam_locs):
            if beam in splitter_dict[key]:
                num_splits += 1
                if beam+1 not in beam_locs:
                    beam_locs.append(beam+1)
                if beam-1 not in beam_locs:
                    beam_locs.append(beam-1)
                beam_locs.remove(beam)

    return sorted(beam_locs), num_splits


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
    print(test_splitters)

    test_beams, num_splits = generate_beams(test_input, test_splitters)
    print(test_beams, num_splits)

    problem_input_list = get_input_list('/Users/tim/Downloads/aoc2025/d7_input.txt')
    problem_splitters = find_splitters(problem_input_list)
    problem_beams, num_splits = generate_beams(problem_input_list, problem_splitters)
    print(problem_beams, num_splits)

