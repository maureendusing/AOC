
### If there is something directly in front of you, turn right 90 degrees.
### Otherwise, take a step forward.


### continue the following until you are out of range
### move up until you hit # 
### move right until you hit # 
### move down until you hit # 
### move left until you hit # 
### move up until you hit # 


def move_upward(grid, index1, index2):
    while index1-1 > 0 and grid[index1-1][index2] != "#":
        grid[index1-1][index2] = "X"
        index1=index1-1
        move_upward(grid, index1, index2)

    if index1-1 < 0: 
        return "stop"
    if grid[index1-1][index2] == "#":
        move_right(grid, index1,index2)
        print(f'HIT SOMETHING, grid: {grid}')
        
def move_right(grid, index1,index2):
    try: 
        while grid[index1][index2+1] != "#":
            grid[index1][index2+1] = "X"
            index2=index2+1
            move_right(grid, index1, index2)
        if grid[index1][index2+1] == "#":
            move_down(grid, index1,index2)
            print(f'HIT SOMETHING, grid: {grid}')
    except: 
        return "stop"
    
def move_down(grid, index1, index2):
    try:
        while grid[index1+1][index2] != "#":
            grid[index1+1][index2] = "X"
            index1=index1+1
            move_down(grid, index1, index2)
        if grid[index1+1][index2] == "#":
            move_down(grid, index1,index2)
            print(f'HIT SOMETHING, grid: {grid}')
    except: 
        return "stop"
    
def move_left(grid, index1, index2):
    while index2-1 > 0 and grid[index1][index2-1] != "#":
        grid[index1][index2-1] = "X"
        index2=index2-1
        move_upward(grid, index1, index2)

    if index1-1 < 0: 
        return "stop"
    if grid[index1-1][index2] == "#":
        move_upward(grid, index1,index2)
        print(f'HIT SOMETHING, grid: {grid}')

def part_one(input):
    file = open(input, 'r')
    data = file.readlines()
    grid = []

    for line in data:
        line = line.strip()
        letters = list(line)
        grid.append(letters)
    for index_row in range(0, len(letters)):
        for index_col in range(0, len(data)):
            if grid[index_row][index_col] == "^":
                starting_row_index = index_row
                starting_col_index = index_col
                print(f'starting point: {index_row}, {index_col}') 
    
    move_upward(grid, starting_row_index, starting_col_index)

    print(grid)

part_one('test-input.txt')