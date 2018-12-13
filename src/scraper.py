import asyncio

from pyppeteer import launch
from src.utils import write_html


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://www.expedia.com')
    page_source = await page.content()

    flight_nav_element = await page.xpath('//*[@id="primary-header-flight"]')
    print(flight_nav_element.)
    # write_html(page_source, 'google_homepage.html')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())