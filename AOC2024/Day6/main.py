
### If there is something directly in front of you, turn right 90 degrees.
### Otherwise, take a step forward.


### continue the following until you are out of range
### move up until you hit # 
### move right until you hit # 
### move down until you hit # 
### move left until you hit # 
### move up until you hit # 
import sys


sys.setrecursionlimit(10000)

def move_upward(grid, index1, index2):
    while index1-1>=0 and grid[index1-1][index2] != "#":
        grid[index1-1][index2] = "X"
        index1=index1-1

    if grid[index1-1][index2] == "#":
        print(f'turning right')
        move_right(grid, index1,index2)

        # print(f'HIT SOMETHING, grid: {grid}')
    
    else: 
        print('stopped going up off page')
        
def move_right(grid, index1,index2):
    while index2<len(grid[0]) and grid[index1][index2+1] != "#": 
        grid[index1][index2+1] = "X"
        index2 = index2 + 1
    if grid[index1][index2+1] == "#":
        print(f'turning down')
        move_down(grid, index1,index2)
        # print(f'HIT SOMETHING, grid: {grid}')
    else: 
        print('stopped going right off page')

    
def move_down(grid, index1, index2):
    while index1 < len(grid[0]) and grid[index1+1][index2] != "#":
        grid[index1+1][index2] = "X"
        index1 = index1 + 1
    if grid[index1+1][index2] == "#":
        print(f'turning left')
        move_left(grid, index1,index2)
        # print(f'HIT SOMETHING, grid: {grid}')
    else: 
        print('stopped going down off page')
    
def move_left(grid, index1, index2):
    while index2-1 >= 0 and grid[index1][index2-1] !="#":
        grid[index1][index2-1] = "X"
        index2=index2-1
        
    if grid[index1][index2-1] == "#":
        print(f'turning up')
        move_upward(grid, index1,index2)
        # print(f'HIT SOMETHING, grid: {grid}')
    else: 
        print('stopped going left off page')

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

    
    count = 0
    for index_row in range(0, len(letters)):
        for index_col in range(0, len(data)):
            if grid[index_row][index_col] == "X" or grid[index_row][index_col] == "^":
                count = count + 1
    for row in grid:
        print("".join(map(str, row)))

    
    # print(f'grid: {grid}')

    print(f'count: {count}')

#961 is too low 
part_one('input.txt')