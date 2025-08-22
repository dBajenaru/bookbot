import stats
import sys
import pdb


def get_text(filepath):
    with open(filepath) as f:
        return f.read()


def pretty_print(text, wc, chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", text)
    print("----------- Word Count ----------")
    print("Found", wc, "total words")
    print("--------- Character Count -------")

    for x in chars:
        if x["char"].isalpha():
            print(x["char"] + ":", x["count"])

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text_fp = sys.argv[1]
    text = get_text(text_fp)

    word_count = stats.count_words(text)
    char_count = stats.count_characters(text)
    sorted_chars = stats.sort_characters(char_count)

    pretty_print(text_fp, word_count, sorted_chars)


main()
