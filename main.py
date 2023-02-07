from wsgiref import headers

import requests
from bs4 import BeautifulSoup
from setuptools.unicode_utils import decompose

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

soup = BeautifulSoup(post.text, "html.parser")

doctors = soup.find_all('div', class_='item-professionnel')
doctor_infos = []

for doctor in doctors[:50]:
    name = doctor.find("div", class_='nom-pictos').text.strip()
    if doctor.find('div', class_='tel'):
        phone = doctor.find('div', class_='tel').text.strip()
    else:
        phone = "No phone"

    adresse = soup.find('div', class_='adresse')
    doctor_infos.append({"name": name, "phone": phone, "adresse": adresse})

print(doctor_infos)
