def words_to_digits(phone_words):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    phone_words = phone_words.split()
    phone_digits = []

    i = 0
    while i < len(phone_words):
        word = phone_words[i]
        repeat_count = 1

        if word == 'double' or word == 'triple':
            repeat_count = 2 if word == 'double' else 3
            i += 1

        phone_digits.append(word_to_digit.get(phone_words[i], '') * repeat_count)

        i += 1

    return ''.join(phone_digits)

# Take input from the user
phone_words_input = input("Enter the phone number in words: ").lower()
phone_digits_output = words_to_digits(phone_words_input)

print(f"The phone number in digits is: {phone_digits_output}")
