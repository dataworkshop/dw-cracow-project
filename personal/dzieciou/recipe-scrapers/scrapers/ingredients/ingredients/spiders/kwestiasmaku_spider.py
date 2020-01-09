import scrapy


class KwestiaSmakuSpider(scrapy.Spider):
  name = 'kwestiasmaku'
  allowed_domains = ['www.kwestiasmaku.com']
  # FIXME Some recipes are not downloaded, e.g., https://www.kwestiasmaku.com/ryby_i_owoce_morza/dorsz/dorsz_pomidory/przepis.html
  start_urls = [
    'https://www.kwestiasmaku.com'

  ]

  def parse(self, response):
    def extract(query):
      e = response.css(query).get()
      return None if e is None else e.strip()

    def extract_list(query):
      return [i.strip() for i in response.css(query).getall()]

    if any(s in response.url for s in ['/przepis/', 'przepis.html']):
      ingredients = extract_list('.field-name-field-skladniki>ul>li::text')
      portions_count = extract('div.field-name-field-ilosc-porcji::text')
      yield {'url': response.url,
             'portions_count': portions_count,
             'ingredients': ingredients}

    for a in response.css('span.field-content a'):
      yield response.follow(a, callback=self.parse)

    for a in response.css('li.next a'):
      yield response.follow(a, callback=self.parse)

    for a in response.css('a[href]'):
      yield response.follow(a, callback=self.parse)

