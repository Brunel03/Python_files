from bs4 import BeautifulSoup
html = """
    <!DOCTYPE html>

    <html lang="de">
    <head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta content="" name="description"/>
    <meta content="" name="author"/>
    <title>Crawler-Auflistung</title>
    <!-- Bootstrap core CSS -->
    <link href="./lib/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>
    <link href="./css/narrow-jumbotron.css" rel="stylesheet"/>
    </head>
    <body>
    <div class="container">
    <div class="header clearfix">
    <nav>
    <ul class="nav nav-pills float-right">
    <li class="nav-item">
    <a class="nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
    </li>
    <li class="nav-item">
    <a class="nav-link" href="#">About</a>
    </li>
    <li class="nav-item">
    <a class="nav-link" href="#">Contact</a>
    </li>
    </ul>
    </nav>
    <h3 class="text-muted">Crawler-Auflistung</h3>
    </div>
    <div class="jumbotron">
    <h1 class="display-3">Crawler-Auflistung</h1>
    <p class="lead">
    	        Eine Ansammlung an Daten, die du automatisiert Crawlen darfst.<br/>
    	        Alles zufällig generierte Daten. 
    	    </p>
    </div>
    <div class="row content">
    <div class="col-lg-12">
    <p>Seite: 1 von 6</p>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/1.jpg" target="_blank">
    <img alt="Bild 1" class="img-responsive float-right" src="./img/1.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😩</span>
    <span>Polarised modular conglomeration</span>
    </h4>
    <p class="card-text">Optio numquam ut accusantium laborum unde assumenda. Ea et totam asperiores fugiat voluptatem vitae. Et provident nam et mollitia.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/2.jpg" target="_blank">
    <img alt="Bild 2" class="img-responsive float-right" src="./img/2.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😐</span>
    <span>Cross-group contextually-based middleware</span>
    </h4>
    <p class="card-text">Deleniti atque autem et commodi cupiditate cupiditate. Fuga illum quas aliquam velit. Labore dolor fugit quia id odio nam.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/3.jpg" target="_blank">
    <img alt="Bild 3" class="img-responsive float-right" src="./img/3.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😌</span>
    <span>De-engineered encompassing structure</span>
    </h4>
    <p class="card-text">Assumenda tempora inventore harum cumque voluptatibus sit et. Et omnis et dolore quod voluptas sit a.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/4.jpg" target="_blank">
    <img alt="Bild 4" class="img-responsive float-right" src="./img/4.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😚</span>
    <span>Fully-configurable multi-tasking interface</span>
    </h4>
    <p class="card-text">Cumque unde officia autem quia at fugit. Sint iure veritatis culpa aut provident aliquam in. Eos eum accusantium quia vel dignissimos nesciunt expedita. Rem aut accusantium et tempore.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/5.jpg" target="_blank">
    <img alt="Bild 5" class="img-responsive float-right" src="./img/5.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😠</span>
    <span>Versatile eco-centric core</span>
    </h4>
    <p class="card-text">Delectus distinctio quis omnis ut commodi sed. Beatae officia doloribus consequatur dolore. Consectetur impedit quia voluptas et ut. Incidunt rem mollitia fugiat quia corporis quo. Quod possimus ut et neque deserunt.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/6.jpg" target="_blank">
    <img alt="Bild 6" class="img-responsive float-right" src="./img/6.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😮</span>
    <span>Optional maximized utilisation</span>
    </h4>
    <p class="card-text">Consequatur sit deleniti sunt aut ullam eos. Vel ex ut sunt velit provident corporis consequatur. Ea est dolorum ut atque unde. Quasi itaque nihil pariatur.</p>
    </div>
    </div>
    <br/>
    <div class="card">
    <div class="card-block">
    <a href="./img/7.jpg" target="_blank">
    <img alt="Bild 7" class="img-responsive float-right" src="./img/7.jpg" style="max-height: 100px;max-width:110px;margin-left:15px;"/>
    </a>
    <h4 class="card-title">
    <span class="emoji">😢</span>
    <span>Open-architected secondary product</span>
    </h4>
    <p class="card-text">Reiciendis dolor quisquam tempora in. Totam ut distinctio vero. Ullam maiores dolor sunt voluptas.</p>
    </div>
    </div>
    <br/>
    <div class="navigation">
    <a class="btn btn-primary" href="index.php?page=2">Zur nächsten Seite!</a>
    </div>
    </div>
    </div>
    <footer class="footer">
    <p>© Company 2017</p>
    </footer>
    </div>
    </body>
    </html>
"""
doc = BeautifulSoup(html, "html.parser")

for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title = card.select(".card-title span")[1].text
    image = card.select_one("img").attrs["src"]
    
    print(image)
    print(emoji)
    print(title)
    print(content,"\n")

class CrawlerArticle():
    def __init__(self,title,image,emoji,content):
        self.title = title
        self.image = image
        self.emoji = emoji
        self.content = content
        
class ArticleFetcher():
    def fetch(self):
        doc = BeautifulSoup(html, "html.parser")
        articles = []        
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = card.select_one("img").attrs["src"]
        
            crawler = CrawlerArticle(title,image,emoji,content)
            articles.append(crawler)
        return articles

#for article in articles:
    #print(article.title)
    #print(article.image)
    #print(article.emoji)
    #print(article.content,"\n")
    #print(article)
"""
scraped = ArticleFetcher()
artikeln = scraped.fetch()

for artikel in artikeln:
    print(artikel.emoji)
"""
