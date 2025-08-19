def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    char_count = {}

    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
