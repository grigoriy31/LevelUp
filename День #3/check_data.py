from data_enter import data_input
from data_enter import l
def verf():
    exm = l
    i = 0
    c = bool
    k = 0
    while i < len(exm) - 2:
        if k < 3:
            if exm[i+1] != "+" and exm[i+1] != '-' and exm[i+1] != '*' and exm[i+1] != "/":
                data_input()
                k += 1
            elif exm[i].isdigit() != True:
                data_input()
                k += 1
            else:
                c = True
                i += 2
        else:
            print('Превышен лимит поппыток. Попоробуйте позже.')
            c = False

    return exm, c
# print(verf())





