# coding=utf-8
from framework.http.httpLib import HttpLib
from project.api_call.baseApi import BaseApi
from project.configuration.statusCode import status_code_200
from project.configuration.configReader import parse_value_from_users_tokens


class LikesApi(BaseApi):
    def __init__(self, account_id):
        super(LikesApi, self).__init__()
        self.token = parse_value_from_users_tokens()[account_id]

    def is_liked(self, user_id, item_id_obj, type_obj='photo'):
        """
        Проверяет, находится ли объект в списке Мне нравится заданного пользователя.
        type:
            post — запись на стене пользователя или группы;
            comment — комментарий к записи на стене;
            photo — фотография;
            audio — аудиозапись;
            video — видеозапись;
            note — заметка;
            photo_comment — комментарий к фотографии;
            video_comment — комментарий к видеозаписи;
            topic_comment — комментарий в обсуждении;

        В случае успеха возвращает объект с полями:
            liked — есть ли отметка «Мне нравится» от текущего пользователя (0 — отметки нет, 1 — отметка есть);
            copied — сделан ли репост текущим пользователем (0 — не сделан, 1 — сделан).
        """
        url = '{api}likes.isLiked'.format(api=self.api_url)
        params = {'type': type_obj,
                  'owner_id': user_id,
                  'item_id': item_id_obj,
                  'access_token': self.token,
                  'v': self.api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Likes.isLiked"  FAILED. {text}'.format(text=res.response.text)
        response = res.response.json()['response']
        return response['liked'], response['copied']

    def add(self, owner_id, item_id_obj, type_obj='photo'):
        """
        Добавляет указанный объект в список Мне нравится текущего пользователя.
        type:
            post — запись на стене пользователя или группы;
            comment — комментарий к записи на стене;
            photo — фотография;
            audio — аудиозапись;
            video — видеозапись;
            note — заметка;
            photo_comment — комментарий к фотографии;
            video_comment — комментарий к видеозаписи;
            topic_comment — комментарий в обсуждении;

        В случае успеха возвращает объект с полем likes, в котором находится текущее количество пользователей, которые добавили данный объект в свой список Мне нравится.
        """
        url = '{api}likes.add'.format(api=self.api_url)
        params = {'type': type_obj,
                  'owner_id': owner_id,
                  'item_id': item_id_obj,
                  'access_token': self.token,
                  'v': self.api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Likes.add"  FAILED. {text}'.format(text=res.response.text)
        print 'Лайк проставлен. Пользователь: id{user_id}.'.format(user_id=owner_id)
        return res.response.json()['response']['likes']
