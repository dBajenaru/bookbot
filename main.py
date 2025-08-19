from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    frankenstein = "books/frankenstein.txt"
    book = get_book_text(frankenstein)
    word_count = count_words(book)
    print(word_count, "words found in the document")


main()
