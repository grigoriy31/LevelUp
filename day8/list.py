# a = int(input('Введите число: '))

def num_list(a):
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
    t = bool
    i = 0
    b = num_list(a)
    summ = 0
    for i in b:
        summ += i
        if summ == a:
            t = True
        else:
            t = False
    return t
for a in range(1, 10000):
    if summ() == True:
        print(a)




