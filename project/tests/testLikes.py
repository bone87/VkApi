# coding=utf-8
import random
import time

from framework.support.commonFunctions import get_random_int
from framework.support.log import log_info
from project.api_call.friendsApi import FriendsApi
from project.steps.likesSteps import add_like_to_profile_photo
from project.steps.usersSteps import search_users_minsk, search_users_lesnoi

opera_account = '310582170'
ff_account = '291495044'


def likes_friends(account_id):
    friends = FriendsApi(account_id).get()
    count = 1
    for friend in friends:
        if friend.has_photo == 1:
            if add_like_to_profile_photo(account_id=account_id, user=friend):
                random_seconds = get_random_int(5, 20)
                print '{message}: {count}, задержка {seconds} s'.format(message='Лайк',
                                                                        count=count,
                                                                        seconds=random_seconds)
                time.sleep(random_seconds)
                count += 1
                if count >= 150:
                    break
            else:
                print '[SKIP] Пользователь: {id}, {first_name} {last_name} уже имеет лайк к фото.'.format(
                    id=friend.user_id,
                    first_name=friend.first_name,
                    last_name=friend.last_name)
                time.sleep(get_random_int(1, 3))
        else:
            print '[SKIP] Пользователь: {id}, {first_name} {last_name} не имеет фото.'.format(id=friend.user_id,
                                                                                              first_name=friend.first_name,
                                                                                              last_name=friend.last_name)
    print 'Лайкнуто: {count}/{len}'.format(count=count - 1,
                                           len=len(friends))


def likes_users(account_id):
    users = search_users_lesnoi(account_id=account_id)
    log_info('Найдено {len}'.format(len=len(users)))
    count = 1
    while count < 140 or len(users) <= 1:
        random_index = random.randint(0, len(users)-1)
        print random_index, len(users)
        user = users.pop(random_index)
        if user.has_photo == 1:
            if add_like_to_profile_photo(account_id=account_id, user=user):
                random_seconds = get_random_int(5, 20)
                print '[{random}] {message}: {count}, задержка {seconds} s'.format(random=random_index,
                                                                                   message='Лайк',
                                                                                   count=count,
                                                                                   seconds=random_seconds)
                time.sleep(random_seconds)
                count += 1
            else:
                print '[SKIP] Пользователь: {id}, {first_name} {last_name} уже имеет лайк к фото.'.format(
                    id=user.user_id,
                    first_name=user.first_name,
                    last_name=user.last_name)
                time.sleep(get_random_int(1, 3))
        else:
            print '[SKIP] Пользователь: {id}, {first_name} {last_name} не имеет фото.'.format(id=user.user_id,
                                                                                              first_name=user.first_name,
                                                                                              last_name=user.last_name)
    print 'Лайкнуто: {count}/{len}'.format(count=count - 1,
                                           len=len(users))


# likes_friends(ff_account)
likes_users(ff_account)


# list1 = list('spisok')
# print list1
# print list1.pop(2)
