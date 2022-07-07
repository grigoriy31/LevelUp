from check_data import verf

# print(data_input())
# print(verf())
с = bool
exm, c = verf()



def calc_num1():
    exn = exm
    t = []
    for i in range(len(exn)):
        t.append(exn[i])
    i = -1
    a = 0
    b = len(exm) - 2
    while i < b:
        i += 2
        if str(t[i]) == "/":
            a = int(t[i-1]) / int(t[i+1])
            del t[i-1:i+2]
            t.insert(i - 1, a)
            i -= 2
            b -= 2
        elif str(t[i]) == "*":
            a = int(t[i - 1]) * int(t[i + 1])
            del t[i - 1:i + 2]
            t.insert(i - 1, a)
            i -= 2
            b -= 2
        else:
            continue
    return t

def calc_num2():

    t = calc_num1()
    a = 0
    i = -1
    while i < len(t) - 2:
        i += 2
        if c == True:
            while str(t[1]) == "+":
                    a = int(t[0]) + int(t[2])
                    del t[0:3]
                    t.insert(0, a)
            if str(t[1]) == "-":
                    a = int(t[0]) - int(t[2])
                    del t[0:3]
                    t.insert(0, a)
            elif str(t[1]) == "=":
                    break
            break
        elif c == False:
            print("Превышено число попыток. Попробуйте позже.")
            pass

    return a


