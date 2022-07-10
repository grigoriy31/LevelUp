from parameters import b, c, e, flg_print
from data_chek import f
def ch_parameters():
    if f == True:
        if flg_print == "Круг":
            if b <= 0:
                print('Введены не верные данные. Попробуйте позже')
                k = False
            else:
                print('Cпасибо')
                k = True
        if flg_print == "Прямоугольник":
                if b <= 0 or c <= 0:
                    print('Введены не верные данные. Попробуйте позже')
                    k = False
                else:
                    print('Cпасибо')
                    k = True
        if flg_print == "Треугольник":
                if b <= 0 or c <= 0 or e <= 0:
                    print('Введены не верные данные. Попробуйте позже')
                    k = False
                else:
                    print('Cпасибо')
                    k = True
        return k
k = ch_parameters()