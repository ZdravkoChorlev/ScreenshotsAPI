import asyncio
from pyppeteer import launch
from urllib.parse import urljoin, urlparse
import shutil
import os

async def screenshot_scrapred_pages(start_url: str, num_of_links: int,  dir_name: str, output_dir: str = 'screenshots'):
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()

    visited_urls = set()
    to_visit_urls = [start_url]
    full_path = os.path.join(output_dir, dir_name)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    while to_visit_urls and len(visited_urls) < num_of_links:
        current_url = to_visit_urls.pop(0)
        
        if current_url in visited_urls:
            continue

        try:
            await page.goto(current_url, {'waitUntil': 'networkidle2'})
        except Exception as e:
            print(f"Failed to load {current_url}: {e}")
            continue

        parsed_url = urlparse(current_url)
        screenshot_path = os.path.join(full_path, f"{parsed_url.netloc}_{len(visited_urls)}.png")

        await page.screenshot({'path': screenshot_path})
        visited_urls.add(current_url)

        links = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('a'))
                        .map(a => a.href)
                        .filter(href => href.startsWith('http'));
        }''')

        for link in links:
            absolute_link = urljoin(current_url, link)
            if absolute_link not in visited_urls and absolute_link not in to_visit_urls:
                to_visit_urls.append(absolute_link)

    await browser.close()

def create_zip(zip_name: str, zip_path: str):
    shutil.make_archive(zip_name, 'zip', zip_path)
