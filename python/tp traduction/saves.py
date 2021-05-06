import json
def openSave():
    fp = open('1.json',)
    dictionnaire = json.load(fp)
    return dictionnaire

def savesName(dictionnaire):
    with open('1.json','w') as fp:
        json.dump(dictionnaire,fp)