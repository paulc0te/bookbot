from stats import *

file_path = "books/frankenstein.txt"

def main():
    print(get_book_text(file_path))
    dict_characters = get_characters(file_path)
    for key, value in dict_characters.items():
        print(f"'{key}': {value}")
main()
