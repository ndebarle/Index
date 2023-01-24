import json

def openFile(document):
    with open(document, "r") as f:
        file = json.load(f)
    return file
