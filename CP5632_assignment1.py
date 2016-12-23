__author__ = "jc451634"

# Initialize the constants
book_file = 'books.csv'

def main():
    print("Reading List 1.0 - by Shreyas Bharadwaj N R")
    book_list = []
    load_books(book_list)
    display_menu()
    choice = input('>>>').upper()

    while choice != 'Q':
        if choice == 'R':
            list_required_books(book_list)
        elif choice == 'C':
            list_completed_books(book_list)
        elif choice == 'A':
            list_all_new_books(book_list)
        elif choice == 'M':
            list_mark_book_completed(book_list)
        else:
            print('Please enter R,C,A,M or Q(quit)')
        choice = input('>>>').upper()
    print('Have a nice day:')
   # end of main()


def display_menu():
    print('Menu')
    print('R - List required books')
    print('C - List completed books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')

def list_required_books(book_list):
    print("required books")

def list_completed_books(book_list):
    print("completed books")

def list_all_new_books(book_list):
    print("you can print even your name li;ke SHYREYAS YOU DIE ")

def list_mark_book_completed(book_list):
    print("this is not a ")



def load_books(book_list):
	"""

	"""
print("load books")

# end of load_books()



def complete_a_book():
	"""

	"""
print("complete a book")

    # end of complete_a_book()

    # Start the program
main()