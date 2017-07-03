# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from framework.data_proc.jsonLib import get_pretty, get_value_from_json


class User(object):
    def __init__(self, response):
        self.blacklisted = get_value_from_json(response, 'blacklisted')
        self.user_id = get_value_from_json(response, 'id')
        self.first_name = get_value_from_json(response, 'first_name')
        self.last_name = get_value_from_json(response, 'last_name')
        self.friend_status = get_value_from_json(response, 'friend_status')
        self.can_write_private_message = get_value_from_json(response, 'can_write_private_message')
        self.has_photo = get_value_from_json(response, 'has_photo')
        self.last_seen = get_value_from_json(get_value_from_json(response, 'last_seen'), 'time')
        try:
            if self.has_photo == 1:
                self.photo_id = get_value_from_json(response, 'photo_id')
            else:
                self.photo_id = None
        except KeyError:
            self.has_photo = 0

    def __str__(self):
        return get_pretty(self.__dict__)
