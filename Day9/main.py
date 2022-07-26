a = [2, 4, 6, 3, 1]
b = int(min(a))
c = int(max(a))
i = 0
while i < len(a):
    if a[i] == min(a):
        a_min = i
        i += 1
    elif a[i] == max(a):
        a_max = i
        i += 1
    else:
        i += 1
a[a_min] = c
a[a_max] = b

print(a)

