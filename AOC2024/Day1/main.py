###Day 1


def part_one():
    file = open('input.txt', 'r')
    lines = file.readlines()

    first_column = []
    second_column = []
    for line in lines: 
        count = 0
        first_column_num, second_column_num = line.strip().split('   ')
        first_column.append(int(first_column_num))
        second_column.append(int(second_column_num))
        # for char in line: 
        #     if char.isnumeric(): 
        #         count = count + 1
        #         if char.isnumeric() and count ==1:
        #             first_column.append(char)
        #         elif char.isnumeric() and count ==2:
        #             second_column.append(char)

    first_column.sort()
    second_column.sort()
    print(f"first_column: {first_column}")
    print(f"second_column: {second_column}")

    total = 0

    for index in range(0, len(first_column)):
        difference = int(second_column[index]) - int(first_column[index])
        if difference < 0:
            difference = -difference
        total = total + difference
    
    print(f"total:{total}")

def part_two():
    file = open('input2.txt', 'r')
    lines = file.readlines()

    first_column = []
    second_column = []
    for line in lines: 
        count = 0
        first_column_num, second_column_num = line.strip().split('   ')
        first_column.append(int(first_column_num))
        second_column.append(int(second_column_num))

    first_column.sort()
    second_column.sort()
    print(f"first_column: {first_column}")
    print(f"second_column: {second_column}")

    total = 0

    for index1 in range(0, len(first_column)):
        similarity = 0
        for index2 in range(0, len(second_column)):
            if first_column[index1] == second_column[index2]:
                similarity = similarity + 1
        total = total + similarity*first_column[index1]
    
    print(f"total:{total}")

part_two()