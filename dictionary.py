import requests
import json

def Dictionary(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term":term}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "<API- KEY>"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_data = response.json()


    return response_data
