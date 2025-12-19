import sys
from stats import get_word_count, num_each_char, sorted_char_count, makeSortedList

def get_book_text(book):
    with open(book) as f:
        return f.read()

def print_header(bookPath):    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")

def printSortedCharCount(charCounts):
    for k, v in charCounts.items():
        if k.isalpha():
            print(k + ": " + str(v))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = sys.argv[1]
#    print(get_book_text('books/frankenstein.txt'))
    print_header(bookPath)
    
    print(f"Found {get_word_count(bookPath)} total words")
    
    print("--------- Character Count -------")
    sortedList = makeSortedList(num_each_char(bookPath))
    for item in sortedList:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
 
 #   num_chars= num_each_char('books/frankenstein.txt')
 #   sortedCharCount = sorted_char_count(num_chars)
 #   printSortedCharCount(sortedCharCount)

    print("============= END ===============")

if __name__ == "__main__":
    # This calls the main() function
    main()