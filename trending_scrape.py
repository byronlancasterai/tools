#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
sys.path.insert(0, "/config/byron/projects/dev_tools")
from simple_logger import log


def get_trending():
    # api.github.com is more reliable than scraping the HTML page.
    # Search recently updated repos sorted by stars as a trending proxy.
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'pushed:>2026-10-27',
        'sort': 'stars',
        'order': 'desc',
        'per_page': '10',
    }
    headers = {'User-Agent': 'byron-lancaster'}
    response = requests.get(url, headers=headers, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()
    results = []
    for item in data.get('items', []):
        results.append({
            'owner': item.get('owner', {}).get('login', ''),
            'project': item.get('name', ''),
            'stars': item.get('stargazers_count', 0),
        })
    return results

if __name__ == "__main__":
    import json
    from datetime import datetime
    data = get_trending()
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out = f"/config/byron/projects/trending_{ts}.json"
    with open(out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} repos to {out}")
