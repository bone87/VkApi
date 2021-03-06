from project.configuration.api_config import api_url, api_version
from framework.support.MyLogger import MyLogger


class BaseApi(object):
    def __init__(self):
        self.api_url = api_url
        self.api_version = api_version
        self.logger = MyLogger()
