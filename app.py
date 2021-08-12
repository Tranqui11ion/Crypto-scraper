import asyncio
import aiohttp
import time
import requests
import logging
from pages.coin_page import AllCoinsPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level= logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list.....')


page_content = requests.get('https://coinmarketcap.com/').content
page = AllCoinsPage(page_content)

loop = asyncio.get_event_loop()

coins = page.coins

async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start}')
        return await response.text()

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks



urls = [f'https://coinmarketcap.com/?page={page_num+1}' for page_num in range(1, 2)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total page requests took {time.time() - start}')


for page_content in pages:
    logger.debug('Creating AllBooksPage from page content.')
    coin = AllCoinsPage(page_content)
    coins.extend(page.coins)

