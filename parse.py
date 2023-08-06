from time import sleep

import pandas
import requests
from bs4 import BeautifulSoup
from progress.bar import FillingCirclesBar
from progress.counter import Counter

from config import OUTPUT_DATA_DIR, BASE_URL, PAGES, SLEEP_TIME, URL

articles = []
bar = Counter("Обработка страницы ", max=len(PAGES))

for page in PAGES:
    bar.next()
    params = {
        "page": page,
    }

    r = requests.get(URL, params=params)

    soup = BeautifulSoup(r.text, "lxml")

    articles_soup = soup.find_all("article", class_="OPHIx", limit=50)
    bar_articles = FillingCirclesBar(
        "Обработка статьи ",
        max=len(articles_soup))

    for article in articles_soup:
        bar_articles.next()
        sleep(SLEEP_TIME)
        tag_a = article.find("h2", class_="h9Jmx").find("a")
        articles.append(
            {
                "date_time": article.find("time").get("datetime"),
                "title": tag_a.get("title"),
                "link": BASE_URL + tag_a.get("href"),
            }
        )
    bar_articles.finish()

bar.finish()

df = pandas.DataFrame(articles)
df.to_excel(OUTPUT_DATA_DIR)
