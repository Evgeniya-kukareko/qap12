str_1 = "Robin Singh"
str_2 = "I love arrays they are my favorite"
str_to_array_1 = str_1.split(" ")
str_to_array_2 = str_2.split(" ")

arr = ["Ivan", "Ivanou"]
minsk = "Minsk"
belarus = "Belarus"


# print(f"Привет, {arr[0]} {arr[1]}! Добро пожаловать в {minsk} {belarus}")


def list_to_string(array):
    if type(array) != list:
        return "Error"
    else:
        new_str = " "
        return new_str.join(array)


# print(list_to_string(str_to_array_2))

elements_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_modification(lst, el_to_change, el, el_to_delete):
    if type(lst) != list:
        return "Error"
    else:
        lst[el_to_change] = el
        lst.pop(el_to_delete)
        return lst


# print(list_modification(elements_list, 2, 100, 9))

a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
ab = {}


def combine_dicts(dict_1, dict_2, new_dict):
    if type(dict_1) != dict or type(dict_2) != dict:
        return "Error"
    else:
        all_keys = set(dict_1.keys()) | set(dict_2.keys())
        for key in all_keys:
            new_dict[key] = [dict_1.get(key, None), dict_2.get(key, None)]
        return new_dict


# print(combine_dicts(a, b, ab))

list_of_numbers = [1, 5, 2, 9, 2, 9, 1]


def check_if_unique(lst):
    unique_number = set(lst)
    for num in unique_number:
        if list_of_numbers.count(num) == 1:
            print(num)


# check_if_unique(list_of_numbers)


def letter_counter(s):
    lower_s = s.lower()

    count = {}

    for el in lower_s:
        if not el.isalpha():
            continue
        if el in count:
            count[el] += 1
        else:
            count[el] = 1

    max_count = 0

    for i in count.values():
        if i > max_count:
            max_count = i

    max_letters = []

    for letter, el in count.items():
        if el == max_count:
            max_letters.append(letter)

    max_letters.sort()

    return max_letters[0]
