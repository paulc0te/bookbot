def get_book_text(file_path):
    """
    Get number of words
    """
    with open(file_path) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    return f"Found {num_words} total words"

def get_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read().replace('\n', '')  # del \n
    dict_characters = {}
    for character in file_contents:
        if character.lower() not in dict_characters:
            dict_characters[character.lower()] = 1
        else:
            dict_characters[character.lower()] += 1
    return dict_characters

def get_sorted_list_characters(dict_characters):
    sorted_list_characters = []
    for key, value in dict_characters.items():
        sorted_list_characters.append({"character": key, "count_char": value})
    result = sorted(sorted_list_characters, reverse=True, key=lambda dict_characters: dict_characters["count_char"])    # get key of sort
    return result
