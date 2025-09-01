import sys
from stats import get_word_count, get_char_count, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        num_words = get_word_count(file_path)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        char_count = sort_dict(file_path)
        for char in char_count:
            if char['char'].isalpha():
                print(f"{char['char']}: {char['num']}")
        print(f"============ END =============")
        
main()