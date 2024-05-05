def main():
    book_path = "books/frankenstine.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} found in file")
    chars_dict = get_chars_dict(text)
    arr_of_dicts = get_dict_arr(chars_dict)

    for item in arr_of_dicts:
        for key, value in item.items():
            print(f"the '{key}' character was found {value} times")
   


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_dict_arr(chars_dict):
    arr = [{key: value} for key, value in chars_dict.items()]
    return arr

main()       