import os
import requests

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
        os.rename(file, dictionnary["titles"][i] + "-" + dictionnary["authors"][i] + ".txt")
        i += 1


def wordsInBooks():
    dictionnary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        filtre = filter(wordFilter, current_file.read().replace("\n", " ").split(" "))
        dictionnary[file.replace(".txt", "")] = len(' '.join(list(filtre)).split())
    return dictionnary


def getAllWordOccurence():
    dictionnary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        words = filter(wordFilter, current_file.read().replace("\n", " ").split(" "))
        all_words = (' '.join(list(words)).split())

def wordFilter(words):
    filtre = ["-", "", " ", "*"]
    return words in filtre and False or True


getAllWordOccurence()