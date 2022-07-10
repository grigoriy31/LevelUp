from parameters import parameters_figure, b, c, e
from data_enter import flg_print
def sq_per_tri():
    # b, c, e = parameters_figure()
    p = b + c + e
    sq = (p * (p - b) * (p - c) * (p - e))**(1/2)
    return sq, p
# print(sq_per_tri())
sq, p = sq_per_tri()
c = print("Периметр фигуры " + flg_print + " равен " + str(p) + ", " + "площадь равна " + str(sq))