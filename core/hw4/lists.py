first_list = ["Taylor", "12345", "Brown", "Miller"]
second_list = ["56789", "Wilson", "Roberts"]


def print_second_element(lst):
    return lst[1]


def change_last_element(lst):
    lst[-1] = "changed element"
    return lst


joined_lists = first_list + second_list
# print(joined_lists)

sliced_list = joined_lists[::2]


# print(sliced_list)


def add_element_to_list(lst, *args):
    lst += args
    return lst


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def intersection_list(lst_1, lst_2):
    new_list = list(set(lst_1).intersection(set(lst_2)))
    return new_list


last_list = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
# print(set(last_list))
