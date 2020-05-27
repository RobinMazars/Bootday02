def ft_map(fc, list):
    for x in list:
        yield (fc(x))


li = [1, 2, 3, 4, 5]


def x2(n):
    return n*2


# fin2 = map(None, li)
# print(fin2)
# print(list(fin2))
# fin = ft_map(None, li)
# print(fin)
# print(list(fin))
