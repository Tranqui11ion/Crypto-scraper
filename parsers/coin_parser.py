import logging

import logging
from locators.coin_locators import CoinLocators

logger = logging.getLogger('scraping.book_parser')



class CoinParser():



    def __init__(self, parent):
        logger.debug(f'New Coin parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'<Coin: {self.coin_name}: {self.price}'

    @property
    def coin_name(self):
        logger.debug('Looking for coin name...')
        locator = CoinLocators.COIN_NAME
        coin_name = self.parent.select_one(locator).string
        logging.debug(f'Coin name found: `{coin_name}`')
        return coin_name
    # @property
    # def link(self):
    #     logger.debug('Looking for link...')
    #     locator = CoinLocators.LINK
    #     link_name = self.parent.select_one(locator).attrs['href']
    #     logging.debug(f'Link address found: `{link_name}`')
    #     return link_name

    # @property
    # def price(self):
    #     logger.debug('Looking for price...')
    #     locator = CoinLocators.PRICE
    #     price = self.parent.select_one(locator).string
    #     float_price = float(price.replace('£', ""))
    #     logging.debug(f'Price found and converted to a float `{float_price}`')
    #     return float_price

    # @property
    # def rating(self):
    #     logger.debug('Looking for rating...')
    #     locator = CoinLocators.RATING
    #     star_rating_tag = self.parent.select_one(locator)
    #     classes = star_rating_tag.attrs['class']
    #     classes = [c for c in classes if c != 'star-rating']
    #     logger.debug(f'Rating found: `{classes[0]}`')
    #     rating = self.RATINGS.get(classes[0])
    #     logger.debug(f'Rating converted to integer: `{rating}`')
    #     return rating


