# try each operator + * in 

def test_solution(current_solution, current_numbers):
    print(f'{current_solution}, {current_numbers}')
    total = 0
    current_solution = int(current_solution)
    # if len(current_numbers) == 2:
    #     print('only 2 numbers')
    for index in range(0,len(current_numbers)-1):
        if total != current_solution: 
            ### This only works on the first iteration
            if int(current_numbers[index])*int(current_numbers[index+1]) <= current_solution: 
                total = total + int(current_numbers[index])*int(current_numbers[index+1])
            elif int(current_numbers[index])+int(current_numbers[index+1]) <= current_solution:
                total = total +int(current_numbers[index])+int(current_numbers[index+1])
            else:
                print(f'I dont think this solution works: {current_solution}, {current_numbers}')
    if total == current_solution:
        print(f'Solution works! {current_solution}, {current_numbers}')




def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()
    numbers_list = []
    solutions_list = []

    correct_solutions = []
    
    for line in lines: 
        solution, numbers = line.strip().split(": ")
        solutions_list.append(solution)
        numbers_list.append(numbers.split(" "))
        

    for index in range(0,len(solutions_list)):
        test_solution(solutions_list[index], numbers_list[index])
                
        

part_one('test-input.txt')