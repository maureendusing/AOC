file = open('test.txt', 'r')
lines = file.readlines()


def check_zeros(difference_list): 
    for val in difference_list:
        if val !=0:
            return True 
    return False

for line in lines:
    values = line.strip().split(' ')
    print(values)
    difference_list = []
    while True: 
        for i in range(0, len(values)-1):
            difference = int(values[i+1]) - int(values[i])
            difference_list.append(difference)
        if check_zeros(difference_list) == False:
            break
    print(check_zeros(difference_list))
    print(difference_list)
