from stats import (
    get_book_text,
    get_characters,
    get_sorted_list_characters
)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(get_book_text(file_path))
    print("--------- Character Count -------")
    dict_characters = get_characters(file_path)
    sorted_list_characters = get_sorted_list_characters(dict_characters)
    for dict_characters in sorted_list_characters:
        if dict_characters["character"].isalpha():
            print(f'{dict_characters["character"]}: {dict_characters["count_char"]}')
    print("============= END ===============")

main()
