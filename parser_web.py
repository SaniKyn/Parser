import requests
import lxml
import json
from bs4 import BeautifulSoup


# def get_data(url):
#     headers = {
#         "User - Agent":
#             'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 116.0.0.0Safari / 537.36'
#     }
#     req = requests.get(url)
#     with open('new_index.html', 'w', encoding='utf-8') as file:
#         file.write(req.text)
#
#
# get_data('https://www.jefit.com/exercises/')

def get_text_file(file: str) -> json:
    with open(file, 'r', encoding='utf-8') as file:
        scr = file.read()
    soup = BeautifulSoup(scr, 'lxml')
    type_muscles = soup.find_all('div', class_='col-4 col-md-3 my-3 rounded-border')
    new_json = {}
    for item in type_muscles:
        item_name = item.find(class_="text-center mt-2").text.strip()
        item_href = item.find('a').get('href')
        req = requests.get(item_href).text
        soup = BeautifulSoup(req, 'lxml')
        exc_type_muscle = soup.find_all(class_='row p-0 m-0')
        list_exc = []
        new_json[item_name] = list_exc
        for j in exc_type_muscle:
            j_name = j.find('a').get('title')
            j_req = requests.get('https://www.jefit.com/exercises/' + j.find('a').get('href')).text
            j_soup = BeautifulSoup(j_req, 'lxml')
            exc_about = j_soup.find_all(class_='col-xl-9')
            how_lvl_exc = {}
            for k in exc_about:
                level_k = k.find('h1', class_='border-bottom').find('div').text.split()[0]
                how_do = k.find('p', class_='p-2').text
                how_lvl_exc[j_name] = {'level': level_k, 'how_to_do_it': how_do}
            list_exc.append(how_lvl_exc)

        with open('new_json.json', 'w', encoding='utf-8') as file_json:
            json.dump(new_json, file_json, indent=4)


get_text_file('new_index.html')
