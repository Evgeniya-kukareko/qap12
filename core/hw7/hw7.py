greeting_name = lambda name: print(f"Hello, {name}")

greeting_names = lambda names_in_lam: [f"Hello, {name}" for name in names_in_lam]

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def positive_numbers(numbers):
    for num in numbers:
        try:
            if num > 0:
                yield num
        except TypeError:
            pass


def count_letters_in_str(str):
    words = str.split()
    try:
        word_lengths = [len(word) for word in words if word != "the"]
    except TypeError:
        return "Invalid input"
    else:
        return word_lengths


def caesar_cipher_encoder(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def caesar_cipher_decoder(ciphertext, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    for letter in ciphertext:
        if letter in alphabet:
            index = alphabet.find(letter)
            shifted_index = index - shift
            plaintext += alphabet[shifted_index]
        else:
            plaintext += letter
    return plaintext
