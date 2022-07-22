# a = int(input('Введите число: '))

def list():
    b = []
    i = 2
    while i < a:
        if a % i == 0:
            b.append(i)
            i += 1
        else:
            i += 1
    return b
# print(b)
def summ():
    i = 0
    b = list()
    summ = 0
    for i in b:
        summ += i
    if summ == a:
        out = True
    else:
        out = False
    return out
for a in range(10000):
    if summ(a) == True:
        print(a)




