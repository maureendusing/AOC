
### If there is something directly in front of you, turn right 90 degrees.
### Otherwise, take a step forward.


### continue the following until you are out of range
### move up until you hit # 
### move right until you hit # 
### move down until you hit # 
### move left until you hit # 
### move up until you hit # 


def move_upward(grid, index1, index2):
    if grid[index1-1][index2] != "#":
        grid[index1-1][index2] = "X"
        move_upward(grid, index1-1, index2)

    if index1-1 < 0: 
        return "stop"
    if grid[index1-1][index2] == "#":
        print(f'turning right')
        move_right(grid, index1,index2)
        # print(f'HIT SOMETHING, grid: {grid}')
        
def move_right(grid, index1,index2):
    try: 
        if grid[index1][index2+1] != "#":
            grid[index1][index2+1] = "X"
            move_right(grid, index1, index2+1)
        if grid[index1][index2+1] == "#":
            print(f'turning down')
            move_down(grid, index1,index2)
            # print(f'HIT SOMETHING, grid: {grid}')
    except: 
        return "stop"
    
def move_down(grid, index1, index2):
    try:
        if grid[index1+1][index2] != "#":
            grid[index1+1][index2] = "X"
            move_down(grid, index1+1, index2)
        if grid[index1+1][index2] == "#":
            print(f'turning left')
            move_left(grid, index1,index2)
            # print(f'HIT SOMETHING, grid: {grid}')
    except: 
        return "stop"
    
def move_left(grid, index1, index2):
    if grid[index1][index2-1] !="#":
        grid[index1][index2-1] = "X"
        move_left(grid, index1, index2-1)

    if index2-1 < 0: 
        return "stop"
    if grid[index1][index2-1] == "#":
        print(f'turning up')
        move_upward(grid, index1,index2)
        # print(f'HIT SOMETHING, grid: {grid}')

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
    count = 0
    for index_row in range(0, len(letters)):
        for index_col in range(0, len(data)):
            if grid[index_row][index_col] == "X" or grid[index_row][index_col] == "^":
                count = count + 1
    print(f'count: {count}')

#961 is too low 
part_one('test-input.txt')