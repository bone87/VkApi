import requests


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

    def send_get(self):
        self.response = requests.get(url=self.url,
                                     params=self.params,
                                     headers=self.header)
        return self

    def send_post(self):
        self.response = requests.post(url=self.url,
                                      params=self.params,
                                      body=self.body,
                                      json=self.json,
                                      headers=self.header)
        return self
