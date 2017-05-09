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
    likes_users(account_id=account_id, users=friends)


def likes_users(account_id, users):
    log_info('Найдено {len}'.format(len=len(users)))
    count = 1
    limit = get_random_int(130, 140)
    while count < limit or len(users) <= 1:
        random_index = random.randint(0, len(users) - 1)
        print random_index, len(users)
        user = users.pop(random_index)
        if user.has_photo == 1:
            if add_like_to_profile_photo(account_id=account_id, user=user):
                random_seconds = get_random_int(150, 300)
                log_info('[{random}] {message}: {count}, задержка {minutes:.2f} min'
                         .format(random=random_index,
                                 message='Лайк',
                                 count=count,
                                 minutes=float(random_seconds) / 60))
                time.sleep(random_seconds)
                count += 1
            else:
                log_info('[SKIP] Пользователь: {id}, {first_name} {last_name} уже имеет лайк к фото.'.format(
                    id=user.user_id,
                    first_name=user.first_name,
                    last_name=user.last_name))
                time.sleep(get_random_int(2, 5))
        else:
            log_info('[SKIP] Пользователь: {id}, {first_name} {last_name} не имеет фото.'.
                     format(id=user.user_id,
                            first_name=user.first_name,
                            last_name=user.last_name))
    log_info('Лайкнуто: {count}/{len}'.format(count=count - 1,
                                              len=len(users)))


# users_minsk = search_users_minsk(account_id=opera_account)

users_borov = search_users_borovl(account_id=opera_account)
print len(users_borov)

# users_les = search_users_lesnoi(account_id=opera_account)

# likes_friends(ff_account)
# likes_users(account_id=ff_account, users=users_les)

# black = id78641892
# user = UsersApi(ff_account).get('12855014')
# print user
