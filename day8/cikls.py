a = input()
i = 0
data = a.replace(" ", "")

def poli():
    result = bool
    i = 0
    while i <= len(data) / 2:
        if data[- i - 1] == data[i]:
            result = True
            i += 1
        else:
            result = False
    return result
print(poli())

