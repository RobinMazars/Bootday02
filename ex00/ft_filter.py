def ft_filter(fc, list):
    for x in list:
        if fc is None or fc(x):
            yield x


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_A_student(score):
    return score > 75


# over_75 = list(filter(is_A_student, scores))
# print(over_75)
#
# over_752 = list(ft_filter(is_A_student, scores))
# print(over_752)
