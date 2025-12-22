def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    print(text)


main()
