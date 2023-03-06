def display_elements(filename):
    with open(filename, 'r') as f:
        content = f.read().split()
        if len(content) < 3:
            raise ValueError("File must have at least 3 integers")
        first = int(content[0])
        second = int(content[1])
        penultimate = int(content[-2])
        last = int(content[-1])
        return first, second, penultimate, last


# print(display_elements("first.txt"))


def sort_file(filename):
    with open(filename, 'r') as f:
        numbers = f.read().split()
        print(numbers)

    even_numbers = []
    odd_numbers = []

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            even_numbers.append(num)
        elif num % 2 != 0:
            odd_numbers.append(num)
        else:
            print(num)

    if even_numbers:
        with open('even_numbers.txt', 'w') as f:
            f.write('\n'.join(str(num) for num in even_numbers))

    if odd_numbers:
        with open('odd_numbers.txt', 'w') as f:
            f.write('\n'.join(str(num) for num in odd_numbers))


# sort_file("first.txt")

def data_squaring(filename):
    with open(filename, 'r+') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            squares = [n ** 2 for n in numbers]
            file.seek(0)
            file.write(' '.join(map(str, squares)) + '\n')
            file.truncate()


# data_squaring("to_replace.txt")

def swap_binary_files(file1_path, file2_path):
    # read the contents of the first file
    with open(file1_path, 'rb') as file1:
        file1_content = file1.read()

    # read the contents of the second file
    with open(file2_path, 'rb') as file2:
        file2_content = file2.read()

    # swap the contents
    with open(file1_path, 'wb') as file1:
        file1.write(file2_content)

    with open(file2_path, 'wb') as file2:
        file2.write(file1_content)


# swap_binary_files("file1.bin", "file2.bin")
