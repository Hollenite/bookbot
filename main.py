from stats import word_count
from stats import times

def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    print(word_count(book))
    print(times(book))


def get_book_text(path):
    with open(path,encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents


main()