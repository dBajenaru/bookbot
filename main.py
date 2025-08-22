import stats
import pdb


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    frankenstein = "books/frankenstein.txt"
    text = get_book_text(frankenstein)
    word_count = stats.count_words(text)
    char_count = stats.count_characters(text) # this is char dict

    breakpoint()
    sorted_chars = stats.sort_characters(char_count)
#    print(char_count)
    print(sorted_chars)

    """
    split_dict = stats.split_dictionary(char_count)
    print(split_dict)
    split_dict.sort(reverse=True, key=stats.sort_on)
    print(split_dict)
    """

#    sort_chars = stats.sort_characters(char_count)
    print(word_count, "words found in the document")
#    print(char_count)
#    print(sort_chars)


main()
