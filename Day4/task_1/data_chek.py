from data_enter import flg_print, dat_enter


def check_data():
    a = flg_print
    k = 0
    fig = str
    while k < 3:

        if a == ("Треугольник") or a == ("Прямоугольник") or a == ("Круг"):
            fig = a
            f = True
            break
        else:
            print("Введены не верные данные")
            dat_enter()
            k += 1
    if k == 3:
        f = False
        print("Превышено количество попыток")

    return fig, f
flg, f = check_data()

# print(check_data())