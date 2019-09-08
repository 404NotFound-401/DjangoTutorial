import requests


def getName(name):
    processName = name.replace(" ", "+")

    path = "http://www.omdbapi.com/?t="
    api_key = '&apikey=d6f684e4'
    search = path + processName + api_key
    r = requests.get(search)
    moive_info = string_process(r.text)
    return moive_info


def string_process(text_origin):
    moive_info = {}
    text_origin = text_origin[2:len(text_origin)-2]
    elements_list = text_origin.split('","')

    for element in elements_list:
        keywords = element.split('":"')
        moive_info[keywords[0]] = keywords[1]
    
    ratings = moive_info["Value"]
    moive_info["Value"] = ratings[:6]
    return moive_info

