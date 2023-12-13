def star_one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total_cals = 0
    count = 1 
    mapping = {}
    for line in lines:
        if line == '\n':
            mapping[count] = total_cals
            count = count + 1 
            total_cals = 0
        else: 
            total_cals = total_cals + int(line)
    mapping[count] = total_cals
    most_cals = 0
    for key in mapping: 
        if mapping.get(key) > most_cals: 
            most_cals = mapping.get(key)
    return most_cals
print(star_one())

def star_two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total_cals = 0
    count = 1 
    mapping = {}
    for line in lines:
        if line == '\n':
            mapping[count] = total_cals
            count = count + 1 
            total_cals = 0
        else: 
            total_cals = total_cals + int(line)
    mapping[count] = total_cals
    most_cals = []
    for key in mapping: 
        most_cals.append(mapping.get(key))
        most_cals.sort(reverse=True)
    print(most_cals)
    top3 = 0
    for i in range(1,4):
        top3 = top3 + most_cals[i-1] 

    return top3
print(star_two())