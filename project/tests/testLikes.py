# coding=utf-8
import random
import time

from framework.support.commonFunctions import get_random_int
from framework.support.log import log_info
from project.api_call.friendsApi import FriendsApi
from project.api_call.usersApi import UsersApi
from project.steps.likesSteps import add_like_to_profile_photo
from project.steps.usersSteps import search_users_minsk, search_users_lesnoi, search_users_borovl

opera_account = '310582170'
ff_account = '291495044'


def likes_friends(account_id):
    friends = FriendsApi(account_id).get()
    likes_users_photo_account(account_id=account_id, users=friends)


def delete_users_without_photo(users):
    return [user for user in users if user.has_photo == 1]


def likes_users_photo_account(account_id, users):
    users = delete_users_without_photo(users)
    count_all_users_with_photo = len(users)
    log_info('Найдено {len}'.format(len=len(users)))
    count = 1
    limit = get_random_int(130, 140)
    while count < limit or len(users) <= 2:
        random_index = random.randint(0, len(users) - 1)
        user = users.pop(random_index)
        log_info('[{random}/{all}] Пользователь: id{id}, {first_name} {last_name}: '.format(
            random=random_index,
            all=len(users),
            id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name))
        if add_like_to_profile_photo(account_id=account_id, user=user):
            random_seconds = get_random_int(150, 300)
            log_info('  {message}: {count}, задержка {minutes:.2f} min'
                     .format(message='лайк',
                             count=count,
                             minutes=float(random_seconds) / 60))
            time.sleep(random_seconds)
            count += 1
        else:
            log_info('  [skip] пользователь уже имеет лайк к фото.')
            random_seconds = get_random_int(2, 5)
            time.sleep(random_seconds)
            log_info('      задержка {seconds} sec.'.format(seconds=random_seconds))
    log_info('Лайкнуто: {count}/{len}'.format(count=count - 1,
                                              len=count_all_users_with_photo))


# users_minsk = search_users_minsk(account_id=opera_account)

# users_borov = search_users_borovl(account_id=opera_account)
# print len(users_borov)

users_les = search_users_lesnoi(account_id=opera_account)
# print len(users_les)
# users_with_photo = delete_users_without_photo(users_les)
# print len(users_with_photo)
# likes_friends(ff_account)
likes_users_photo_account(account_id=ff_account, users=users_les)

# black = id78641892
# user = UsersApi(ff_account).get('12855014')
# print user
