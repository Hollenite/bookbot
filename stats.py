def get_book_text(path):
    with open(path,encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

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

def convert(dic):
    val_list = []
    for key, value in dic.items():
        if key.isalpha():
            x = {"char": key, "num": value}
            val_list.append(x)
    return val_list

def sort_on(lis):
    return lis["num"]

def printdata(path):
    path = path
    book = get_book_text(path)
    #this is now the entire dictionary in key,value pairs
    occurence = times(book)
    #this is now the unsorted list of each line of dictionary as a dictionary
    list_val = convert(occurence)
    #this is now the sorted list of dictionaries
    list_val.sort(key=sort_on, reverse=True)
    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {path}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count(book)} total words\n"
        "--------- Character Count -------\n"
    )
    for x in list_val:
        print(f"{x['char']}: {x['num']}")
    print(
        "============= END ==============="
    )

