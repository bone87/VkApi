# encoding=windows-1251
import sys
import json
import logging
import os
import datetime

reload(sys)
sys.setdefaultencoding('utf8')


class MyLogger(object):
    __instance = None

    def __new__(cls):
        if MyLogger.__instance is None:
            MyLogger.__instance = object.__new__(cls)
            MyLogger.__instance.__config__()
        return MyLogger.__instance

    def __config__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_name = os.path.join(os.path.dirname(__file__), datetime.datetime.now().strftime("%Y-%m-%d") + '.txt')
        fh = logging.FileHandler(self.file_name)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_info(self, message, *args, **kwargs):
        self.logger.log(level=logging.INFO, msg=message, *args, **kwargs)

    def log_debug(self, message, *args, **kwargs):
        self.logger.debug(msg=message, *args, **kwargs)

    def log_step(self, number):
        self.log_info(message='\n')
        self.log_info(message=':::::::::: {number} ::::::::::'.format(number=number))

    def log_pretty_json(self, json_message=None, message='JSON RESULT: '):
        self.log_debug(message=message + '\n' + json.dumps(json_message, sort_keys=True, indent=4) + '\n')

    def log_error(self, message, *args, **kwargs):
        self.logger.error(msg=message, args=args, kwargs=kwargs)

    def end_log(self):
        self.log_info(message='\n')
        self.log_info(":::::::::: END LOG ::::::::::")

    def __del__(self):
        self.end_log()
