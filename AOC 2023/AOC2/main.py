# day 2 completed
# #12 red cubes, 13 green cubes, and 14 blue cubes
# Star 1 
CUBES_DICT = {
    'total_cubes' : 39,
    'red': 12,
    'green': 13,
    'blue': 14
}

file = open('input.txt', 'r')
lines = file.readlines()
total = 0
dictionary = {}
def create_dictionary(lines):
    for line in lines: 
        # print(line)
        game, choices = line.strip().split(':')
        list_pulls = choices.strip().split(';')
        cubes_list = []
        for pull in list_pulls: 
            cubes = pull.strip().split(',')
            cube_dict = {}
            for cube in cubes:
                num, color = cube.strip().split(' ')
                cube_dict[color] = int(num)
            cubes_list.append(cube_dict)
            # print(cubes)
        dictionary[game] = cubes_list
    return dictionary
# print(dictionary)

total_blocks = 0
for key in dictionary: 
    # print(key, dictionary[key])
    valid = True
    for index in dictionary[key]:
        for k in index: 
            if index[k] > CUBES_DICT[k]:
                valid = False
    
    if valid == True:
        name, num = key.strip().split(' ')
        total = total + int(num)

# print(total)
   

###
#Star 2 
dictionary = create_dictionary(lines)
# print(dictionary)
sum_of_powers = 0

for key in dictionary: 
    print(key)
    # print(key, dictionary[key])
    min_cubes_dict = {'red': 0, 'blue': 0, 'green': 0}
    for index in dictionary[key]:
        # print(index)
        
        power = 1 
        for k in index: 
            if index[k] > min_cubes_dict[k]:
                min_cubes_dict[k] = index[k]
    print(min_cubes_dict)
        
    for k1 in min_cubes_dict:
        power = min_cubes_dict[k1]*power
        print(power)
    sum_of_powers = sum_of_powers + power

print(sum_of_powers)
