import random

ver = {}
for i in range(1, 1000):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c, d, e, f, g, h, u, v, w, z, y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if a + b == 2:
        c += 1
        ver[2] = c / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 3:
        d += 1
        ver[3] = d / i
    elif a + b == 4:
        e += 1
        ver[4] = e / i
    elif a + b == 5:
        f += 1
        ver[5] = f / i
    elif a + b == 6:
        g += 1
        ver[6] = g / i
    elif a + b == 7:
        h += 1
        ver[7] = h / i
    elif a + b == 8:
        u += 1
        ver[8] = u / i
    elif a + b == 9:
        v += 1
        ver[9] = v / i
    elif a + b == 10:
        w += 1
        ver[10] = w / i
    elif a + b == 11:
        z += 1
        ver[11] = z / i
    elif a + b == 12:
        y += 1
        ver[12] = y / i

print(c, d, e, f, g, h, u, v, w, z, y)