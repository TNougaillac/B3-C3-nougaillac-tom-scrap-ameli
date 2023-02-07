from wsgiref import headers

import requests
from bs4 import BeautifulSoup

url = "http://annuairesante.ameli.fr/recherche.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

req = requests.Session()

params = {
        'type': 'ps',
        'ps_profession': '34',
        'ps_profession_label': 'Médecin généraliste',
        'ps_localisation': 'HERAULT (34)',
        'localisation_category': 'departements',
}

page = req.get(url)
post = req.post(url, params=params, headers=header)

content = post.content
soup = BeautifulSoup(post.content, "html.parser")

# resultlinks_to_parse = get_text_link(soup)

print(soup)
