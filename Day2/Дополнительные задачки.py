# # #Задача 1 Строки:
# # #a вывод колво пробелов в каждой строке
# # n = int(input("Введите кол-во строк: "))
# # while n <= 0:
# #     n = int(input("Введите кол-во строк: "))
# # text = list()
# # k = 0
# # while k != n:
# #     a = input("введите текст: ")
# #     text.append(a.count(' '))
# #     k += 1
# #
# # k = 1
# # for chek_space in text:
# #     print("В строке " + str(k) + " ,количество пробелов: " + str(chek_space))
# #     k += 1
#
# #a вывод кол-во пробелов общее
# # def check_space(test):
# #     i = 0
# #     k = 0
# #     while i < len(test):
# #         a = test[i]
# #         text.append(a.count(' '))
# #         k += 1
# #         i += 1
# #     print(k)
# # text = list()
# # test = list(iter(input, ''))
# # check_space(test)
#
#
# # #b
# # def check_text(test):
# #     b = test[0]
# #     i = 0
# #     while i < len(test):
# #          i += 1
# #          if i < len(test):
# #               b = b + " " + test[i]
# #          elif i == len(test):
# #                b = b + "."
# #     print(b)
# #
# # test = list(iter(input, ''))
# # check_text(test)
#
# #b part 2 (c функцией)
# # def check_text(test):
# #     i = 1
# #     b = test[0]
# #     while i < len(test):
# #         i += 1
# #         if i < len(test):
# #             b = b + ' ' + test[i-1]
# #         if i == len(test):
# #             b = b + ' ' + test[i-1] + "."
# #         else:
# #             continue
# #     print(b)
# # n = int(input("Введите кол-во строк: "))
# # while n <= 0:
# #     n = int(input("Введите кол-во строк: "))
# # test = list()
# # k = 0
# # while k != n:
# #     a = input("введите текст: ")
# #     test.append(a)
# #     k += 1
# # check_text(test)
#
# #b(без функции)
# # b = test[0]
# # i = 0
# # while i < len(test):
# #     i += 1
# #     if i < len(test):
# #         b = b + ' ' + str(test[i]) + "."
# #     else:
# #         continue
# #     print(b)
#
# #Функции
# #a
#
# # def mini_calculator(a, b):
# #     if mc == "/":
# #         d = a / b
# #     elif mc == "*":
# #         d = a * b
# #     elif mc == '+':
# #         d = a + b
# #     elif mc == '-':
# #         d = a - b
# #     print(d)
# # num = input("Введите числа: ").split()
# # if 2 < len(num):
# #     num = input("Введите числа: ").split()
# # else:
# #     sign = input("Введите действие: ")
# #     if 1 != len(sign):
# #         sign = input("Введите действие: ")
# #     elif sign != '/' and sign != '*' and sign != '+' and sign != "-":
# #         sign = input("Введите действие: ")
# # a, b = int(num[0]), int(num[1])
# # mc = str(sign)
# #
# # mini_calculator(a, b)
#
# #b прописал проверки на ввод положительных чисел
def check_data_entry(a, c):
    for k in range (3):
          if k != 2:
                if a[0].isdigit() == a[1].isdigit() == True:
                    if len(a) != 2:
                        a = input("Введите сумму вклада и скрок: ").split()
                    elif len(a) == 2:
                        if int(a[0]) <= 0 or int(a[1]) <= 0:
                            a = input("Введите сумму вклада и скрок: ").split()
                        elif int(a[0]) > 0 and int(a[1]) > 0:
                            c = True
                            break
                else:
                    a = input("Введите сумму вклада и скрок: ").split()
          elif k == 2:
              if a[0].isdigit() == a[1].isdigit() == True:
                    if len(a) != 2:
                        a = print("Превышено число попыток. Попоробуйте позже.")
                        c = False
                        break
                    elif len(a) == 2:
                        if int(a[0]) <= 0 or int(a[1]) <= 0:
                            a = print("Превышено число попыток. Попоробуйте позже.")
                            c = False
                            break
                        elif int(a[0]) > 0 and int(a[1]) > 0:
                            c = True
                            break
              else:
                  a = print("Превышено число попыток. Попоробуйте позже.")
                  c = False
                  break
    return a, c


def calc_dep(a):
    c = bool
    a, c = check_data_entry(a, c)
    i = 0
    b = int(a[0])
    while i < int(a[1]):
        b += b / 10
        i += 1
    return b

def check_calc_data(a):
    c = bool
    a, c = check_data_entry(a, c)
    while c == True:
        calc_dep(a)
        a = calc_dep(a)
        break
    if c == False:
        pass
    return a


a = input("Введите сумму вклада и скрок: ").split()


# print(check_calc_data(a))
# print(check_data_entry(a,c))



print(check_calc_data(a))


# calc_dep(a)

