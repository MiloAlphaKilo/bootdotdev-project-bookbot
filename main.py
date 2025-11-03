from report import book_report_complete  


def main():
    
    book = "./books/frankenstein.txt" 
    report = book_report_complete(book)
    
    print(f"{report}")


main()
