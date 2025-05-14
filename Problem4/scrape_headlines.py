from scraper_helper import ScraperHelper
from bs4 import BeautifulSoup
import re
from datetime import datetime

def collect_bbc_headlines():
    base_url = "https://www.bbc.com"
    soup = ScraperHelper.fetch_webpage(base_url)

    if not soup:
        print("Failed to retrieve headlines.")
        return

    headlines = []
    elements = soup.find_all(['article', 'div'], class_=re.compile(r'(promo|media|card|block|teaser|headline|story)'))

    for item in elements:
        title_node = item.find(['h1', 'h2', 'h3', 'a'], class_=re.compile(r'(title|heading|headline)'))
        if not title_node:
            title_node = item.find(['h1', 'h2', 'h3', 'a'])

        if not title_node:
            continue

        title = title_node.get_text(strip=True)
        if not title or len(title) < 10:
            continue

        anchor = title_node if title_node.name == 'a' else title_node.find('a')
        href = anchor.get('href') if anchor else None
        if not href:
            alt_link = item.find('a')
            href = alt_link.get('href') if alt_link else None
        if not href:
            continue

        link = ScraperHelper.format_url(base_url, href)

        time_node = item.find(['time', 'span', 'div'], class_=re.compile(r'(date|time|published|timestamp)'))
        date_text = time_node.get_text(strip=True) if time_node else None
        if not date_text and time_node and time_node.has_attr('datetime'):
            date_text = time_node['datetime']

        date = ScraperHelper.parse_date(date_text) if date_text else datetime.now().strftime("%b %d %Y")

        tag_node = item.find(['span', 'div'], class_=re.compile(r'(tag|category|genre|section|topic)'))
        tag = tag_node.get_text(strip=True) if tag_node and tag_node.get_text(strip=True) else "News"

        if not any(h[0] == title or h[1] == link for h in headlines):
            headlines.append((title, link, date, tag))

    if not headlines:
        links = soup.find_all('a')
        for a in links:
            text = a.get_text(strip=True)
            href = a.get('href')
            if not text or not href or len(text) < 15:
                continue
            if text.lower() in {'home', 'news', 'sport', 'weather', 'iplayer', 'sounds', 'bitesize', 'account'}:
                continue
            url = ScraperHelper.format_url(base_url, href)
            headlines.append((text, url, datetime.now().strftime("%b %d %Y"), "News"))

    ScraperHelper.print_headlines(headlines)

if __name__ == "__main__":
    collect_bbc_headlines()
