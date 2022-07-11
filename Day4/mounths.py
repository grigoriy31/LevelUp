def day_mounths(a):

    if a < 1:
        b = "Не верный ввод!!!"
    elif a > 12:
        b = "Не верный ввод!!!"
    elif 1 < a <= 7:
        if a == 2:
            b = 28
        elif (a % 2) == 0:
            b = 30
        else:
            b = 31
    elif 7 < a <= 12:
        if (a % 2) == 0:
            b = 31
        else:
            b = 28
    return b

