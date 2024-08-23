from dotenv import load_dotenv
import requests


class Api:
    def __init__(self, api_url, api_key):
        self.api_key =  api_key
        self.api_url = api_url
    def call_api(self, endpoint, payload = {}, headers = {}):
        url = f"{self.api_url}{endpoint}&api_key={self.api_key}"
        payload = payload
        headers = headers 
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
        

