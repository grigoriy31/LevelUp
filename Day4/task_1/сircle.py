from parameters import parameters_figure, b
from data_enter import flg_print
from math import pi




def sq_per_cir():
    # b, c, e, flg = parameters_figure()
    p = 2 * pi * b
    sq = pi * (b ** 2)
    return sq, p
sq, p = sq_per_cir()
a = print("Периметр фигуры " + flg_print + " равен " + str(p) + ", " + "площадь равна " + str(sq))
