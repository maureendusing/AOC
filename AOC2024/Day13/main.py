def check_solutions_zero(button_a, button_b, prize):    
    a_button_pushes = 0
    b_button_pushes = 0

    if prize[0]%button_a[0] == 0: 
        a_button_pushes = prize[0]/button_a[0]

    if prize[1]%button_b[1] == 0:
        if a_button_pushes > 0 and prize[1]/button_b[1] <a_button_pushes*3:

            b_button_pushes = prize[1]/button_b[1]
            a_button_pushes = 0
    print(f'button_a: {button_a}, button_b: {button_b}, prize: {prize}')
    return a_button_pushes, b_button_pushes

def process_systems_of_equations(button_a, button_b, prize):
    """doing this by solving for b"""

    determinant=button_a[0]*button_b[1]-button_a[1]*button_b[0]
    if determinant !=0:

        subtraction_variable = button_a[1]*button_b[0] - button_b[1]*button_a[0]
        subtract_equals_to = (button_a[1])*prize[0] - (prize[1])*button_a[0]

        b_button_pushes = subtract_equals_to/subtraction_variable


        a_button_pushes = (prize[0] - button_b[0]*b_button_pushes)/button_a[0]
    if determinant == 0:
        print('in if')
        a_button_pushes,b_button_pushes =check_solutions_zero(button_a, button_b, prize)
        # a_button_pushes = 0
        # b_button_pushes = 0
        
    return a_button_pushes, b_button_pushes




def calculate_total(a_button_pushes, b_button_pushes, prize):
    if a_button_pushes%1 ==0 and b_button_pushes%1==0 and a_button_pushes <= 100 and b_button_pushes <= 100:
        total = 3*a_button_pushes + b_button_pushes
    else: 
        return 0
    return total

def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()

    button_a = []
    button_b = []
    prize = []
    tokens = 0

    count = 0 
    for line in lines:
        count = count + 1
        if count%4 !=0:
            button, formula = line.strip().split(':')
            x, y = formula.strip().split(', ')

            if button == "Button A":
                _, x = x.strip().split('+') or 1
                _, y = y.strip().split('+') or 1
                button_a = [int(x),int(y)]
            if button == "Button B":
                _, x = x.strip().split('+') or 1
                _, y = y.strip().split('+') or 1
                button_b = [int(x),int(y)]
            if button == "Prize":
                _, x = x.strip().split('=')
                _, y = y.strip().split('=')
                prize = [int(x),int(y)]

        else: 
            button_a_pushes, button_b_pushes = process_systems_of_equations(button_a, button_b, prize)
            # if calculate_total(button_a_pushes, button_b_pushes, prize) == 0:
            #     print(f'didnt work {button_a}, {button_b}, {prize}')
            # print(f'a_button_pushes else block: {button_a_pushes}')
            tokens = tokens + calculate_total(button_a_pushes, button_b_pushes, prize)
            
            button_a = []
            button_b = []
            prize = []

    ## 25531 too low
    print(f'tokens:{tokens}')

part_one('input.txt')