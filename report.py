from stats import letter_counter, word_counter 

def book_report_header(book_path):
    
    book_report_header = "============ BOOKBOT ============"
    book_string = "Analyzing book found at {book_path}..."
    book_report_header_string = f"{book_report_header}\n{book_string}\n"

    return book_report_header_string


def book_report_word_count(book_path):

    word_count_header = "----------- Word Count ----------"
    word_count = word_counter(book_path)
    word_count_string = f"{word_count_header}\n{word_count}\n"
    
    return word_count_string
    
def book_report_letter_counts(book_path):
    
    letter_counts_header = "--------- Character Count -------"
    letter_count = "\n".join(f"'{k}': {v}" for k, v in letter_counter(book_path).items())
    letter_counter_string = f"{letter_counts_header}\n{letter_count}\n"

    return letter_counter_string

def book_report_complete(book_path):

    br_header = book_report_header(book_path)
    br_word_count = book_report_word_count(book_path)
    br_letter_count = book_report_letter_counts(book_path)
    br_footer = "============= END ==============="

    br_full_report = f"{br_header}{br_word_count}{br_letter_count}{br_footer}"
    # br_full_report = f"{br_header}\n{br_footer}"

    return br_full_report
