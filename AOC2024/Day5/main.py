def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()

    for line in lines:
        page_one, page_two = line.strip().split('|')


part_one('test-input.txt')