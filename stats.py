def get_book_text(book_path):
    
    with open(book_path) as book:

        book_contents = book.read()

    return book_contents


def split_book_to_words(book_path):

    book_contents = get_book_text(book_path)
    words = book_contents.split()
    word_count = len(words)

    return word_count
