from logging.config import _OptionalDictConfigArgs
from app.utils import get_item
from app.models.opinion import Opinion
import requests
from bs4 import BeautifulSoup
from app.models.opinion import Opinion
from matplotlib import pyplot as plt
import json
import os


class Product():
    def __init__(self, product_id, name="", description="", price=0, opinions=[], pros_count=0, cons_count=0 , average_score=0, opinions_count=0):
        self.name = name
        self.product_id = product_id
        self.description = description
        self.price = price
        self.opinions = opinions
        self.pros_count= pros_count
        self.cons_count = cons_count
        self.average_score = average_score
        return self

    def extract_name(self):
        url = "https://www.ceneo.pl/"+product_id+"#tab=reviews"
        response
        self.product_name = get_item("h1.product-top__product-info__name")

        
        product-top


    def extract_opinions(self):
        url = "https://www.ceneo.pl/"+product_id+"#tab=reviews"
        while(url):
            response = requests.get(url)
            page = BeautifulSoup(response.text, "html.parser")
            opinions = page.select("div.js_product-review")
            for opinion in opinions:

                single_opinion = Opinion().extract_opinion(opinion) 
                self.opinions.append(single_opinion)
            try:
                url = "https://www.ceneo.pl"+get_item(page,"a.pagination__next")["href"]
            except TypeError:
                url = None
        return self
    def calculate_stats(self.opinions):
        
        opinions = pd.read_json(json.dumps)
