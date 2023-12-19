file = open('input.txt', 'r')
lines = file.readlines()
count = 0
for line in lines:
    p1, p2 = line.strip().split(',')
    p1_lower, p1_upper = p1.strip().split('-')
    p2_lower, p2_upper = p2.strip().split('-')
    p1_list = []
    p2_list = []
    
    in_list = False
    for index in range(int(p1_lower), (int(p1_upper)+1)):
        p1_list.append(index)
    for index in range(int(p2_lower), (int(p2_upper)+1)):
        p2_list.append(index)
    if any(p1_list in p2_list for p1_list in range(0, len(p2_list))):
        count = count + 1
    print(p1_list)
    print(p2_list)
    print(count)