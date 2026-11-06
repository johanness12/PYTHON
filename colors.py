color_list = []

while True:
    color = input('Sisesta värv või lõpeta (x): ')
    if color.lower() == 'x':
        break
    else:
        if color in color_list:
            continue
        color_list.append(color)

while color_list:
    print (color_list.pop(0))