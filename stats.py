def get_book_text(book_path):
    
    with open(book_path) as book:

        book_contents = book.read()

    return book_contents


def letter_counter(book_path):
    book_contents = get_book_text(book_path)

    letter_counter_register = {}

    for char in book_contents.lower():
        if char.isalpha():
            if char in letter_counter_register:
                letter_counter_register[char] += 1
            else:
                letter_counter_register[char] =1

    return letter_counter_register
    

def split_book_to_words(book_path):

    book_contents = get_book_text(book_path)
    words = book_contents.split()
    word_count = len(words)

    return word_count
