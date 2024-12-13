# If stone is engraved with 0 -> replace with 1 
# if len(stones)%2==0: split in the middle to 2 new stones
    #remove leading zeros 
# else stone = stonex2024
#  

def split_even(stone):
    halfway = int((len(stone)/2))
    print(halfway)    
    print(f'left stone: {stone[0:halfway-1]}')
    left_stone = stone[0:halfway-1]
    right_stone = stone[halfway:]
    return left_stone, right_stone

def part_one(input):
    file = open(input, 'r')
    data = file.read()
    stones = (data.split(" "))
    
    new_stones = []

    for index in range(0,len(stones)):
        current_stone = stones[index]
        if current_stone == '0':
            stones[index] = 1
            new_stones.append(stones[index])
        elif len(current_stone)%2==0: 
            left_stone, right_stone = split_even(current_stone)
            new_stones.append(left_stone)
            new_stones.append(right_stone)
        else: 
            stones[index] = str(int(current_stone)*2024)
            new_stones.append(stones[index])
    print(new_stones)
part_one('test-input.txt')