import sys

from report import book_report_complete  

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        report = book_report_complete(book)
        print(f"{report}")


main()
