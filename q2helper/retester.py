def print_shit() ->str:
    rows = int(input('enter num'))
    counter = 0
    for i in range((rows)):
        x = '*' * (rows + counter)
        y = '* ' * (rows - 1 + counter)
        print(x)
        print (y)
        counter += 1
print_shit()
    