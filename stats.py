def get_book_text(file_path):
    """
    Get number of words
    """
    with open(file_path) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    return f"{num_words} words found in the document"

def get_characters(file_path):
    """
    Get number of characters
    """
    with open(file_path) as f:
        file_contents = f.read().replace('\n', '')  # del \n
    dict_characters = {}
    for character in file_contents:
        if character.lower() not in dict_characters:
            dict_characters[character.lower()] = 1
        else:
            dict_characters[character.lower()] += 1
    return dict_characters
