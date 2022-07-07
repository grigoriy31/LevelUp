from calc import calc_num2
from data_enter import l
def prnt_data():
    i = 0
    s = l
    a = calc_num2()
    b = str(s[0])
    while i < len(s):
        i += 1
        if i < len(s):
            b = b + str(s[i])
        elif i == len(s):
            b = b + "=" + str(a)

    return b

print(prnt_data())