import asyncio

from src.page import PageBuilder


# def _build_pages():
page_builder = PageBuilder('https://www.expedia.com')
page_builder.build_pages(['hotel', 'package', 'flight'])
