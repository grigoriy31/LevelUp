from calc import calc_num2
from data_enter import l
from calc import c
def prnt_data():
    i = 0
    s = l
    a = calc_num2()

    while i < len(s):
        if c == True:
            b = str(s[0])
            i += 1
            if i < len(s):
                b = b + str(s[i])
            elif i == len(s):
                b = b + "=" + str(a)
        else:
            b = print("Спасибо!")
            break
    return b
if prnt_data() != None:
    print(prnt_data())