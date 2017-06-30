# coding=utf-8
import random

import time

from framework.support.commonFunctions import get_random_int, sleep
from framework.support.log import log_info
from project.api_call.friendsApi import FriendsApi
from project.api_call.likesApi import LikesApi


def is_profile_photo_liked(account_id, user):
    photo_id = user.photo_id.split('_')[1]
    return True if LikesApi(account_id).is_liked(user_id=user.user_id, item_id_obj=photo_id)[0] == 1 else False


def add_like_to_profile_photo(account_id, user):
    if not is_profile_photo_liked(account_id=account_id, user=user):
        photo_id = user.photo_id.split('_')[1]
        LikesApi(account_id).add(owner_id=user.user_id, item_id_obj=photo_id)
        return True
    return False


def likes_friends(account_id):
    friends = FriendsApi(account_id).get()
    likes_users_photo_account(account_id=account_id, users=friends)


def delete_users_without_photo(users):
    return [user for user in users if user.has_photo == 1]


def likes_users_photo_account(account_id, users):
    users = delete_users_without_photo(users)
    count_all_users_with_photo = len(users)
    log_info('Найдено {len} чел.'.format(len=len(users)))
    count = 1
    limit = get_random_int(70, 90)
    # limit = 1
    while count < limit and len(users) >= 1:
        random_index = random.randint(0, len(users) - 1)
        user = users.pop(random_index)
        log_info('[{random}/{all}] Пользователь: id{id}, {first_name} {last_name}.'.format(
            random=random_index,
            all=len(users),
            id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name))
        if add_like_to_profile_photo(account_id=account_id, user=user):
            random_seconds = get_random_int(300, 500)
            log_info('   {message}: {count}.'.format(message='Лайк',
                                                     count=count))
            sleep(random_seconds)
            count += 1
        else:
            log_info('  [skip] Пользователь уже имеет лайк к фото.')
            random_seconds = get_random_int(2, 5)
            sleep(random_seconds)
    log_info('::: [END] Лайкнуто: {count}/{len} :::'.format(count=count - 1,
                                                            len=count_all_users_with_photo))
