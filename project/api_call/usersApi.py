# coding=utf-8
from framework.data_proc.jsonLib import get_value_from_json
from framework.http.httpLib import HttpLib
from project.api_call.baseApi import BaseApi
from project.configuration.statusCode import status_code_200
from project.model.user import User


class UsersApi(BaseApi):
    def __init__(self, token):
        super(UsersApi, self).__init__()
        self.token = token

    def search(self, count, city, sex, age_from, age_to, offset=None, status=None, birth_day=None, birth_month=None):
        """
        Возвращает список пользователей в соответствии с заданным критерием поиска.
        После успешного выполнения возвращает объект, содержащий число результатов
            в поле count и массив объектов, описывающих пользователей в поле items.

        Параметры: https://vk.com/dev/users.search
        :return (list<user>)
        """
        url = '{api}users.search'.format(api=self.api_url)
        params = {'city': city,
                  'sort': '0',
                  'offset': offset,
                  'count': count,
                  'fields': 'can_write_private_message, last_seen, has_photo, photo_id, blacklisted, friend_status',
                  'sex': sex,
                  'status': status,
                  'age_from': age_from,
                  'age_to': age_to,
                  'birth_day': birth_day,
                  'birth_month': birth_month,
                  'access_token': self.token,
                  'v': self.api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Users.search"  FAILED. {text}'.format(text=res.response.text)
        response = get_value_from_json(res.response.json(), 'response')
        users_list = get_value_from_json(response, 'items')
        user_model_list = []
        for user in users_list:
            if not(UsersApi.is_blacklisted(user)) and (user['id'] not in [11225104,
                                                                          150437158]):
                user_model = User(user)
                user_model_list.append(user_model)
        self.logger.log_info(u'Всего найдено пользователей: {count}.'.format(count=len(user_model_list)))
        return user_model_list

    @staticmethod
    def is_blacklisted(user_json):
        if get_value_from_json(user_json, 'blacklisted') == 1:
            return True
        else:
            return False

    def get(self, user_id):
        url = '{api}users.get'.format(api=self.api_url)
        params = {'user_ids': user_id,
                  'fields': 'can_write_private_message, last_seen, has_photo, photo_id, blacklisted, friend_status',
                  'access_token': self.token,
                  'v': self.api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Users.get"  FAILED. {text}'.format(text=res.response.text)
        response = get_value_from_json(res.response.json(), 'response')[0]
        if get_value_from_json(response, 'blacklisted') == 0:
            return User(response)

    # def get_nearby(self):
    #     url = '{api}users.getNearby'.format(api=self.api_url)
    #     params = {'latitude': '53.905265',
    #               'longitude': '27.553459',
    #               # 'accuracy': 1000,
    #               'radius': 4,
    #               'access_token': self.token,
    #               'v': self.api_version}
    #     res = HttpLib(url=url,
    #                   params=params).send_get()
    #     status_code = res.response.status_code
    #     print status_code
    #     print res.response.json()
    #     users_list = res.response.json()['response']['items']
    #     user_model_list = []
    #     for user in users_list:
    #         user_model = User(user)
    #         print user_model
    #         user_model_list.append(user_model)
    #     return user_model_list
