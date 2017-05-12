# coding=utf-8
from framework.data_proc.jsonLib import get_value_from_json
from project.configuration.api_config import api_url, api_version
from framework.http.httpLib import HttpLib
from project.configuration.statusCode import status_code_200
from project.configuration.configReader import parse_value_from_users_tokens
from project.model.user import User


class FriendsApi(object):
    def __init__(self, account_id):
        self.token = parse_value_from_users_tokens()[account_id]

    def add(self, user_id, text=None):
        """
        Одобряет или создает заявку на добавление в друзья. Если идентификатор выбранного пользователя присутствует в
        списке заявок на добавление в друзья, полученном методом friends.getRequests, то одобряет заявку на добавление и
        добавляет выбранного пользователя в друзья к текущему пользователю. В противном случае создает заявку на
        добавление в друзья текущего пользователя к выбранному пользователю.
        После успешного выполнения возвращает одно
        из следующих значений:
            1 — заявка на добавление данного пользователя в друзья отправлена;
            2 — заявка на добавление в друзья от данного пользователя одобрена;
            4 — повторная отправка заявки.
        """
        url = '{api}friends.add'.format(api=api_url)
        params = {'user_id': user_id,
                  'access_token': self.token,
                  'text': text,
                  'v': api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Friends.add"  FAILED. {text}'.format(text=res.response.text)
        return get_value_from_json(res.response.json(), 'response')

    def are_friends(self, user_ids):
        """
        Возвращает информацию о том, добавлен ли текущий пользователь в друзья у указанных пользователей.
        Также возвращает информацию о наличии исходящей или входящей заявки в друзья (подписки).
        После успешного выполнения возвращает массив объектов status, каждый из которых содержит следующие поля:
            friend_status — статус дружбы с пользователем:
                0 – пользователь не является другом,
                1 – отправлена заявка/подписка пользователю,
                2 – имеется входящая заявка/подписка от пользователя,
                3 – пользователь является другом;
        """
        url = "https://api.vk.com/method/friends.areFriends"
        params = {'user_ids': user_ids,
                  'access_token': self.token,
                  'v': '5.64'}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Friends.are_firends"  FAILED. {text}'.format(text=res.response.text)
        response = get_value_from_json(res.response.json(), 'response')[0]
        return get_value_from_json(response, 'friend_status')

    def get(self, user_id=None):
        """

        """
        url = '{api}friends.get'.format(api=api_url)
        params = {'user_id': user_id,
                  'fields': 'has_photo, photo_id, can_write_private_message, last_seen',
                  'access_token': self.token,
                  'v': api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Friends.add"  FAILED. {text}'.format(text=res.response.text)
        response = get_value_from_json(res.response.json(), 'response')
        friends_list = get_value_from_json(response, 'items')
        friends_model_list = []
        for friend in friends_list:
            friend_model = User(friend)
            friends_model_list.append(friend_model)
        return friends_model_list


# url = 'https://api.vk.com/method/friends.add'
# params = {'user_id': '310582170',
#           'captcha_sid': '299917636468',
#           'captcha_key ': 's7amh',
#           'access_token': '014d3430a604a0e5e4ebc684e011ad149c37280e6d34cbb1d6b19c59926b38629797283d0e63c77127235',
#           'v': '5.64'}
# res = HttpLib(url=url,
#               params=params).send_get()
# status_code = res.response.status_code
# print status_code
