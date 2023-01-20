import json
import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

titres = {}

def recupere_titre(URL):
    try:
        with urllib.request.urlopen(URL) as f:
            soup = BeautifulSoup(f, 'html.parser')
            print(soup.title)
    except:
        print('Erreur sur le lien', URL)

# Charger les données à partir du fichier JSON
with open("crawled_urls.json", "r") as f:
    data = json.load(f)

print("Nombre de documents :", len(data))

for url in data:
    print(word_tokenize("Bonjour, c'est pour tester, s'il vous plait"))
    recupere_titre(url)
    print(titres)