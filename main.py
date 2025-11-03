from stats import split_book_to_words, letter_counter


def main():
    book = "./books/frankenstein.txt" 

    num_words = split_book_to_words(book)
    letter_stats = letter_counter(book)
    letter_stats.sort()

    print(f"Found {num_words} total words")
    
    for k, v in letter_stats.items():
        print(f"'{k}': {v}")

main()
