from index.opener import openFile
from index.extracter import extractTitles
from index.statistics import countToken


# Charger les données à partir du fichier JSON
    
data = openFile("crawled_urls.json")
print("Nombre de documents :", len(data))

# Compter le nombre de tokens
titres = extractTitles(data)
print("Nombre de tokens :", countToken(titres))

