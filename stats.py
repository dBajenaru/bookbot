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



# sort() key method
def sort_on(items):
    return items["count"]


def split_dictionary(dict):
    split_dict = []
    for key, value in dict.items():
        split_dict.append({"char": key, "count": value})

    return split_dict


def sort_characters(dict):
    split_dict = split_dictionary(dict)
    print(split_dict)
    sorted = split_dict.sort(reverse=True, key=sort_on)

    return sorted
