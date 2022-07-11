date =[]
date = input("Введите данные: ").split()
a = int(date[0])
b = int(date[1])
c = int(date[2])
D = b**2 - 4 * a * c



def diskriminante():
    if D > 0:
        root1 = (-b + (D ** 0.5)) / (2 * a)
        root2 = (-b- (D ** 0.5)) / (2 * a)
        d = 'X1 = ' + str(root1) + ',' + 'x2 = ' + str(root2)
    if D == 0:
        root1 = -b / (2 * a)
        root2 = None
        d = 'x1 = ' + str(root1)
    if D < 0:
        root1 = None
        root2 = None
        d = 'Нет корней'
    return d

print(diskriminante())