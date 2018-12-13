import asyncio

from pyppeteer import launch
from urllib.parse import urlparse, parse_qs


class PageBuilder:
    def __init__(self, base_url):
        (self.base_url, self.domain, self.site_id) = self._parse_url(base_url)
        self.pages = []

    @staticmethod
    def _parse_url(base_url):
        parse = urlparse(base_url)
        queries = parse_qs(parse.query)
        site_id = None
        if 'siteid' in queries:
            site_id = queries['siteid'][0]
            if site_id.isdigit():
                site_id = int(site_id)

        return parse.scheme + "://" + parse.netloc, parse.netloc, site_id

    async def _home_page(self):
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.setViewport({'width': 1366, 'height': 768})
        # await page.goto('https://www.google.com')
        await page.goto('https://www.expedia.com', timeout=0, waituntil='networkidle0')
        # page_source = await page.content()

        flight_nav_element = await page.xpath('//*[@id="primary-header-flight"]')
        bounding_box = await flight_nav_element[0].boundingBox()
        print(bounding_box)
        # write_html(page_source, 'google_homepage.html')
        await browser.close()

    def build_pages(self, lobs):
        asyncio.get_event_loop().run_until_complete(asyncio.ensure_future(self._home_page()))
