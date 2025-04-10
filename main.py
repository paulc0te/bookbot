from stats import *

def main():

    file_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(get_book_text(file_path))
    print("--------- Character Count -------")
    dict_characters = get_characters(file_path)
    # for key, value in dict_characters.items():
    #     print(f"'{key}': {value}")
    sorted_list_characters = get_sorted_list_characters(dict_characters)
    for dict_characters in sorted_list_characters:
        if dict_characters["character"].isalpha():
            # с этим задание не принимают, но программа работает
            # print(f"{dict_characters["character"]}: {dict_characters["count_char"]}")
            # с этим задание принимают
            print(f'{dict_characters["character"]}: {dict_characters["count_char"]}')

main()
