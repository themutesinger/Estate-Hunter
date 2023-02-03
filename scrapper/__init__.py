import asyncio

from scrapper.lalafo import scrape_lalafo
from scrapper.housekg import scrape_housekg
from settings.settings import LALAFO, HOUSEKG


def get_data():
    fuctions = []
    if LALAFO['run']:
        fuctions.append(scrape_lalafo)
    if HOUSEKG['run']:
        fuctions.append(scrape_housekg)

    loop = asyncio.get_event_loop()
    scraped_data = []

    for func in fuctions:
        scraped_data += loop.run_until_complete(func())
    loop.close()
    return scraped_data
