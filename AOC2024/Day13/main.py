def process_systems_of_equations(button_a, button_b, prize):
    """doing this by solving for b"""

    subtraction_variable = button_a[1]*button_b[0] - button_b[1]*button_a[0]
    ### this is wrong 
    subtract_equals_to = (button_a[1])*prize[0] - (prize[1])*button_a[0]
    
    print(f'subtraction_variable: {subtraction_variable}, subtraction_equals:{subtract_equals_to}')

    b_button_pushes = subtract_equals_to/subtraction_variable


    a_button_pushes = (prize[0] - button_b[0]*b_button_pushes)/button_a[0]

    print(f'a_button_pushes: {a_button_pushes},b_button_pushes: {b_button_pushes}')
    return a_button_pushes, b_button_pushes

def calculate_total(a_button_pushes, b_button_pushes, prize):
    if a_button_pushes%1 ==0 and b_button_pushes%1==0 and a_button_pushes < 100 and b_button_pushes < 100:
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
        print(f'count: {count}')
        print(f'line: {line}')
        if count%4 !=0:
            button, formula = line.strip().split(':')
            x, y = formula.strip().split(', ')

            if button == "Button A":
                _, x = x.strip().split('+')
                _, y = y.strip().split('+')
                print(f'x: {x}, y:{y}')
                button_a = [int(x),int(y)]
            if button == "Button B":
                _, x = x.strip().split('+')
                _, y = y.strip().split('+')
                button_b = [int(x),int(y)]
            if button == "Prize":
                _, x = x.strip().split('=')
                _, y = y.strip().split('=')
                prize = [int(x),int(y)]

        else: 
            button_a_pushes, button_b_pushes = process_systems_of_equations(button_a, button_b, prize)
            tokens = tokens + calculate_total(button_a_pushes, button_b_pushes, prize)
            
            button_a = []
            button_b = []
            prize = []
    print(f'tokens:{tokens}')

part_one('input.txt')