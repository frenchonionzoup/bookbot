from stats import get_num_words, get_char_stats, sort_dict 

def main():
    print("============ BOOKBOT =============")
    
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}")
    
    text = get_book_text(book_path)
    #print(text)
    
    num_words = get_num_words(text)
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    
    print("------- Character Count -------")
    char_stats = get_char_stats(text) 
    #print(char_stats)
    sorted_stats = sort_dict(char_stats)
    def print_sorted_stats(stats):
        for stat in stats:
            print(f"{stat["char"]}: {stat["num"]}")
    print(print_sorted_stats(sorted_stats))

    print("================= End =================")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents



main()
