import requests, json, time, os, math

last_repositories = {}
best_repositories = {}


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
        # title_desc = "Title : " + item["name"] + "\n" + (item["description"] is not None and "Description : " +
        #                                                 item["description"] or "Description : None") + "\n\n"
        i += 1
    repo_json = json.dumps(repo_dict)
    open(file_name, "w", encoding="utf8").write(repo_json)


def getMostPopularRepo():
    repo_dict = {}
    file_name = "repositories/data_best_repositories.json"
    print("Downloading : [                                                    "
          "                                                ]", end="\r")
    j = 0
    for i in range(1, 11):
        json_item = getAPIHttpRequest("https://api.github.com/search/repositories?sort=stars"
                                      "&per_page=100&q=created:2020-01-01&page=" + str(i))["items"]
        for item in json_item:
            repo_dict[j] = {}
            repo_dict[j]["title"] = item["name"]
            repo_dict[j]["description"] = item["description"]
            repo_dict[j]["stars"] = item["stargazers_count"]
            # title_desc = "Title : " + item["name"] + "\n" + \
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
    file = open(file_name, "a", encoding="utf8").write(repo_json)
    print("Download Complete !", end="\n")


def initialiseJsonFiles():
    last_file = "repositories/data_last_repositories.json"
    best_file = "repositories/data_best_repositories.json"
    last_file_content = open(last_file, "r", encoding="utf8").read()
    best_file_content = open(best_file, "r", encoding="utf8").read()

    last_json = json.loads(last_file_content)
    best_json = json.loads(best_file_content)

    last_repositories = last_json
    best_repositories = best_json


def getLastRepositories():
    return last_repositories


def getBestRepositories():
    return best_repositories


def getUserAllReposPage(user):
    response = getAPIHttpRequest("https://api.github.com/users/" + user)
    count = response["public_repos"]
    return math.ceil(count / 100)


def viewUserStarChanges(user):
    repo_info = json.dumps(getAllRepoInfo(getUserAllReposPage(user), user))
    if not os.access("./users/" + user + ".json", os.R_OK):
        open("./users/" + user + ".json", "w", encoding="utf8").write(repo_info)
    else:
        user_file = open("./users/" + user + ".json", "r", encoding="utf8").read()
        user_json = json.loads(user_file)
        more_stars = {}
        i = 0
        dictionary = json.loads(open("./users/" + user + ".json", "r", encoding="utf8").read())
        for items in dictionary:
            print(json.loads(repo_info))
            if repo_info[i][1] > items["stars"]:
                print("MORE STARS")
            i += 1

def getAllRepoInfo(pages, user):
    dictionary = {}
    j = 0
    for page in range(1, pages+1):
        reponse = getAPIHttpRequest("https://api.github.com/users/" + user + "/repos?per_page=100&page=" + str(page))
        for items in reponse:
            dictionary[j] = {}
            dictionary[j]["title"] = items["name"]
            dictionary[j]["stars"] = items["stargazers_count"]
            j += 1
    return json.dumps(dictionary)


viewUserStarChanges("facebook")
#initialiseJsonFiles()
#getLastPublicRepo()
#getMostPopularRepo()
