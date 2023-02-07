import pandas as pd
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

if page.status_code == 200:
    lienrecherche = page.url

doctors = soup.findAll('div', class_='item-professionnel')
doctor_infos = []

for doctor in doctors[:50]:
    name = doctor.find("div", class_='nom_pictos').text.strip()
    if doctor.find('div', class_='tel'):
        phone = doctor.find('div', class_='tel').text.strip()
    else:
        phone = "No phone"

    adresse = soup.find('div', class_='adresse').text.strip()
    doctor_infos.append({"name": name, "tel": phone, "adresse": adresse})
    csv = pd.DataFrame(doctor_infos)
    csv.to_csv("doctors.csv", index=False)
