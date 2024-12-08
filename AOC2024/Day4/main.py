def check_diagonal_left_up(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if index1-count < 0 or index2 - count < 0:
                found = False
            else:
                if grid[index1-count][index2-count] == letters[count]:
                    continue
                else: 
                    found = False
        if found == True:
            print("Diagonal Left Up Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_vertical_up(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if index1-count < 0:
                found = False
            else:
                if grid[index1-count][index2] == letters[count]:
                    continue
                else: 
                    found = False
        if found == True:
            print("Vertical Up Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_diagonal_right_up(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if index1-count < 0:
                found = False
            else:
                if grid[index1-count][index2+count] == letters[count]:
                    continue
                else: 
                    found = False
        if found == True:
            print("Diagonal Right Up Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_horizontal_left(grid, index1, index2):
    try:
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if index2 - count < 0:
                found = False
            else:
                if grid[index1][index2-count] == letters[count]:
                    continue
                else: 
                    found = False
        if found == True:
            print("Horizontal Left Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_horizontal_right(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if grid[index1][index2+count] == letters[count]:
                continue
            else: 
                found = False
        if found == True:
            print("Horizontal Right Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_diagonal_down_left(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if index2 - count < 0:
                found = False
            else:
                if grid[index1+count][index2-count] == letters[count]:
                    continue
                else: 
                    found = False
        if found == True:
            print("Diagonal Left Down Found")
            return 1
        else:
            return 0
    except:
        return 0

def check_vertical_down(grid, index1, index2):
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if grid[index1+count][index2] == letters[count]:
                # print(grid[index1+count][index2+count])
                continue
            else: 
                found = False
        if found == True:
            print("Vertical Down Found")
            return 1
        else:
            return 0
    except:
        return 0
    
def check_diagonal_down_right(grid, index1, index2):
    # print(f'index1: {index1}, index2: {index2}')
    try:    
        letters = ["X", "M", "A", "S"]
        found = True
        for count in range(1,4):
            if grid[index1+count][index2+count] == letters[count]:
                # print(grid[index1+count][index2+count])
                continue
            else: 
                found = False
        if found == True:
            print("Diagonal Right Down Found")
            return 1
        else:
            return 0
    except:
        return 0

def find_neighbor(grid, index1, index2):
    ##needs to be 4 - not currently finding 5
    #print(f'diagonal_left_up: {check_diagonal_left_up(grid, index1, index2)}')

    ##needs to be 2 - good
    # print(f'vertical_up: {check_vertical_up(grid, index1, index2)}')

    ##needs to be 4 - good
    # print(f'check_diagonal_right_up: {check_vertical_up(grid, index1, index2)}')

    ##needs to be 2 - good
    # print(f'check_horizontal_left: {check_horizontal_left(grid, index1, index2)}')

    ##needs to be 3 - good
    # print(f'check_horizontal_right: {check_horizontal_right(grid, index1, index2)}')

    ##needs to be 1 - good
    # print(f'check_diagonal_down_left: {check_diagonal_down_left(grid, index1, index2)}')

    ##needs to be 1 - good
    # print(f'check_vertical_down: {check_vertical_down(grid, index1, index2)}')

    ##needs to be 1 - good
    ## why is it saying that index 2,2 is right? 
    # print(f'check_diagonal_down_right: {check_diagonal_down_right(grid, index1, index2)}')

    ##somehow is getting 9,1 as an option
    if check_diagonal_left_up(grid, index1, index2) == 1:
        print(f'index1: {index1}, index2: {index2}, letter: {grid[index1][index2]}')
        print(f'index1: {index1-1}, index2: {index2-1}, letter: {grid[index1-1][index2-1]}')
        print(f'index1: {index1-2}, index2: {index2-2}, letter: {grid[index1-2][index2-2]}')
        print(f'index1: {index1-3}, index2: {index2-3}, letter: {grid[index1-3][index2-3]}')

    sum = check_diagonal_left_up(grid, index1, index2)+check_vertical_up(grid, index1, index2)+check_diagonal_right_up(grid, index1, index2)+check_horizontal_left(grid, index1, index2)+check_horizontal_right(grid, index1, index2)+check_diagonal_down_left(grid, index1, index2)+check_vertical_down(grid, index1, index2)+check_diagonal_down_right(grid, index1, index2)
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
    for index_row in range(0, len(letters)):
        for index_col in range(0, len(data)):
            # print(grid[index_row][index_col])
            if grid[index_row][index_col] == "X":
                # print("X")
                total = total + find_neighbor(grid, index_row, index_col)
                # print(total)

    print(total)


    # print(grid)
    



def part_two(input):
    file = open(input, 'r')
    data = file.readlines()
    grid = []
    total = 0 

    for line in data:
        line = line.strip()
        letters = list(line)
        grid.append(letters)
    for index_row in range(0, len(letters)):
        for index_col in range(0, len(data)):
            if grid[index_row][index_col] == "X":
                # print("X")
                total = total + find_neighbor(grid, index_row, index_col)
                # print(total)

    print(total)



part_one('input.txt')
# part_one('input.txt')

part_two('test-input.txt')
# part_two('input.txt')