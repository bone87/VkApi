# coding=utf-8
import time

import datetime

from framework.support.commonFunctions import convert_date_to_unix_time_stamp, get_random_int, sleep
from framework.support.log import log_info
from project.api_call.messagesApi import MessagesApi
from project.steps.usersSteps import detete_more_10_weeks_last_seen_users


def send_message(account_id, user_model, message):
    """
    Отправляет сообщение.
    После успешного выполнения возвращает идентификатор отправленного сообщения.
    """
    return MessagesApi(account_id).send(user_model=user_model, text=message)


def send_birthday_message(account_id, user_model):
    if user_model.can_write_private_message == 1:
        birthday_message = 'с днЁм рождения) Здоровья, любви, тепла и чтобы всё сбылось, что сегодня нажелают😉'
        discount_message = 'В честь дня рождения мы дарим вам скидочку 10% на установку Windows или чистку ' \
                           'ноутбука, на выбор😊.\nДействует в течении месяца😉'
        end_dialog = 'Еще раз с праздником!😊'
        message = '{birth}\n\n{discount}\n{end}'.format(birth=birthday_message,
                                                        discount=discount_message,
                                                        end=end_dialog)
        return send_message(account_id=account_id,
                            user_model=user_model,
                            message=message)


def send_birthday_messages(account_id,
                           users):
    users = detete_more_10_weeks_last_seen_users(users)
    count_users = len(users)
    log_info('Найдено {len} чел.'.format(len=count_users))
    count = 1
    for birthday_user in users:
        result = send_birthday_message(account_id=account_id,
                                       user_model=birthday_user)
        if result is not None:
            random_seconds = get_random_int(500, 600)
            log_info('   {message}: {count}.'.format(message='Отправлено',
                                                     count=count))
            sleep(random_seconds)
            count += 1
            if count >= 20:
                break
    log_info('::: [END] Отправлено сообщений: {count}/{len}. :::'.format(count=count - 1,
                                                                         len=count_users))
