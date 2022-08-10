from os.path import exists

way = input('Введите путь к файлу: ')

file_exists = exists(str(way))
if file_exists == True:
    with open(str(way), encoding='utf8') as f:
        data = [line.strip() for line in f]
    a = data[0]
    for text in data:
        if len(a) > len(text):
            a = a
        else:
            a = text
    print(a)
else:
    print('Not Found')




