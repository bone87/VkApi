# coding=utf-8

from robot.libraries.BuiltIn import BuiltIn
from framework.support.commonFunctions import get_random_int, sleep
from framework.support.log import log_info
from project.api_call.messagesApi import MessagesApi
from project.steps.usersSteps import detete_more_10_weeks_last_seen_users
import random


def send_message(token, user_model, message):
    """
    Отправляет сообщение.
    После успешного выполнения возвращает идентификатор отправленного сообщения.
    """
    return MessagesApi(token).send(user_model=user_model, text=message)


def send_birthday_message(token, user_model):
    if user_model.can_write_private_message == 1:
        birthday_message = 'с днЁм рождения) Здоровья, любви, тепла и чтобы всё сбылось, что сегодня нажелают😉'
        birthday_message2 = 'с днем рождения😊 Желаем вам крепкого здоровья, отличных друзей и исполнения самых безумных идей😉'
        birthday_message3 = 'с днем рождения! Не буду желать ничего хорошего, только лучшего😉: успехов в делах, здоровья, новых открытий, самых приятных ' \
                            'эмоций. Пусть вся жизнь будет сплошным праздником!😊'
        discount_message = 'В честь дня рождения мы дарим вам скидочку 10% на установку Windows или чистку(устранение '\
                           'перегрева) компьютера/ноутбука, на выбор😊.\nДействует в течение месяца😉'
        end_dialog = 'Еще раз с праздником!😊'
        message = '{birth}\n\n{discount}\n{end}'.format(birth=random.choice([birthday_message, birthday_message2, birthday_message3]),
                                                        discount=discount_message,
                                                        end=end_dialog)
        return send_message(token=token,
                            user_model=user_model,
                            message=message)


def send_birthday_messages(token, users, max_count=20):
    users = detete_more_10_weeks_last_seen_users(users)
    count_users = len(users)
    log_info('Найдено {len} чел.'.format(len=count_users))
    count = 0
    for birthday_user in users:
        if count >= max_count:
            break
        result = send_birthday_message(token=token,
                                       user_model=birthday_user)
        if result is not None:
            count += 1
            random_seconds = get_random_int(20, 59)
            log_info('   {message}: {count}.'.format(message='Отправлено',
                                                     count=count))
            sleep(random_seconds)
    log_info('::: [END] Отправлено сообщений: {count}/{len}. :::'.format(count=count, len=count_users))
    if count < 5:
        BuiltIn().fail(msg='Count < {}'.format(count-1))
