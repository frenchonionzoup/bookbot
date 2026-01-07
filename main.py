import sys
from stats import (
    get_num_words, 
    get_char_stats, 
    sort_dict,
)

def main():
    if len(sys.argv) == 2:
        print("bookot starting...")
    else:
        print("Don't be stupit! :")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = f"{sys.argv[1]}"
    #bookpath = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_stats = get_char_stats(text)
    sorted_stats = sort_dict(char_stats)
    print_report(book_path, num_words, sorted_stats)





def print_sorted_stats(stats):
    for stat in stats:
        if not stat["char"].isalpha():
            continue
        print(f"{stat["char"]}: {stat["num"]}")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(path, num_words, sorted_stats):
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    print(print_sorted_stats(sorted_stats))
    print("================= End =================")
    
main()
