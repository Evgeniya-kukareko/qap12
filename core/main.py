from core.hw3 import *
from core.hw4 import *
from core.hw7 import *
from core.hw8 import *

print(number_converter(-5.6))
print(symbol_replacer('www.my_site.com#about'))
print(add_ing('stroka'))
print(replace_name('Ivanou Ivan'))
print(remove_spaces('  A string with spaces.   '))
print(check_if_included("employ", "employment"))
check_if_unique([1, 5, 2, 9, 2, 9, 1])

print(print_str_data("Christopher"))
print(print_second_str("communication"))
print(change_second_name("my name is name", "Jane"))
print(check_str("Hello world!"))

print(print_second_element(["Taylor", "12345", "Brown", "Miller"]))
print(change_last_element(["56789", "Wilson", "Roberts"]))
print(add_element_to_list(["56789", "Wilson", "Roberts"], "123", "New"))

print(list_to_string(["I", "love", "arrays", "they", "are", "my", "favorite"]))
print(list_modification([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 100, 9))
print(combine_dicts({"a": 1, "b": 2, "c": 3}, {"c": 3, "d": 4, "e": 5}, {}))
print(letter_counter("a" * 9000 + "b" * 1000))

print(add_one(10))
print(positive_numbers_counter(1, 3, -2))
print(days_in_year(1300))
print(day_of_the_week(7))
print(weight_converter(4, 56))

print(count_summ(1, 13))
print(multiplication(2, -3, 2, 5, 6, -1, 34, 5))
swimmers = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}
print(best_score(**swimmers))


print(mult_sum(4))
print(count_s(105, 500878))
print(sum_and_digits(503))
print(age_counter(50,3))

greeting_name("Jane")
print(greeting_names(["Helen", "Sharon", "Laura", "David"]))

positive_result = positive_numbers(numbers)

for number in positive_result:
   print(number)

print(count_letters_in_str("the quick brown fox jumps over the lazy dog"))
print(caesar_cipher_encoder("This is a test string", 2))
print(caesar_cipher_decoder("Ymnx nx f yjxy xywnsl", 5))

print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols("a", "b"))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))

print(lexicographic_asc(1, 2, 3))

