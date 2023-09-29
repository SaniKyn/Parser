import requests
import lxml
import json
from bs4 import BeautifulSoup


def get_exc(file: str) -> BeautifulSoup:
    with open(file, 'r', encoding='utf-8') as file:
        item_scr = file.read()
    item_soup = BeautifulSoup(item_scr, 'lxml')
    exc_type_muscles = item_soup.find_all('div', class_='row p-0 m-0')


get_exc('Triceps.html')
