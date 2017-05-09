# coding=utf-8
import time

from framework.support.commonFunctions import get_random_int, sleep
from framework.support.log import log_info
from project.api_call.friendsApi import FriendsApi


def add_quickly(account_id, user_model):
    status = FriendsApi(account_id).add(user_id=user_model.user_id)
    if status != 1:
        log_info('   Заявка на добавление в друзья НЕ ОТПРАВЛЕНА!'.format(user_id=user_model.user_id))
        return status
    else:
        if status == 1:
            log_info('   Добавлен в подписку.'.format(
                user_id=user_model.user_id,
                first_name=user_model.first_name,
                last_name=user_model.last_name))
            return status


def is_user_no_friend(account_id, user_model):
    if FriendsApi(account_id).are_friends(user_model.user_id) == 0:
        return True
    else:
        return False


def get_no_friends_only(users):
    return [user for user in users if user.friend_status == 0]


def add_friends(account_id, users):
    users_no_friends = get_no_friends_only(users)
    no_friends_count = len(users_no_friends)
    limit = get_random_int(30, 40)
    log_info('Найдено {len}/{all} чел.'.format(len=no_friends_count,
                                               all=len(users)))
    count = 1
    while count < limit and len(users_no_friends) >= 1:
        random_index = get_random_int(0, (len(users_no_friends) - 1))
        user = users_no_friends.pop(random_index)
        log_info('[{random}/{all}] Пользователь: id{id}, {first_name} {last_name}.'.format(random=random_index,
                                                                                           all=len(users),
                                                                                           id=user.user_id,
                                                                                           first_name=user.first_name,
                                                                                           last_name=user.last_name))
        if add_quickly(account_id=account_id, user_model=user) == 1:
            random_seconds = get_random_int(500, 800)
            log_info('   {message}: {count}.'.format(message='Подписано',
                                                     count=count))
            sleep(random_seconds)
            count += 1
            if count >= limit:
                break
    log_info('::: [END] Подписано: {count}/{len}, осталось {delta}. :::'.format(count=count - 1,
                                                                                len=limit,
                                                                                delta=no_friends_count - (count - 1)))
