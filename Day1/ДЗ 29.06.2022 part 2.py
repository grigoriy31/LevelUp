
a = int(input("Введите номер месяца: "))
if a < 1:
    print("Не верный ввод!!!")
elif a > 12:
    print("Не верный ввод!!!")
elif 1< a <= 7:
    if a == 2:
        print("ФЕВРАЛЬ")
    elif(a % 2) == 0:
        print("30")
    else:
        print("31")
elif 7 < a <= 12:
    if(a % 2) ==0:
        print("31")
    else:
        print("30")
