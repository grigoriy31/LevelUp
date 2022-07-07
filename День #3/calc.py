# from check_data import verf
from data_enter import data_input

def calc_num1(data):
    i = -1
    a = 0
    while i < len(data):
        i += 2
        if data[i].append(a.count('/')):
            a = a + int(data[i-1]) / int(data[i+1])
            a.append(data[i-1])
        elif data[i].appened(a.count('*')):
            a = a + int(data[i - 1]) * int(data[i + 1])
            a.append(data[i - 1])
        else:
            continue
        a = data
    return a

def calc_num2(a):
    c = bool
    exm = []
    a = []
    exm, c = verf(exm, c)
    a = calc_num1(a)
    i = -1
    while i < len(a):
        i += 2
        if a[i] == "+":
            a = a + a[i-1] + a[i+1]
        elif a[i] == '-':
            a = a + a[i-1] - a[i+1]
        elif a[i] == '=':
            break
    return a

