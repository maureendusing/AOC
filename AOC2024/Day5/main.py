def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()

    for line in lines:
        pages = line.strip().split('|')
        print(f'pages: {pages}')


part_one('test-input.txt')