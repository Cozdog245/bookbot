def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars_count = {}
    text = text.lower()

    for char in text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_char_count(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        chars_list.append({'char':char, "count": count})
    
    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list