# tools/sanctions_tool.py
import requests
import csv
from io import StringIO

# Example: check OFAC consolidated list CSV url (public)
OFAC_CSV_URL = "https://www.treasury.gov/ofac/downloads/sdn.csv"

def fetch_ofac_names():
    resp = requests.get(OFAC_CSV_URL, timeout=15)
    resp.raise_for_status()
    text = resp.text
    reader = csv.reader(StringIO(text))
    names = set()
    for row in reader:
        if row:
            names.add(row[0].strip())
    return names

def is_on_ofac(name, cached=None):
    names = cached or fetch_ofac_names()
    return any(name.lower() in n.lower() for n in names)

from crewai_tools import Tool
sanctions_tool = Tool(
    name="Sanctions Lookup",
    description="Check basic public sanctions/watchlists for entity names",
    func=is_on_ofac
)
