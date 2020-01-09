import scrapy


class KwestiaSmakuSpider(scrapy.Spider):
  name = 'jadlonomia'
  allowed_domains = ['www.jadlonomia.com']
  start_urls = [
    'http://www.jadlonomia.com/rodzaj_dania/sniadania/',
    'http://www.jadlonomia.com/rodzaj_dania/ciasta-i-desery/',
    'http://www.jadlonomia.com/rodzaj_dania/do-chleba/',
    'http://www.jadlonomia.com/rodzaj_dania/zupy/',
    'http://www.jadlonomia.com/rodzaj_dania/napoje/',
    'http://www.jadlonomia.com/rodzaj_dania/lunche-do-pracy/',
    'http://www.jadlonomia.com/rodzaj_dania/dania-glowne/',
    'http://www.jadlonomia.com/rodzaj_dania/sosy-i-dodatki/'
  ]

  def parse(self, response):
    def extract(query):
      e = response.css(query).get()
      return None if e is None else e.strip()

    def extract_list(query):
      return [i.strip() for i in response.css(query).getall()]

    if '/przepisy/' in response.url:
      l = [i.split("<br>") for i in response.css("#RecipeCard p").getall()]
      flat_list = [i for sublist in l for i in sublist]
      ingredients = [i.replace('<p>', '').replace('</br>', '').strip() for i in
                     flat_list]
      portions_count = None
      yield {'url': response.url,
             'portions_count': portions_count,
             'ingredients': ingredients}

    for a in response.css('a.sr'):
      yield response.follow(a, callback=self.parse)

    for a in response.css('a#LoadMore'):
      yield response.follow(a, callback=self.parse)
