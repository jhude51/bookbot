def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book_text):
    book_contents = get_book_text(book_text)
    return len(book_contents.split())

def get_char_count(book_text):
    contents = get_book_text(book_text)
    char_count = {}
    text = contents.lower()
    for char in text:
        if char not in char_count:   
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dict(book_text):
    count_dict = get_char_count(book_text)
    sorted_dict = {}
    sorted_list = []
    for char,num in count_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list