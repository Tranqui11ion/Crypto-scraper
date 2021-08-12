import logging
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at cheapest books
- 'n' to just get next available book on the page
- 'q' to exit

Enter your choice: '''

def print_5_star_books():
    logger.info("Find the best book by rating...")
    best_books = [book for book in books if book.rating == 5]
    for book in best_books:
        print(book)

def print_cheapest_books():
    logger.info("Find the best book by price...")
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def print_next_book():
    logger.info("Find the next book from the generator...")
    print(next(books_generator))

user_choices = {
    'b': print_5_star_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in 'bcn':
           user_choices[user_input]()

        else:
            print('***You have not input a valid selection***')
        user_input = input(f'\n\n{USER_CHOICE}')
    logger.debug("Terminating program...")


menu()