import os
import requests
import json
import sys, time


def getAPIHttpRequest(link):
    results = requests.get(link)
    return json.loads(results.text)


def getLastPublicRepo():
    json_item = getAPIHttpRequest("https://api.github.com/repositories")
    for item in json_item:
        title_desc = "Title : " + item["name"] + "\n" + (item["description"] is not None and "Description : " +
                                                         item["description"] or "Description : None") + "\n\n"
        open("./repositories/last_repositories.txt", "a").write(title_desc)


def getMostPopularRepo():
    print("Downloading : [                                                                                                    ]", end="\r")
    j = 0
    for i in range(1, 11):
        json_item = getAPIHttpRequest("https://api.github.com/search/repositories?sort=stars&per_page=100&q=created:2020-01-01&page=" + str(i))["items"]
        for item in json_item:
            title_desc = "Title : " + item["name"] + "\n" + \
             (item["description"] is not None and "Description : " + item["description"] or "Description : None") +\
             "\n" + "Stars : " + str(item["stargazers_count"])
            open("./repositories/best_repositories.txt", "a", encoding="utf8").write(title_desc)
            j += 1
            if j % 10 == 1:
                case = []
                for k in range(1, 101):
                    if k < (j/10):
                        case.append("=")
                    else:
                        case.append(" ")
                print("Downloading : [" + "".join(case) + "]", end="\r")
                time.sleep(0.5)
    print("Download Complete !", end="\n")


getMostPopularRepo()