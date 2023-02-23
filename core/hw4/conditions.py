def add_one(number):
    if type(number) == int and number > 0:
        return number + 1
    else:
        return "Error"


def positive_numbers_counter(*args):
    counter = 0
    for i in args:
        if i > 0:
            counter += 1
    return counter


def days_in_year(year):
    if year % 4 == 0:
        if year % 400 != 0:
            return 365
        return 366
    else:
        return 365


def day_of_the_week(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Error"


def weight_converter(index, weight):
    if index == 1:
        return weight
    elif index == 2:
        return weight / 1000000
    elif index == 3:
        return weight / 1000
    elif index == 4:
        return weight * 1000
    elif index == 5:
        return weight * 100
    else:
        return "Error"
