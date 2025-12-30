def word_count(book):
    x  = len(book.split())
    return f"Found {x} total words"

def times(book):
    count = {}
    for char in book:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count
