def add_one(number):
    if type(number) == int and number > 0:
        return number + 1
    else:
        return "Error"


# print(add_one(1.3))

def positive_numbers_counter(*args):
    counter = 0
    for i in args:
        if i > 0:
            counter += 1
    return counter


# print(positive_numbers_counter(1, 3, -2))

def days_in_year(year):
    if year % 4 == 0:
        if year % 400 != 0:
            return 365
        return 366
    else:
        return 365


# print(days_in_year(1300))

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

# print(day_of_the_week(7))
