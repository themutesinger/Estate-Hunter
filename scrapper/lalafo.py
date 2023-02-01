import asyncio
import aiohttp

from settings.settings import LALAFO, HEADERS


async def fetch_data(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()


async def scrape():
    headers = HEADERS
    url = LALAFO['url']
    data = []
    tasks = [asyncio.ensure_future(fetch_data(
        f"{url}&page={page}", headers)) for page in range(1, LALAFO['page_count'], 1)]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        data = data + response['items']
    return data


def scrape_lalafo():
    loop = asyncio.get_event_loop()
    scraped_data = loop.run_until_complete(scrape())
    loop.close()
    return scraped_data
