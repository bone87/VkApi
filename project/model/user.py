# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json
from framework.data_proc.jsonLib import get_pretty, get_value_from_json


class User(object):
    def parse_response_to_user_model(self, response):
        self.user_id = get_value_from_json(response, 'id')
        self.first_name = get_value_from_json(response, 'first_name')
        self.last_name = get_value_from_json(response, 'last_name')
        self.friend_status = get_value_from_json(response, 'friend_status')
        self.can_write_private_message = get_value_from_json(response, 'can_write_private_message')
        self.has_photo = get_value_from_json(response, 'has_photo')
        try:
            self.last_seen = get_value_from_json(get_value_from_json(response, 'last_seen'), 'time')
            if self.has_photo == 1:
                self.photo_id = get_value_from_json(response, 'photo_id')
            else:
                self.photo_id = None
        except KeyError:
            self.has_photo = 0
        return self

    def __str__(self):
        return get_pretty(self.__dict__)
