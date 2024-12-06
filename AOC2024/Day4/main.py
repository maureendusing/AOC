def find_neighbor(grid, index1, index2):
    # print(f'grid: {grid}')
    # print(f'index1: {index1}')
    # print(f'index2: {index2}')
    diagonal_left_up=grid[index1+1][index2-1]
    vertical_up = grid[index1+1][index2]
    diagonal_right_up = grid[index1-1][index2+1]
    horizontal_left = grid[index1][index2-1]
    horizontal_right = grid[index1][index2+1]
    diagonal_down = grid[index1-1][index2-1]
    vertical_down = grid[index1-1][index2]

def part_one(input):
    file = open(input, 'r')
    data = file.readlines()
    grid = []
    # print(data)
    # print(type(data))
    for line in data:
        line = line.strip()
        letters = list(line)
        # print(f'letters: {letters}')
        grid.append(letters)
    
    for index_row in range(0, len(letters)-1):
        for index_col in range(0, len(data)-1):
            # print(grid[index_row][index_col])
            if grid[index_row][index_col] == "X":
                find_neighbor(grid, index_row, index_col)
                print("X")


    # print(grid)
    



def part_two(input):
    file = open(input, 'r')
    data = str(file.readlines())

part_one('test-input.txt')
# part_one('input.txt')

part_two('test-input.txt')
# part_two('input.txt')