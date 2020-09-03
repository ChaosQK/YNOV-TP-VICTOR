import os
import requests
from bs4 import BeautifulSoup
import zipfile

os.chdir('./books')

def getBooksTitleAndAutor():
    titles = []
    authors = []
    dictionnary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        for line in current_file.readlines():
            if line.startswith("Title:"):
                titles.append(line.split(": ")[1].replace("\n", ""))
            elif line.startswith("Author:"):
                authors.append(line.split(": ")[1].replace("\n", ""))
                break
    dictionnary["titles"] = titles
    dictionnary["authors"] = authors
    return dictionnary

def renameAllBooks():
    dictionnary = getBooksTitleAndAutor()
    i = 0
    for file in os.listdir():
        os.rename(file, dictionnary["titles"][i].upper().replace(" ", "_") + "-" + dictionnary["authors"][i].upper().replace(" ", "_") + ".txt")
        i += 1


def wordsInBooks():
    dictionary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        filtre = filter(wordFilter, current_file.read().replace("\n", " ").replace(".", "").split(" "))
        dictionary[file.replace(".txt", "")] = len(' '.join(list(filtre)).split())
    return dictionary


def getAllWordOccurenceInBooks():
    dictionary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        words = filter(wordFilter, current_file.read().replace("\n", " ").replace(".", "").split(" "))
        all_words = (' '.join(list(words)).split())
        book_dictionnary = {}
        for word in all_words:
            if word.lower() not in book_dictionnary:
                book_dictionnary[word.lower()] = 1
            else:
                book_dictionnary[word.lower()] = book_dictionnary[word.lower()] + 1
        dictionary[file.replace(".txt", "")] = book_dictionnary
    return dictionary


def wordFilter(words):
    filtre = ["-", "", " ", "*", "...", ",,", ",", "\"" "'"]
    return words in filtre and False or True


def getAllWordOccurence():
    newdictionary = {} # creation du nouveau dictionnaire
    dictionary = getAllWordOccurenceInBooks() # récupération du dictionnaire des mots dans les livres
    for dicKey in dictionary: # boucle qui parcours toutes les clées "nom des livres" dans le dictionnaire
        for word in dictionary[dicKey]: # boucle qui parcours toutes les clées "mots" dans le dictionnaire dictionary[**dicKey**] (dicKey qui est la clé au dessus)
            if word not in newdictionary: # "if" qui vérifie qui n'y a pas le mot dans le nouveau dictionnaire
                newdictionary[word] = dictionary[dicKey][word] # On ajoute donc le mot et ça valeur dans le dictionnaire des livres
            else: # sinon
                newdictionary[word] = newdictionary[word] + dictionary[dicKey][word] # on récupère la valeur dans le nouveau dictionnaire et on fait la somme avec la valeur du dictionnaire des livres
    return newdictionary # on return le tout


def getTop10MostUsedWords():
    dictionary = getAllWordOccurence()
    all_words = []
    most_used = []
    sort = sorted(dictionary.items(), key=lambda x: x[1])
    for word in sort:
        all_words.append(word)

    for i in range(len(all_words)-1, len(all_words)-11, -1):
        most_used.append(all_words[i])

    return most_used


def getAllBookLinks():
    links = []
    results = requests.get("http://www.gutenberg.org/robot/harvest")
    parser = BeautifulSoup(results.text)
    for link in parser.find_all('a', href=True):
        if str(link["href"]).startswith("http://") and not "-h" in str(link["href"]).rsplit("/", 1)[1]\
                and str(link["href"]).rsplit("/", 1)[1].split(".")[1] == "zip":
            links.append(link["href"])
    return links

def downloadAllBooks():
    links = getAllBookLinks()
    i = 0
    for link in links:
        result = requests.get(link, allow_redirects=True)
        open("../dl_books/" + str(link).rsplit("/", 1)[1], "wb").write(result.content)
        i += 1

def unzipDownloadedBooks():
    os.chdir("../dl_books")
    for file in os.listdir():
        with zipfile.ZipFile(file, "r") as zip_file:
            zip_file.extractall("../books")
    for file in os.listdir():
        os.remove(file)
    os.chdir('../books')
    renameAllBooks()

renameAllBooks()