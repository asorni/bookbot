import sys
from stats import count_words, count_characters, to_sorted_list

def get_book_text(filepath):
    content = ""
    with open(filepath) as f:
        content = f.read()
    return content

def print_report(book_path, num_words, sorted_char_stats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_stats:
        if(item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text= get_book_text(book_path)
    num_words = count_words(text)
    char_stats = count_characters(text)
    sorted_char_stats = to_sorted_list(char_stats)

    print_report(book_path, num_words, sorted_char_stats)

main()
