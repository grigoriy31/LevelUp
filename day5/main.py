a = [int(x) for x in input().split()]
a_tuple = tuple(a)
for i in a_tuple:
    if a_tuple.count(i) == 1:
        print(i)

