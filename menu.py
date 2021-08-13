import logging
import csv
from app import coins

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'p' print coins
- 'e' export to file
- 'q' to exit

Enter your choice: '''

def print_coins():
    logger.info("Printing coins...")
    for coin in coins:
        print(coin)

def export_coins_to_csv():
    logger.info("Exporting coins to file...")
    Details = ['Coin Names']
    rows = []

    with open('Coins.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f, lineterminator = '\n')
        write.writerow(Details)
        for coin in coins:
            write.writerow([coin.coin_name])
            print(coin)




# def print_cheapest_books():
#     logger.info("Find the best book by price...")
#     cheapest_books = sorted(books, key=lambda x: x.price)[:10]
#     for book in cheapest_books:
#         print(book)
#
# books_generator = (x for x in books)
#
# def print_next_book():
#     logger.info("Find the next book from the generator...")
#     print(next(books_generator))

user_choices = {
    'p': print_coins,
    'e': export_coins_to_csv

}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in 'pe':
           user_choices[user_input]()

        else:
            print('***You have not input a valid selection***')
        user_input = input(f'\n\n{USER_CHOICE}')
    logger.debug("Terminating program...")


menu()