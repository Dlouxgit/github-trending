import requests
from bs4 import BeautifulSoup
import datetime
import os

def fetch_trending(language=None, since='daily'):
    url = f"https://github.com/trending/{language}?since={since}" if language else f"https://github.com/trending?since={since}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    repos = []
    for article in soup.find_all('article', class_='Box-row'):
        title = article.find('h1', class_='h3 lh-condensed').text.strip()
        link = "https://github.com" + article.find('a')['href']
        description = article.find('p', class_='col-9 color-fg-muted my-1 pr-4').text.strip() if article.find('p', class_='col-9 color-fg-muted my-1 pr-4') else "No description provided"
        stars = article.find('a', class_="Link--muted d-inline-block mr-3").text.strip()
        forks = article.find_all('a', class_="Link--muted d-inline-block mr-3")[1].text.strip() if len(article.find_all('a', class_="Link--muted d-inline-block mr-3")) > 1 else "0"
        repos.append({"title": title, "link": link, "description": description, "stars": stars, "forks": forks})
    return repos

if __name__ == "__main__":
    trending_data = fetch_trending()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"trending_{now}.json"
    import json
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(trending_data, f, ensure_ascii=False, indent=4)
    print(f"Trending data saved to {filename}")