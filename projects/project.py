import os
import requests
import json
import sys


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
    sys.stdout.write("Downloading : [                                                                                                    ]\r")
    sys.stdout.flush()
    # 66 chars
    # 1000 elements - 10 elements = 1%
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
                    if k < j:
                        case.append("=")
                    else:
                        case.append(" ")
                sys.stdout.write("Downloading : [" + "".join(case) + "]\r")
                sys.stdout.flush()


getMostPopularRepo()