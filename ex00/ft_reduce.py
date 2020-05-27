from functools import reduce


def ft_reduce(fc, list):
    if len(list) > 0:
        result = list[0]
        for x in list[1:]:
            result = fc(result, x)
        return result
    else:
        raise TypeError("reduce() of empty sequence with no initial value")


numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(toto, titi):
    return toto + titi


result = reduce(custom_sum, numbers)
result2 = ft_reduce((custom_sum), ())
print(result)
print(result2)
