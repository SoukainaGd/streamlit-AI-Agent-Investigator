# tools/scraper.py
import requests
import time
from urllib.parse import urlparse
import urllib.robotparser
from bs4 import BeautifulSoup

USER_AGENT = "MyResearchAgentBot/1.0 (+your_contact@example.com)"
DEFAULT_DELAY = 1.5  # seconds between requests (tune down politely)

_session = requests.Session()
_session.headers.update({"User-Agent": USER_AGENT})

_robot_parsers = {}

def can_fetch(url):
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    if base not in _robot_parsers:
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(base + "/robots.txt")
        try:
            rp.read()
        except:
            rp = None
        _robot_parsers[base] = rp
    rp = _robot_parsers[base]
    if not rp:
        return True
    return rp.can_fetch(USER_AGENT, url)

def fetch_html(url, timeout=15):
    if not can_fetch(url):
        raise PermissionError(f"Blocked by robots.txt: {url}")
    time.sleep(DEFAULT_DELAY)
    resp = _session.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.text

def extract_text_from_html(html, max_chars=8000):
    soup = BeautifulSoup(html, "html.parser")
    # remove scripts/styles
    for tag in soup(["script","style","noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    return text.strip()[:max_chars]

from crewai_tools import Tool
scraper_tool = Tool(
    name="Scraper Tool",
    description="Downloads a page (respecting robots.txt) and extracts text",
    func=lambda url: {"html": fetch_html(url), "text": extract_text_from_html(fetch_html(url))}
)
