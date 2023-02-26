import requests
import json


class YaUploader():
    def __init__(self, token):
        self.base_host = 'https://cloud-api.yandex.net:443/'
        self.token = token


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }


    def create_folder(self):
        uri = 'v1/disk/resources'
        request_url = self.base_host + uri
        params = {
            'path': 'Testing',
            }
        response = requests.put(
            request_url, 
            params = params,
            headers = self.get_headers()
            )
        return response.status_code

    def check_folder(self):
        uri = 'v1/disk/resources'
        request_url = self.base_host + uri
        params = {'path': 'Testing'}
        response = requests.get(
            request_url, 
            params=params,
            headers=self.get_headers()
            )
        return response.status_code
        

