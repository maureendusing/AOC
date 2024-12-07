def check_diagonal_left_up(grid, index1, index2):
    try:
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            # print(f'index1: {index1}, index2: {index2}')
            # print(f'count: {count}, letter: {letters[count]}')
            if grid[index1-count][index2-count] == letters[count]:
                print(f'count: {count}, letter: {letters[count]}, grid: {grid[index1-count][index2-count]}')
                # print(grid[index1+count][index2+count])
                continue
            else: 
                found = False
                break
        if found == True:
            return 1
        else:
            return 0
    except:
        return 0



# def check_vertical_up(grid, index1, index2):
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1-count][index2] == letters[count]:
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

# def check_diagonal_right_up(grid, index1, index2):
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1-count][index2+count] == letters[count]:
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

# def check_horizontal_left(grid, index1, index2):
#     try:
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1][index2-count] == letters[count]:
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

# def check_horizontal_right(grid, index1, index2):
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1][index2+count] == letters[count]:
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

# def check_diagonal_down_left(grid, index1, index2):
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1+count][index2-count] == letters[count]:
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

# def check_vertical_down(grid, index1, index2):
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1+count][index2] == letters[count]:
#                 # print(grid[index1+count][index2+count])
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0
    
# def check_diagonal_down_right(grid, index1, index2):
#     # print(f'index1: {index1}, index2: {index2}')
#     try:    
#         letters = ["X", "M", "A", "S"]
#         found = True
#         for count in range(1,4):
#             if grid[index1+count][index2+count] == letters[count]:
#                 # print(grid[index1+count][index2+count])
#                 continue
#             else: 
#                 found = False
#         if found == True:
#             return 1
#         else:
#             return 0
#     except:
#         return 0

def find_neighbor(grid, index1, index2):
    # print(f'grid: {grid}')
    # print(f'index1: {index1}')
    # print(f'index2: {index2}')

    # diagonal_left_up=grid[index1-1][index2-1]
    # vertical_up = grid[index1-1][index2]
    # diagonal_right_up = grid[index1-1][index2+1]
    # horizontal_left = grid[index1][index2-1]
    # horizontal_right = grid[index1][index2+1]
    # diagonal_down = grid[index1+1][index2-1]
    # vertical_down = grid[index1+1][index2]
    # diagonal_down_right = grid[index1+1][index2+1]
    test_case = check_diagonal_left_up(grid, 5, 6)
    print(f'test_case: {test_case}')
    ##needs to be 4 - not
    print(f'diagonal_left_up: {check_diagonal_left_up(grid, index1, index2)}')

    ##needs to be 2 
    # print(f'vertical_up: {check_vertical_up(grid, index1, index2)}')

    ##needs to be 4 - not
    # print(f'check_diagonal_right_up: {check_vertical_up(grid, index1, index2)}')

    ##needs to be 2 - not 
    # print(f'check_horizontal_left: {check_horizontal_left(grid, index1, index2)}')

    ##needs to be 3
    # print(f'check_horizontal_right: {check_horizontal_right(grid, index1, index2)}')

    ##needs to be 1
    # print(f'check_diagonal_down_left: {check_diagonal_down_left(grid, index1, index2)}')

    ##needs to be 1
    # print(f'check_vertical_down: {check_vertical_down(grid, index1, index2)}')

    ##needs to be 1 
    ## why is it saying that index 2,2 is right? 
    # print(f'check_diagonal_down_right: {check_diagonal_down_right(grid, index1, index2)}')

    sum = check_diagonal_left_up(grid, index1, index2)
    # sum = check_diagonal_left_up(grid, index1, index2)+check_vertical_up(grid, index1, index2)+check_diagonal_right_up(grid, index1, index2)+check_horizontal_left(grid, index1, index2)+check_horizontal_right(grid, index1, index2)+check_diagonal_down_left(grid, index1, index2)+check_vertical_down(grid, index1, index2)+check_diagonal_down_right(grid, index1, index2)
    return sum


def part_one(input):
    file = open(input, 'r')
    data = file.readlines()
    grid = []
    total = 0 
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
                # print("X")
                total = total + find_neighbor(grid, index_row, index_col)
                # print(total)

    print(total)


    # print(grid)
    



def part_two(input):
    file = open(input, 'r')
    data = str(file.readlines())

part_one('test-input.txt')
# part_one('input.txt')

part_two('test-input.txt')
# part_two('input.txt')