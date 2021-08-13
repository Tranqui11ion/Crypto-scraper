import logging
from bs4 import BeautifulSoup

from locators.coin_page_locators import CoinPageLocators
from parsers.coin_parser import CoinParser

logger = logging.getLogger('scraping.all_coins_page')

class AllCoinsPage():
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def coins(self):
        logger.debug(f'Finding all coins from current page using `{CoinPageLocators.COIN}')
        return [CoinParser(e) for e in self.soup.select(CoinPageLocators.COIN)]

    # Will statically set
    #---------------------
    # @property
    # def page_count(self):
    #     logger.debug('Finding total amount of pages to scrape')
    #     content = self.soup.select_one(CoinPageLocators.PAGER).string
    #     logger.info(f'Found number of catalogue pages available: `{content}`.')
    #     pattern = 'Page [0-9]+ of ([0-9]+)'
    #     matcher = re.search(pattern, content)
    #     pages = int(matcher.group(1))
    #     logger.debug(f'Extracted number of pages as integer: {pages}')
    #     return pages

