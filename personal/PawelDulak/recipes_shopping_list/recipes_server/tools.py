import przepisy_pl_scraping

def scrape(data):
    result = []
    print('Start Scraping')

    # what site are we scraping from?
    for recipe in data:
        this_recipe = {
            'ingredients' : [],
            'message' : 'Nie mogłem pobrać składników potrawy',
            'url' : recipe['url'],
            'title' : recipe['title'],
            'success' : False,
        }
        
        if 'przepisy.pl/przepis/' in this_recipe['url']:
            # scrape from przepisy.pl
            print('scrape {}'.format(this_recipe['url']))
            this_recipe['ingredients'] = przepisy_pl_scraping.scrape(this_recipe['url'])

        result.append(this_recipe)

    return result

def merge(ingredients):
    return ingredients

