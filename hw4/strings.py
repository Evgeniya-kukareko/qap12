str_to_check = "Christopher"


def print_str_data(string):
    if type(string) != str:
        return "Error"
    else:
        first_symbol = string[0]
        last_symbol = string[-1]
        third_symbol = string[2]
        third_from_the_end_symbol = string[-3]
        length = len(string)
        length_str = str(length)

        result = first_symbol + ", " + last_symbol + ", " + third_symbol + ", " + third_from_the_end_symbol + ". Length = " + length_str

        return result


print(print_str_data(str_to_check))

second_str = "communication"


def print_second_str(string):
    if type(string) != str:
        return "Error"
    else:
        first_8_symbols = string[:8]
        str_middle = len(string) // 2
        four_symbols = string[str_middle - 2:str_middle + 2]
        multiple_of_3 = ""
        str_reverse = string[::-1]
        for i in range(0, len(string), 3):
            multiple_of_3 += string[i]

        result = first_8_symbols + ", " + four_symbols + ", " + multiple_of_3 + ", " + str_reverse
        return result


print(print_second_str(second_str))

third_str = "my name is name"


def change_second_name(string, name):
    if type(string) != str:
        return "Error"
    if type(name) != str:
        return "Error"
    else:
        changed_str = string.replace("name", name)
        final_str = changed_str.replace(name, "name", 1)
        return final_str


print(change_second_name(third_str, "Jane"))

test_str = "Hello world!"
