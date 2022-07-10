from data_chek import flg, f

def parameters_figure():
    a = flg

    l = []
    if f == True:
        if a == "Круг":
             b = input('Введите радиус: ')
             c = 0
             e = 0
        elif a == "Прямоугольник":
            l = input('Введите длинну сторон: ').split()
            b = l[0]
            c = l[1]
            e = 0
        else:
            l = input('Введите длинны сторон: ').split()
            b = l[0]
            c = l[1]
            e = l[2]
    if f == False:
        b = 0
        c = 0
        e = 0
        print("Спасибо, попробуйте позже")
    return b, c, e, flg
b, c, e, flg = parameters_figure()
b = int(b)
c = int(c)
e = int(e)
flg_print = str(flg)