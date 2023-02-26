# Task 1

a = -1.6
b = 2.99


def number_converter(number):
    return int(number)


# print(number_converter(a))
# print(number_converter(b))

# Task 2

initial_string = 'www.my_site.com#about'


def symbol_replacer(string):
    return string.replace('#', '/')


# print(symbol_replacer(initial_string))

# Task 3

original_string = 'stroka'


def add_ing(string):
    return string + 'ing'


# print(add_ing(original_string))

# Task 4

original_name = 'Ivanou Ivan'


def replace_name(name):
    return name.split()[1] + " " + name.split()[0]


# print(replace_name(original_name))


# Task 5

def remove_spaces(input_string):
    return input_string.strip()


# print(remove_spaces('  A string with spaces.   '))

# Task 6

school = {"1a": 20,
          "2б": 23,
          "3в": 25,
          "4г": 30,
          "5а": 21,
          "6б": 32,
          "7в": 24,
          "8г": 31,
          "9а": 23,
          "10б": 27}


def add_class(name, class_with_letter, students):
    name[class_with_letter] = students


add_class(school, "11б", 29)
# print(school)

# Task 7

test_list = ["First element", "Second element"]
# print(test_list[1])

# Task 8

employment = "employment"
employ = "employ"


def check_if_included(first, second):
    return first in second


# print(check_if_included(employ, employment))

# Task 9

x = "My name is Agent Smith"
# print(x[1])
# print(x[3:16:3])

# Task 10

list_of_numbers = [1, 5, 2, 9, 2, 9, 1]


def check_if_unique(lst):
    unique_number = set(lst)
    for num in unique_number:
        if list_of_numbers.count(num) == 1:
            print(num)

# check_if_unique(list_of_numbers)
