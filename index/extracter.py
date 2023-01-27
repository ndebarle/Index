from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import urllib.request




def extractTitles(data):
    titres = {}
    for url in data:
        try:
            with urllib.request.urlopen(url) as f:
                soup = BeautifulSoup(f, 'html.parser')
                titres[url] = word_tokenize(soup.title.string)
                print(url, "OK", soup.title.string)            
        except:
            print('Erreur sur le lien', url)
    return titres