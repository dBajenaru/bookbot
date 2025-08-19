import stats
import pdb


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    frankenstein = "books/frankenstein.txt"
    book = get_book_text(frankenstein)
    word_count = stats.count_words(book)
    char_count = stats.count_characters(book)
    print(word_count, "words found in the document")
    print(char_count)


main()
