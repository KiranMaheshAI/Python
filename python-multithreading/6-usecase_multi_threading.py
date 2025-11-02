"""
Real World Example: Multithreading for I/O Bound Tasks
Scenario: Web scraping
Web scraping often involves making numerous network requests to fetch data from multiple web pages.
These tasks are I/O-bound because the program spends a significant amount of time waiting for responses from web servers.
Multithreading can be used to perform multiple requests concurrently, significantly speeding up the scraping process.
"""

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/deepagents/overview",
    "https://docs.langchain.com/oss/python/modules/models/overview",
]

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        print(f"Fetched {url} with title: {title}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_and_parse, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        print("Finished fetching all URLs.")