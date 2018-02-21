import requests

from framework.data_proc.jsonLib import get_value_from_json
from framework.support.MyLogger import MyLogger

class HttpLib(object):
    def __init__(self, url, header=None, params=None, cookie=None, body=None, json=None, auth=None, response=None):
        self.url = url
        self.header = header
        self.params = params
        self.cookie = cookie
        self.body = body
        self.json = json
        self.auth = auth
        self.response = response
        self.logger = MyLogger()

    def send_get(self):
        self.response = requests.get(url=self.url,
                                     params=self.params,
                                     headers=self.header)
        self.logger.log_pretty_json(json_message=get_value_from_json(self.response.json(), 'response'))
        return self

    def send_post(self):
        self.response = requests.post(url=self.url,
                                      params=self.params,
                                      body=self.body,
                                      json=self.json,
                                      headers=self.header)
        self.logger.log_pretty_json(json_message=get_value_from_json(self.response.json(), 'response'))
        return self
