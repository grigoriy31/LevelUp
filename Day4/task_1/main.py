from data_enter import flg_print
from chek_parameters import k


def run_func():
    l = ["Круг", "Прямоугольник", "Треугольник"]
    i = 1
    g = str
    while i <= 1:
        if k == True:
            if flg_print == 'Круг':
                from сircle import a
                g = a
                i += 1
                continue
            elif flg_print == "Прямоугольник":
                from square import b
                g = b
                i += 1
                continue
            elif flg_print == "Треугольник":
                from triangle import c
                g = c
                i += 1
            continue
        if k == False:
            break
    return g
g = run_func()