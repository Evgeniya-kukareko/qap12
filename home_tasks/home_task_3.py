# Task 1

a = int(-1.6)
b = int(2.99)

print(a, b)

# Task 2

initial_string = 'www.my_site.com#about'
replaced_string = initial_string.replace('#', '/')

print("Replaced string:", replaced_string)

# Task 3

original_string = 'stroka'
new_string = original_string + 'ing'

print("New string:", new_string)

# Task 4

original_name = 'Ivanou Ivan'
changed_name = original_name.split()[1] + " " + original_name.split()[0]
print("New name:", changed_name)


# Task 5

def remove_spaces(input_string):
    return input_string.strip()


print(remove_spaces('  A string with spaces.   '))

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
print(school)

# Task 7

test_list = ["First element", "Second element"]
print(test_list[1])

# Task 8

employment = "employment"
employ = "employ"

if employ in employment:
    print(f"'{employ}' is included in '{employment}'")
else:
    print(f"'{employ}' is not included in '{employment}'")

# Task 9

x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])

# Task 10

list_of_numbers = [1, 5, 2, 9, 2, 9, 1]
unique_number = set(list_of_numbers)
for num in unique_number:
    if list_of_numbers.count(num) == 1:
        print(num)
