from stats import total_words_in_text
from stats import count_letters

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    total_words = total_words_in_text(text)
    letter_counts = count_letters(text)
    print(f"{letter_counts}")


main()
