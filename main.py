from stats import get_word_count, get_book_text, get_char_count, sort_char_count
import sys
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')

    word_count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count = get_char_count(text)
    sorted_chars = sort_char_count(char_count)
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict['char']
        count = char_dict['count']
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")
    
main()
