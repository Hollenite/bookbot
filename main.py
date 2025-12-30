def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    print(word_count(book))


def get_book_text(path):
    with open(path,encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    x  = len(book.split())
    return f"Found {x} total words"

main()