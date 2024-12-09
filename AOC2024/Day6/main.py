
### If there is something directly in front of you, turn right 90 degrees.
### Otherwise, take a step forward.


### continue the following until you are out of range
### move up until you hit # 
### move right until you hit # 
### move down until you hit # 
### move left until you hit # 
### move up until you hit # 


def move_upward(grid, index1, index2):
    if index1-1 < 0: 
        return "stop"
    else:
        if grid[index1-1][index2] != "#":
            grid[index1-1][index2] = "X"
        else: 
            move_right(grid, index1, index2)
    

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
                print(f'starting point: {index_row}, {index_col}') 

    print(grid)

part_one('test-input.txt')