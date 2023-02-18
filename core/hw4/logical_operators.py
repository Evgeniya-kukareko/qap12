a = 5
b = 10

print(((a > 3) and (b < 15) and (8 == 8) and (not False)))
print(((2 + 2 == a) and (len('python') == 6) and (not (7 < 3))))
print(((4 >= 4) and (5 != 6) and (2 ** 3 == 8) and (b in [1, 2, 5, 10])))
print(((a + b) and (len([1, 2, 3]) > b) and ('hello'.isnumeric() == False)))

print(((a < 3) or (b > 15) or (8 == 9) or True))
print(((2 + 2 == a) or (len('python') == 6) or (not (7 < 3))))
print(((a == 4) or (5 == 6) or (2 ** 3 == 10) or (b in [1, 2, 5])))
print(((a == b) and (len([1, 2, 3]) > b) and ('hello'.isnumeric() == False)))

print(("Hello" > "world") and ("world" > "Hello"))
