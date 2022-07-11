import matplotlib.pyplot as plt
date =[]
date = input("Введите данные: ").split()
a = int(date[0])
b = int(date[1])
c = int(date[2])
l = list(range(-10, 11))
y_coords = []
x = []
g = []
def koord():
    i = 0
    while i <=21:
        if i < 21:
            y = a * int(l[i]) ** 2 + b * int(l[i]) + c
            g.append(y)
            i += 1
        else:
            break

    return g
y_coords = koord()
x_coords = l
print(y_coords)
print(x_coords)

plt.plot(x_coords, y_coords )
plt.show()