def order_pages(pages, current_order):
    if pages[0] in current_order:
        index_first_page=current_order.index(pages[0])
        print(index_first_page)
    else:
        current_order.append(pages[0])
        current_order.append(pages[1])
        print(current_order)

def part_one(input):
    file = open(input, 'r')
    lines = file.readlines()
    current_order = []
    for line in lines:
        pages = line.strip().split('|')
        if pages[0] == '':
            print('start processing repports')
        else:
            order_pages(pages, current_order)
        

        print(f'pages: {pages}')
        


part_one('test-input.txt')