import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

class ScraperHelper:
    @staticmethod
    def fetch_webpage(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Page loaded successfully: {url}")
                return BeautifulSoup(response.text, "html.parser")
            else:
                print(f"Unable to load page, status code: {response.status_code}")
        except requests.RequestException as err:
            print(f"Request error: {err}")
        return None

    @staticmethod
    def format_url(base, path):
        if not path:
            return None
        if path.startswith(('http://', 'https://')):
            return path
        if path.startswith('//'):
            return 'https:' + path
        if path.startswith('/'):
            match = re.match(r"(https?://[^/]+)", base)
            if match:
                return match.group(1) + path
        if not base.endswith('/'):
            base = base[:base.rfind('/') + 1]
        if path.startswith('./'):
            path = path[2:]
        return base + path

    @staticmethod
    def parse_date(text):
        if not text:
            return datetime.now().strftime("%b %d %Y")

        now = datetime.now()
        content = text.strip().lower()

        if content in {"now", "today"}:
            return now.strftime("%b %d %Y")
        if content == "yesterday":
            return (now - timedelta(days=1)).strftime("%b %d %Y")

        if "ago" in content:
            match = re.search(r"(\d+)\s+(\w+)\s+ago", content)
            if match:
                value = int(match.group(1))
                unit = match.group(2).lower()

                if "min" in unit:
                    past = now - timedelta(minutes=value)
                elif "hour" in unit or "hr" in unit:
                    past = now - timedelta(hours=value)
                elif "day" in unit:
                    past = now - timedelta(days=value)
                elif "week" in unit or "wk" in unit:
                    past = now - timedelta(weeks=value)
                elif "month" in unit:
                    past = now - timedelta(days=value * 30)
                elif "year" in unit or "yr" in unit:
                    past = now - timedelta(days=value * 365)
                else:
                    past = now
                return past.strftime("%b %d %Y")

        formats = [
            "%d %b %Y", "%B %d, %Y", "%d %B %Y", "%Y-%m-%d",
            "%b %d, %Y", "%b %d %Y", "%d/%m/%Y", "%m/%d/%Y",
            "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y", "%b %d", "%d %b"
        ]

        for fmt in formats:
            try:
                dt = datetime.strptime(content, fmt)
                if "%Y" not in fmt:
                    dt = dt.replace(year=now.year)
                return dt.strftime("%b %d %Y")
            except ValueError:
                continue

        return now.strftime("%b %d %Y")

    @staticmethod
    def extract_headlines(soup, origin, tag_name, class_filter):
        output = []

        candidates = soup.find_all(tag_name, class_=class_filter) if class_filter else soup.find_all(tag_name)

        for node in candidates:
            title = node.get_text(strip=True)
            if len(title) < 10:
                continue

            anchor = node.find("a") if tag_name != "a" else node
            href = anchor.get("href") if anchor else None
            if not href:
                continue

            link = ScraperHelper.format_url(origin, href)

            time_tag = node.find("time") or \
                       node.find(class_=re.compile(r"(date|time|published|timestamp)")) or \
                       (node.parent.find(class_=re.compile(r"(date|time|published|timestamp)")) if node.parent else None)

            sibling = node.previous_sibling
            while not time_tag and sibling:
                if hasattr(sibling, "find"):
                    time_tag = sibling.find(class_=re.compile(r"(date|time|published|timestamp)"))
                sibling = sibling.previous_sibling

            time_text = time_tag.get("datetime") if time_tag and time_tag.get("datetime") else (time_tag.get_text(strip=True) if time_tag else None)
            pub_date = ScraperHelper.parse_date(time_text) if time_text else datetime.now().strftime("%b %d %Y")

            label = "News"
            label_tag = node.find(class_=re.compile(r"(tag|category|genre|section|topic)")) or \
                        (node.parent.find(class_=re.compile(r"(tag|category|genre|section|topic)")) if node.parent else None)

            if label_tag:
                content = label_tag.get_text(strip=True)
                if content:
                    label = content

            if title and link:
                output.append((title, link, pub_date, label))

        return output

    @staticmethod
    def print_headlines(items):
        if not items:
            print("No headlines found.")
            return

        print("\nExtracted Headlines:")
        print("-" * 60)

        for idx, (title, url, date, label) in enumerate(items, 1):
            print(f"{idx}. {title}")
            print(f"   Link: {url}")
            print(f"   Date: {date}")
            print(f"   Tag: {label}")
            print("-" * 60)
