def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    frankenstein = "books/frankenstein.txt"
    book = get_book_text(frankenstein)
    print(book)

main()
