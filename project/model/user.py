# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json
from framework.data_proc.jsonLib import get_pretty


class User(object):
    def parse_response_to_user_model(self, response):
        self.user_id = response['id']
        self.first_name = response['first_name']
        self.last_name = response['last_name']
        self.friend_status = response['friend_status']
        self.can_write_private_message = response['can_write_private_message']
        self.has_photo = response['has_photo']
        try:
            self.last_seen = response['last_seen']['time']
            if self.has_photo == 1:
                self.photo_id = response['photo_id']
            else:
                self.photo_id = None
        except KeyError:
            self.has_photo = 0
        return self

    def __str__(self):
        return get_pretty(self.__dict__)
