from stats import total_words_in_text
from stats import count_letters
from stats import sort_letter_counts
import sys 

 

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2: 
        sys.exit(1)
    else:    
        path_to_file = sys.argv[1]
        text = get_book_text(path_to_file)
        total_words = total_words_in_text(text)
        letter_counts = count_letters(text)
        sorted_letters = sort_letter_counts(letter_counts)
    
    print(f"Found {total_words} total words")
    print("\nLetter counts (sorted from most to least frequent):")
    for letter_dict in sorted_letters:
        print(f"{letter_dict['char']}: {letter_dict['num']}")


main()
