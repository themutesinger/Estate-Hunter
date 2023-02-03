import json
import asyncio

import aiohttp
from bs4 import BeautifulSoup as bs

from settings.settings import HEADERS, HOUSEKG
from scrapper.common import pack_ad_to_dict


async def parse_page(page):
    soup = bs(page, 'lxml')
    ads = soup.find_all(class_="listing")
    data = []
    for ad in ads:
        title = ad.find(class_='title').text.strip()
        address = ad.find(class_="address").text.strip()
        price = int(ad.find(class_="price").text.lstrip('$').replace(' ', ''))
        description = ad.find(class_="description").text.strip()
        url = HOUSEKG['domen'] + ad.find('a').get('href')
        image = ad.find('img').get('data-src') 
        area = float(ad.find("meta", attrs={"itemprop": 'floorSize'})[
                     'content'].split()[0])
        data.append(pack_ad_to_dict(
            title=title,
            address=address,
            price=price,
            description=description,
            url=url,
            image=image,
            area=area
        ))
    return data


async def fetch_data(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await parse_page(await response.text())


async def scrape_housekg():
    headers = HEADERS
    url = HOUSEKG['url']
    data = []
    tasks = [asyncio.ensure_future(fetch_data(
        f"{url}?page={page}", headers)) for page in range(1, HOUSEKG['page_count'], 1)]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        data = response
    return data


# def scrape_housekg():
#     loop = asyncio.get_event_loop()
#     scraped_data = loop.run_until_complete(scrape())
#     loop.close()
#     return scraped_data
