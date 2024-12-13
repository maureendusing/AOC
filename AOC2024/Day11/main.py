def split_even(stone):
    halfway = int((len(stone)/2))
    left_stone = stone[0:halfway]
    left_stone = left_stone.lstrip('0')
    if left_stone == '':
        left_stone = '0'
    right_stone = stone[halfway:]
    right_stone = right_stone.lstrip('0')
    if right_stone == '':
        right_stone = '0'

    return (left_stone, right_stone)

def process_stones(stones):
    new_stones = []

    for index in range(0,len(stones)):
        current_stone = stones[index]
        if current_stone == '0':
            stones[index] = '1'
            new_stones.append(stones[index])
        elif len(current_stone)%2==0: 
            left_stone, right_stone = split_even(current_stone)
            new_stones.append(left_stone)
            new_stones.append(right_stone)
        else: 
            stones[index] = str(int(current_stone)*2024)
            new_stones.append(stones[index])
        # print(new_stones)
    return new_stones


def part_one(input):
    file = open(input, 'r')
    data = file.read()
    stones = (data.split(" "))
    
    for i in range(6):
        stones = process_stones(stones)
        print(f'after iteration {i+1}: {stones}')
    # new_stones = []

    # for index in range(0,len(stones)):
    #     current_stone = stones[index]
    #     if current_stone == '0':
    #         stones[index] = 1
    #         new_stones.append(stones[index])
    #     elif len(current_stone)%2==0: 
    #         left_stone, right_stone = split_even(current_stone)
    #         new_stones.append(left_stone)
    #         new_stones.append(right_stone)
    #     else: 
    #         stones[index] = str(int(current_stone)*2024)
    #         new_stones.append(stones[index])
    # print(new_stones)
part_one('test-input.txt')