from stats import split_book_to_words


def main():
    
    num_words = split_book_to_words("./books/frankenstein.txt")

    print(f"Found {num_words} total words")

main()
