import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        articles = []
        while url != "":
            #time.sleep(1)
            print(url)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
                
            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])
    
                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)
    
            next_page = doc.select_one(".navigation .btn")
            if next_page:
                next_link = next_page.attrs["href"]
                next_link = urljoin(url, next_link)
                #print(next_link)
                url = next_link
            else:
                url = ""
        return articles

review = ArticleFetcher()
for i,article in enumerate(review.fetch(),1):
    print(f"{i}- {article.emoji}{article.title}")