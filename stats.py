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