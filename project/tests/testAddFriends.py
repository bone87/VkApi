# coding=utf-8
import time

from framework.support.commonFunctions import get_random_int
from project.steps.friendsSteps import add_quickly
from project.steps.usersSteps import search_users_borovl, search_users_lesnoi

# 282 - Minsk
# 649 - Grodno
# 2017 - Borovlyany
# 1517622 - Lesnoi

minsk_id = 2017
opera_account = '310582170'
ff_account = '291495044'


def add_friends(account_id):
    users = search_users_lesnoi(account_id)
    users_no_friends = [user for user in users if user.friend_status == 0]
    no_friends_count = len(users_no_friends)
    limit = get_random_int(30, 40)
    print 'Найдено {len}/{all} чел.'.format(len=no_friends_count,
                                            all=len(users))
    count = 1

    for user in users_no_friends:
        if add_quickly(account_id=account_id, user_model=user) == 1:
            random_seconds = get_random_int(300, 500)
            print '{message}: {count}, задержка {minutes:.2f} min'.format(message='Подписано',
                                                                          count=count,
                                                                          minutes=float(random_seconds) / 60)
            time.sleep(random_seconds)
            count += 1
            if count >= limit:
                break
    print 'Подписано: {count}/{len}'.format(count=count - 1,
                                            len=no_friends_count)


add_friends(opera_account)
