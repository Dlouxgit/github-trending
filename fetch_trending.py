import requests
from bs4 import BeautifulSoup
import datetime
import os
import json 

def fetch_trending(language=None, since='daily'):
    url = f"https://github.com/trending/{language}?since={since}" if language else f"https://github.com/trending?since={since}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    repos = []
    for article in soup.find_all('article', class_='Box-row'):
        title = clean_text(article.find('h2', class_='h3 lh-condensed').text.strip())
        link = "https://github.com" + article.find('a')['href']
        description = clean_text(article.find('p', class_='col-9 color-fg-muted my-1 pr-4').text.strip() if article.find('p', class_='col-9 color-fg-muted my-1 pr-4') else "No description provided")
        stars = clean_text(article.find('a', class_="Link Link--muted d-inline-block mr-3").text.strip())
        forks = clean_text(article.find_all('a', class_="Link Link--muted d-inline-block mr-3")[1].text.strip() if len(article.find_all('a', class_="Link Link--muted d-inline-block mr-3")) > 1 else "0")
        repos.append({"title": title, "link": link, "description": description, "stars": stars, "forks": forks})
    return repos


def clean_text(text):
    """
    清理文本中的空格和换行符。
    """
    # 去除换行符 \n
    text = text.replace('\n', '')
    # 移除多余空格 (包括制表符 \t 等)
    text = text.strip()  # 去除首尾空格
    return text


if __name__ == "__main__":
    trending_data = fetch_trending()
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    # 1. 创建 trending 文件夹（如果不存在）
    output_dir = "trending"
    os.makedirs(output_dir, exist_ok=True)  # exist_ok=True 表示如果文件夹已存在则不报错

    # 2. 构建完整的文件路径
    filename = os.path.join(output_dir, f"trending_{now}.json")

    # 3. 保存 JSON 数据到指定路径
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(trending_data, f, ensure_ascii=False, indent=4)

    print(f"排行榜数据保存到 {filename}")