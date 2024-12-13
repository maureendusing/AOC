def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()

    button_a = []
    button_b = []
    prize = []

    def check_button_a(button_a, prize):
        print(f'button_a: {button_a}, prize:{prize}')
        print(f'mod: {(int(prize[1])/int(button_a[1]))%1}')

        if (int(prize[0])/int(button_a[0]))%1 == 0 and (int(prize[1])/int(button_a[1]))%1 == 0:
            return True
        else:
            return False
        
    def check_button_b(button_b, prize):
        print(f'button_b: {button_b}, prize:{prize}')
        print(f'mod: {(int(prize[1])/int(button_b[1]))%1}')

        if (int(prize[0])/int(button_b[0]))%1 == 0 and (int(prize[1])/int(button_b[1]))%1 == 0:
            return True
        else:
            return False

    for line in lines:
        try:
            button, formula = line.strip().split(':')
            # print(f'formula: {formula}')
            x, y = formula.strip().split(', ')

            if button == "Button A":
                _, x = x.strip().split('+')
                _, y = y.strip().split('+')
                print(f'x: {x}, y:{y}')
                button_a = [x,y]
            if button == "Button B":
                _, x = x.strip().split('+')
                _, y = y.strip().split('+')
                button_b = [x,y]
            if button == "Prize":
                _, x = x.strip().split('=')
                _, y = y.strip().split('=')
                prize = [x,y]
                if check_button_a(button_a, prize) or check_button_b(button_b, prize):
                    print("yay")
                else: 
                    print('boo')
            # print(f'button: {button} formula: {formula}')

        except Exception as err:
            button_a = []
            button_b = []
            prize = []
            print(err)

    


    # for line in lines: 
    #     line.strip()
    #     print(line)

    # print(lines)

part_one('test-input.txt')