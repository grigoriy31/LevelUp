# #Задача 1 Строки
# #a
# n = int(input("Введите кол-во строк: "))
# while n <= 0:
#     n = int(input("Введите кол-во строк: "))
# text = list()
# k = 0
# while k != n:
#     a = input("введите текст: ")
#     text.append(a.count(' '))
#     k += 1
#
# k = 1
# for chek_space in text:
#     print("В строке " + str(k) + " ,количество пробелов: " + str(chek_space))
#     k += 1


# #b
# def check_text(test):
#     b = test[0]
#     i = 0
#     while i < len(test):
#          i += 1
#          if i < len(test):
#               b = b + " " + test[i]
#          elif i == len(test):
#                b = b + "."
#     print(b)
#
# test = list(iter(input, ''))
# check_text(test)

#b part 2 (c функцией)
def check_text(test):
    i = 1
    b = test[0]
    while i < len(test):
        i += 1
        if i < len(test):
            b = b + ' ' + test[i-1]
        if i == len(test):
            b = b + ' ' + test[i-1] + "."
        else:
            continue
    print(b)
n = int(input("Введите кол-во строк: "))
while n <= 0:
    n = int(input("Введите кол-во строк: "))
test = list()
k = 0
while k != n:
    a = input("введите текст: ")
    test.append(a)
    k += 1
check_text(test)
#b(без функции)
# b = test[0]
# i = 0
# while i < len(test):
#     i += 1
#     if i < len(test):
#         b = b + ' ' + str(test[i]) + "."
#     else:
#         continue
#     print(b)