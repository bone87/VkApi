# coding=utf-8
import random
import time
import datetime

import math

from framework.support.commonFunctions import get_random_int, get_ten_weeks_before_date, convert_date_to_unix_time_stamp
from project.steps.messagesSteps import send_birthday_message
from project.steps.usersSteps import search_birthday_users, get_user_by_id

# 282 - Minsk
# 649 - Grodno
# 2017 - Borovlyany
minsk_id = 282
opera_account = '310582170'
ff_account = '291495044'


#
def send_birthday_messages(city_id,
                           account_id,
                           age_from,
                           age_to):
    list_birthday_users = search_birthday_users(city=city_id,
                                                account_id=account_id,
                                                age_from=age_from,
                                                age_to=age_to)
    print 'Найдено {len}'.format(len=len(list_birthday_users))
    count = 1
    for birthday_user in list_birthday_users:
        if birthday_user.last_seen >= convert_date_to_unix_time_stamp():
            result = send_birthday_message(account_id=account_id,
                                           user_model=birthday_user)
            if result is not None:
                random_seconds = get_random_int(60, 300)
                print '{message}: {count}, задержка {minutes:.2f} min'.format(message='Отправлено',
                                                                              count=count,
                                                                              minutes=float(random_seconds) / 60)
                time.sleep(random_seconds)
                count += 1
            if count >= 20:
                break
        else:

            print '[SKIP] id{user_id}, последняя активность: {date_time}.' \
                .format(user_id=birthday_user.user_id,
                        date_time=datetime.datetime.fromtimestamp(
                            birthday_user.last_seen))
    print 'Отправлено сообщений: {count}/{len}'.format(count=count-1,
                                                       len=len(list_birthday_users))


def opera_minsk_20_30():
    send_birthday_messages(city_id=minsk_id,
                           account_id=opera_account,
                           age_from=20,
                           age_to=30)


def opera_minsk_31_34():
    send_birthday_messages(city_id=minsk_id,
                           account_id=opera_account,
                           age_from=31,
                           age_to=34)


def ff_minsk_35_39():
    send_birthday_messages(city_id=minsk_id,
                           account_id=ff_account,
                           age_from=35,
                           age_to=39)


def ff_minsk_40_45():
    send_birthday_messages(city_id=minsk_id,
                           account_id=ff_account,
                           age_from=40,
                           age_to=45)


# ff_minsk_35_39()

user = get_user_by_id(account_id=opera_account,
                      user_id='112127288')
# print user
# photo = user.photo_id
# print photo
# last_seen = user.last_seen
# print last_seen
# print type(last_seen)
# print type()
# print last_seen > convert_date_to_unix_time_stamp()
#
# print datetime.datetime.fromtimestamp(1491202432.0)
# print get_ten_weeks_before_date()
# print parse_date_to_unix_time_stamp()
# result = send_birthday_message(account_id=account_id,
#                                user_model=user)
# print result
