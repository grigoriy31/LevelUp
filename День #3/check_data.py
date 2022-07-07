from data_enter import data_input
from calc import calc_num2, calc_num1
def verf():
    exm = data_input()
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
print(verf())
c = bool
exm, c = verf(exm, c)
print(exm, c)

# def verf_final():
#     c = bool
#     exm = []
#     exm, c = verf(exm, c)
#     while c == True:
#         # calc_num2()
#         # break
#     print(1)
#     if c == False:
#         # pass
#         print(2)
#
#
# print(verf_final())

