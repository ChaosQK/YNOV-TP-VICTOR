import requests, json, time, os


def getAPIHttpRequest(link):
    results = requests.get(link)
    return json.loads(results.text)


def getLastPublicRepo():
    repo_dict = {}
    file_name = "repositories/data_last_repositories.json"
    json_item = getAPIHttpRequest("https://api.github.com/repositories")
    i = 0
    for item in json_item:
        repo_dict[i] = {}
        repo_dict[i]["title"] = item["name"]
        repo_dict[i]["description"] = item["description"]
        #title_desc = "Title : " + item["name"] + "\n" + (item["description"] is not None and "Description : " +
        #                                                 item["description"] or "Description : None") + "\n\n"
        i += 1
    repo_json = json.dumps(repo_dict)
    open(file_name, "w", encoding="utf8").write(repo_json)


def getMostPopularRepo():
    repo_dict = {}
    file_name = "repositories/data_best_repositories.json"
    print("Downloading : [                                                                                                    ]", end="\r")
    j = 0
    for i in range(1, 11):
        json_item = getAPIHttpRequest("https://api.github.com/search/repositories?sort=stars&per_page=100&q=created:2020-01-01&page=" + str(i))["items"]
        for item in json_item:
            repo_dict[j] = {}
            repo_dict[j]["title"] = item["name"]
            repo_dict[j]["description"] = item["description"]
            repo_dict[j]["stars"] = item["stargazers_count"]
            #title_desc = "Title : " + item["name"] + "\n" + \
            # (item["description"] is not None and "Description : " + item["description"] or "Description : None") +\
            # "\n" + "Stars : " + str(item["stargazers_count"]) + "\n\n"
            j += 1
            if j % 10 == 1:
                case = []
                for k in range(1, 101):
                    if k < (j/10):
                        case.append("=")
                    else:
                        case.append(" ")
                print("Downloading : [" + "".join(case) + "]", end="\r")
                time.sleep(0.1)
    repo_json = json.dumps(repo_dict)
    open(file_name, "a", encoding="utf8").write(repo_json)
    print("Download Complete !", end="\n")


getLastPublicRepo()
getMostPopularRepo()
