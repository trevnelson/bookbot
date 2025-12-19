def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def get_word_count(book):
    text = get_book_text(book)
    words = text.split()
    return len(words)

def num_each_char(book):
    text = get_book_text(book)
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sorted_char_count(char_count):
    return dict(sorted(char_count.items(), key = lambda item: item[1], reverse=True))

def sort_on(items):
    return items["num"]

def makeSortedList(char_counts):
    list = []
    for k in char_counts:
        list.append({"char": k, "num": char_counts[k]})
        list.sort(reverse=True, key=sort_on)
    return list
        


