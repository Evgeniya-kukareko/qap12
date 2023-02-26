def count_summ(num_1, num_2):
    if num_1 > num_2:
        return "Error"
    elif type(num_1) == float or type(num_2) == float:
        return "Error"
    else:
        result = 0
        for i in range(num_1, num_2):
            result += 1
        return result


def multiplication(*args):
    result = 1
    negative = 0
    for i in args:
        if i > 0:
            result *= i
        else:
            negative += 1
    return result, negative


swimmers = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}


# best_score = max(swimmers.values())
# print(best_score)


def best_score(**kwargs):
    score = None
    for i in kwargs.values():
        if score is None or i > score:
            score = i
    return score
