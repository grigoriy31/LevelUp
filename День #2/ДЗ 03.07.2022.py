# Часть 1
#a = input("Введите числа ").split()
#l = []
#for i in range(len(a)):
#    l.append(a[i])
#print("Введенные данные "), print(l)
#print("Максимальное число " + max(l))
#print("Минимальное число " + min(l))
#i = -1
#while i < len(l):
#    i += 1
#    if i == len(l):
#        continue
#    elif int(l[i]) % 3 == 0 and int(l[i]) % 5 != 0:
#       print(l[i])
#    else:
#        continue


# Часть 2
a = input("Введите числа ").split()
l = []
for i in range(len(a)):
    l.append(a[i])
l.sort()
#При желании посмотреть на отосортированый список
#print(l)
i = -1
while i <= len(l):
    i += 1
    if i == len(l):
        continue
    elif i == -1:
        if int(l[i]) != int(l[i + 1]):
            print(l[i])
        else:
            continue
    elif i == len(l) - 1:
        if int(l[i]) != int(l[i - 1]):
            print(l[i])
        else:
            continue
    elif i > -1 and i < len(l) - 1:
        if int(l[i]) != int(l[i - 1]) and int(l[i]) != int(l[i + 1]):
            print(l[i])
        else:
            continue
    else:
        continue