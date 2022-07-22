a = int(input('Введите число: '))
b = []
i = 2
while i < a:
    if a % i == 0:
        b.append(i)
        i += 1
    else:
        i += 1
print(b)

