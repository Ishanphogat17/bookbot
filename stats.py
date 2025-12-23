def total_words_in_text(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    
    letter_counts = {}
    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def sort_on(dict_item):
    """Helper function to return the 'num' key for sorting"""
    return dict_item["num"]


def sort_letter_counts(letter_counts):
    """
    Takes a dictionary of characters and their counts.
    Returns a sorted list of dictionaries from greatest to least by count.
    Each dictionary has 'char' and 'num' keys.
    """
    # Convert dictionary to list of dictionaries
    letter_list = []
    for char, count in letter_counts.items():
        letter_list.append({"char": char, "num": count})
    
    # Sort the list from greatest to least using the helper function
    letter_list.sort(reverse=True, key=sort_on)
    
    return letter_list