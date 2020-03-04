import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url):
    bs = BeautifulSoup(requests.get(url).text, 'lxml')

    ingredients_list = bs.select('div.ingredients-list-content-item')

    ingredients = []

    for ingredient in ingredients_list:
        ingredient_name = ingredient.select_one('p.ingredient-name span.text-bg-white').text.strip()
        ingredient_quantity_tag = ingredient.select_one('p.quantity span.text-bg-white')
        if ingredient_quantity_tag:
            ingredient_quantity = ingredient_quantity_tag.text.strip()
        else: 
            ingredient_quantity = '---'
        
        ingredients.append( [url, ingredient_name, ingredient_quantity] )

    print(ingredients)

    return ingredients