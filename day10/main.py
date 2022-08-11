
with open(input('Введите имя файлa для открытия: '), 'r') as f:
    with open(input('Введите имя файла для записи: '), 'w') as t:
        lines = f.readlines()
        for i in lines:
            if i[0] != '#':
                t.write(i)



