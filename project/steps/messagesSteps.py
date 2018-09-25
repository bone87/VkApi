# coding=utf-8

from framework.support.commonFunctions import get_random_int, sleep
from framework.support.MyLogger import MyLogger
from project.api_call.messagesApi import MessagesApi
from project.steps.usersSteps import detete_more_10_weeks_last_seen_users
import random

logger = MyLogger()


def send_message(token, user_model, message):
    """
    Отправляет сообщение.
    После успешного выполнения возвращает идентификатор отправленного сообщения.
    """
    return MessagesApi(token).send(user_model=user_model, text=message)


def send_birthday_message(token, user_model):
    if user_model.can_write_private_message == 1:
        birthday_message = 'с днЁм рождения😊 Здоровья, любви, тепла и чтобы всё сбылось, что сегодня нажелают😉'
        birthday_message2 = 'с днем рождения😊 Желаем вам крепкого здоровья, отличных друзей и исполнения самых безумных идей😉'
        birthday_message3 = 'с днем рождения! Не буду желать ничего хорошего, только лучшего😉 Успехов в делах, здоровья, новых открытий, самых приятных ' \
                            'эмоций. Пусть вся жизнь будет сплошным праздником!😊'
        birthday_message4 = 'c днем рождения😊 Желаю Вам счастья, бурной и преданной любви, материального благополучия и осуществления любых желаний😉'
        birthday_message5 = 'поздравляю Вас с днём рождения😊 Желаю успехов и счастья, здоровья и бодрости, оптимизма и исполнения задуманных планов. ' \
                            'Незабываемых впечатлений и только счастливых моментов😉'
        birthday_message6 = 'поздравляю😊 Пусть каждый день будет по-своему прекрасен, а жизнь полна любви и счастья😊'
        birthday_message7 = 'поздравляю Вас😊 Пусть именно сегодня сбудутся все ваши мечты и желания. С днЁм рождения😊'
        birthday_message8 = 'с праздником Вас😊 Желаю стремиться только к лучшему, с легкостью достигать желаемых целей и никогда не унывать😉'

        discount_message = 'В честь дня рождения мы дарим вам скидочку 20% на одну из наших услуг:\n' \
                           'установка Windows или чистка(устранение '\
                           'перегрева) компьютера/ноутбука.\n' \
                           'Ваша цена на любую из них - 29руб😊\n' \
                           'Действует в течение месяца😉'
        discount_message2 = 'Дарим Вам скидочку 20% на наши услуги(установка Windows/устранение перегрева ноутбука)😊\n' \
                            'Цена для Вас на любую из услуг - 29руб😊'
        discount_message3 = 'Вам скидочка 20% на одну из наших услуг: установка Windows/устранение перегрева ноутбука.\nЦена для Вас - 29руб😊.'
        end_dialog = 'Еще раз с праздником!😊'
        end_dialog2 = 'Хорошо Вам отметить😊'
        end_dialog3 = 'Отличного Вам праздника😉'
        end_dialog4 = 'Еще раз с Днем Рождения!😊'
        end_dialog5 = 'Хорошего дня и отлично отметить😊'
        message = '{birth}\n\n{discount}\n{end}'.format(birth=random.choice([birthday_message,
                                                                             birthday_message2,
                                                                             birthday_message3,
                                                                             birthday_message4,
                                                                             birthday_message5,
                                                                             birthday_message6,
                                                                             birthday_message7,
                                                                             birthday_message8]),
                                                        discount=random.choice([discount_message,
                                                                                discount_message2,
                                                                                discount_message3]),
                                                        end=random.choice([end_dialog,
                                                                           end_dialog2,
                                                                           end_dialog3,
                                                                           end_dialog4,
                                                                           end_dialog5]))
        return send_message(token=token,
                            user_model=user_model,
                            message=message)


def send_birthday_message_sto325(token, user_model):
    if user_model.can_write_private_message == 1:
        birthday_message = 'с днЁм рождения😊 Здоровья, любви, тепла и чтобы всё сбылось, что сегодня нажелают😉'
        birthday_message2 = 'с днем рождения😊 Желаем вам крепкого здоровья, отличных друзей и исполнения самых безумных идей😉'
        birthday_message3 = 'с днем рождения! Не буду желать ничего хорошего, только лучшего😉 Успехов в делах, здоровья, новых открытий, самых приятных ' \
                            'эмоций. Пусть вся жизнь будет сплошным праздником!😊'
        birthday_message4 = 'c днем рождения😊 Желаю Вам счастья, бурной и преданной любви, материального благополучия и осуществления любых желаний😉'
        birthday_message5 = 'поздравляю Вас с днём рождения😊 Желаю успехов и счастья, здоровья и бодрости, оптимизма и исполнения задуманных планов. ' \
                            'Незабываемых впечатлений и только счастливых моментов😉'
        birthday_message6 = 'с праздником Вас😊 Желаю стремиться только к лучшему, с легкостью достигать желаемых целей и никогда не унывать😉'

        discount_message = 'В честь дня рождения мы дарим вам бесплатную диагностику подвески, тормозной системы и ' \
                           'системы охлаждения! \n' \
                           'А так же: ароматизатор в машину и смазку для замков!\n' \
                           'Предварительная запись - обязательна!\n' \
                           'Наш телефон +375296235325. Сообщите нам промокод "ВК325" и забирайте подарки в течение месяца.\n' \
                           'sto325.by'
        end_dialog = 'Еще раз с праздником!😊'
        end_dialog2 = 'Хорошо Вам отметить😊'
        end_dialog3 = 'Отличного Вам праздника😉'
        end_dialog4 = 'Еще раз с Днем Рождения!😊'
        end_dialog5 = 'Хорошего дня и отлично отметить😊'
        message = '{birth}\n\n{discount}\n{end}'.format(birth=random.choice([birthday_message,
                                                                             birthday_message2,
                                                                             birthday_message3,
                                                                             birthday_message4,
                                                                             birthday_message5,
                                                                             birthday_message6]),
                                                        discount=random.choice([discount_message]),
                                                        end=random.choice([end_dialog,
                                                                           end_dialog2,
                                                                           end_dialog3,
                                                                           end_dialog4,
                                                                           end_dialog5]))
        return send_message(token=token,
                            user_model=user_model,
                            message=message)


def send_birthday_messages(token, users, max_count=20):
    count_users = len(users)
    logger.log_info('Найдено {len} чел.'.format(len=count_users))
    count = 0
    for birthday_user in users:
        if count >= max_count:
            break
        result = send_birthday_message(token=token,
                                       user_model=birthday_user)
        if result is not None:
            count += 1
            random_seconds = get_random_int(100, 200)
            logger.log_info('   {message}: {count}.'.format(message='Отправлено', count=count))
            sleep(random_seconds)
    logger.log_info('::: [END] Отправлено сообщений: {count}/{len}. :::'.format(count=count, len=count_users))
    return count


def send_birthday_messages_sto325(token, users, max_count=20):
    count_users = len(users)
    logger.log_info('Найдено {len} чел.'.format(len=count_users))
    count = 0
    for birthday_user in users:
        if count >= max_count:
            break
        result = send_birthday_message_sto325(token=token, user_model=birthday_user)
        if result is not None:
            count += 1
            random_seconds = get_random_int(100, 200)
            logger.log_info('   {message}: {count}.'.format(message='Отправлено', count=count))
            sleep(random_seconds)
    logger.log_info('::: [END] Отправлено сообщений: {count}/{len}. :::'.format(count=count, len=count_users))
    return count
