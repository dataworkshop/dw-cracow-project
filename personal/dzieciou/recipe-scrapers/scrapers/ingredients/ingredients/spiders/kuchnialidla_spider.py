import scrapy


class KwestiaSmakuSpider(scrapy.Spider):
  name = 'kuchnialidla'
  allowed_domains = ['www.kuchnialidla.pl', 'kuchnialidla.pl']
  start_urls = [
    'https://kuchnialidla.pl/przepisy'
  ]

  def parse(self, response):
    def extract_by_xpath(query):
      e = response.xpath(query).get()
      return None if e is None else e.strip()

    def extract(query):
      e = response.css(query).get()
      return None if e is None else e.strip()

    def extract_list(query):
      return [i.strip() for i in response.css(query).getall()]

    title = extract_by_xpath('/html/head/title/text()')
    if 'przepis' in title:
      ingredients = extract_list('div.skladniki ul li::text')
      portions_count = extract('li.meta_size::text')
      yield {'url': response.url,
             'portions_count': portions_count,
             'ingredients': ingredients}

    for a in response.css('a.description'):
      yield response.follow(a, callback=self.parse)

    for a in response.css('a.nextPage'):
      yield response.follow(a, callback=self.parse)
