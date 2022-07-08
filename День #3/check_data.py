from data_enter import data_input
from data_enter import l
def verf():
    exm = l
    i = 0
    c = bool
    k = 0
    while i < len(exm):
        if k < 2:
            if i < len(exm) - 1:
                if exm[i+1] != "+" and exm[i+1] != '-' and exm[i+1] != '*' and exm[i+1] != "/":
                    data_input()
                    k += 1
                elif exm[i].isdigit() != True:
                    data_input()
                    k += 1
                else:
                    c = True
                    i += 2
            elif i == len(exm) - 1:
                if exm[i].isdigit() != True:
                    data_input()
                    k += 1
                else:
                    c = True
                    i += 2
        else:
            c = False
            break

    return exm, c
# print(verf())





