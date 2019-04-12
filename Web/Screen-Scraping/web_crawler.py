# A simple web crawler using requests and Beautiful Soup
# Use with care, as it fetches pages serially without any delays, and doesn't look at robots.txt.

from queue import Queue
from typing import Dict
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

STARTING_URL = 'https://your web site'
IGNORE_PATHS = ('', '/')

found_paths_with_titles: Dict[str, str] = dict()
queue = Queue()
queue.put_nowait(STARTING_URL)

while not queue.empty():
    current_url: str = queue.get()
    parsed_current_url = urlparse(current_url)
    if parsed_current_url.path not in found_paths_with_titles:
        print('fetching ' + parsed_current_url.path)
        response = requests.get(current_url, headers={'User-Agent': 'Simple web crawler'})
        print('done fetching ' + parsed_current_url.path)
        if response.status_code != 200:
            print(f'Status code {response.status_code}')
        else:
            if 'text/html' in response.headers['content-type']:
                html_doc = response.text
                soup = BeautifulSoup(html_doc, 'html.parser')
                title = soup.find('title')
                found_paths_with_titles[parsed_current_url.path] = title.text if title else ''

                unique_paths = set()
                for parsed_url in (urlparse(a['href']) for a in soup.find_all('a', href=True)):
                    if parsed_url.path not in IGNORE_PATHS and not parsed_url.scheme:
                        start = 1 if parsed_url.path[0] == '/' else 0
                        unique_paths.add(parsed_url.path[start:])

                for path in unique_paths:
                    url: str = parsed_current_url.scheme + '://' + parsed_current_url.netloc + '/' + path
                    queue.put_nowait(url)

                print(f'Found {len(found_paths_with_titles)}, enqueued: {queue.qsize()}')
    queue.task_done()

longest_path: int = max((len(key) for key in found_paths_with_titles.keys()))
for key in sorted(found_paths_with_titles.keys()):
    print(f'{key:{longest_path + 1}s}{found_paths_with_titles[key]}')
