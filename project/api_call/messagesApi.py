# coding=utf-8
from framework.data_proc.jsonLib import get_value_from_json
from framework.http.httpLib import HttpLib
from framework.support.MyLogger import MyLogger
from project.api_call.baseApi import BaseApi
from project.configuration.statusCode import status_code_200


class MessagesApi(BaseApi):
    def __init__(self, token):
        super(MessagesApi, self).__init__()
        self.token = token
        self.logger = MyLogger()

    def send(self, user_model, text):
        """
        Отправляет сообщение.
        После успешного выполнения возвращает идентификатор отправленного сообщения.
        """
        url = '{api}messages.send'.format(api=self.api_url)
        params = {'user_id': user_model.user_id,
                  'access_token': self.token,
                  'message': '{first_name}, {message}'.format(first_name=user_model.first_name,
                                                              message=text),
                  'v': self.api_version}
        res = HttpLib(url=url,
                      params=params).send_get()
        status_code = res.response.status_code
        assert status_code == status_code_200, '"Messages.send"  FAILED. {text}'.format(text=res.response.text)
        self.logger.log_info('   Сообщение отправлено. Пользователь: id{user_id}, {first_name} {last_name}.'.format(
            user_id=user_model.user_id,
            first_name=user_model.first_name,
            last_name=user_model.last_name))
        return get_value_from_json(res.response.json(), 'response')
