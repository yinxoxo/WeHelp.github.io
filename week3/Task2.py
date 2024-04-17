import urllib.request as req
from bs4 import BeautifulSoup
import csv


# 取得每篇文章的標題及like數字
def fetch_titles_and_likes(url, writer):
    request = req.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
            "Cookie": "over18=1",  # 設置 cookie 符合年齡限制
        },
    )
    # 讀取網站
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    soup = BeautifulSoup(data, "html.parser")
    entries = soup.find_all("div", class_="r-ent")
    for entry in entries:
        title_tag = entry.find("div", class_="title")
        if title_tag.a:  # 跳過被刪除的文章
            title = title_tag.a.text
            article_url = "https://www.ptt.cc" + title_tag.a["href"]
            like_tag = entry.find("div", class_="nrec")
            like_text = (
                like_tag.span.text if like_tag.span else "0"  # 如果没有 like 數字就為0
            )
            publish_time = fetch_article_details(article_url)
            writer.writerow([title, like_text, publish_time])  # 寫入 CSV

    # 抓取上一頁連結
    prev_link = soup.find("a", string="‹ 上頁")  # 找到內文是‹ 上頁的a標籤
    return prev_link["href"]


# 取得發佈的日期時間
def fetch_article_details(article_url):
    request = req.Request(
        article_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
            "Cookie": "over18=1",
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    # 找尋發佈時間
    meta_tags = soup.find_all("span", class_="article-meta-value")
    for tag in meta_tags:
        if ":" in tag.text and "/" not in tag.text:  # 檢查是否符合時間格式
            return tag.text
    return " "


# 初始的URL
url = "https://www.ptt.cc/bbs/Lottery/index.html"
count = 0
# 寫入article.csv
with open("article.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # 抓取前三頁內容
    while count < 3:
        if url:
            next_page = fetch_titles_and_likes(url, writer)
            url = "https://www.ptt.cc" + next_page if next_page else None
            count += 1
