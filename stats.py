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


def sort_characters(dict):
    # step 1: splits a dictionary into a list of dicts
    split_dict = []
    for key, value in dict.items():
        split_dict.append({"char": key, "count": value})

    # step 2: sort the list of dicts
    split_dict.sort(reverse=True, key=sort_on)

    return split_dict
