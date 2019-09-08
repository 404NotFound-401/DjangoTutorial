import requests


def getName(name):
    processName = name.replace(" ", "+")

    path = "http://www.omdbapi.com/?t="
    api_key = '&apikey=d6f684e4'
    search = path + processName + api_key
    r = requests.get(search)
    return r.text
