# coding=utf-8
import time
import datetime

from framework.support.commonFunctions import convert_date_to_unix_time_stamp
from project.api_call.friendsApi import FriendsApi
from project.api_call.usersApi import UsersApi


def print_no_friends(user_id, users_list):
    no_friends = 0
    size = len(users_list)
    for k in range(size):
        friends_status = FriendsApi(user_id).are_friends(users_list[k].user_id)
        print '{num}/{from_num}: {first_name} {last_name}: {status}'.format(num=k,
                                                                            from_num=size,
                                                                            first_name=users_list[k].first_name,
                                                                            last_name=users_list[k].last_name,
                                                                            status=friends_status)
        if friends_status == 0:
            no_friends += 1
        time.sleep(0.3)

    print '{friends}/{all}'.format(friends=no_friends,
                                   all=len(users_list))


def detete_more_10_weeks_last_seen_users(users):
    return [user for user in users if user.last_seen >= convert_date_to_unix_time_stamp()]


def search_birthday_users(account_id,
                          count=30,
                          offset=0,
                          status=None,
                          city=282,
                          sex=1,
                          age_from=19,
                          age_to=49,
                          timedelta=0):
    date = datetime.datetime.now() + datetime.timedelta(days=int(timedelta))
    day_now = date.day
    month_now = date.month
    users = UsersApi(account_id).search(count=count,
                                        offset=offset,
                                        status=status,
                                        city=city,
                                        sex=sex,
                                        age_from=age_from,
                                        age_to=age_to,
                                        birth_day=day_now,
                                        birth_month=month_now)
    # for user in users:
    #     print user
    return users


def search_users_minsk(account_id, count=1000, offset=0, status=None, age_from=19, age_to=49):
    return UsersApi(account_id).search(count=count,
                                       offset=offset,
                                       city=282,
                                       sex=1,
                                       status=status,
                                       age_from=age_from,
                                       age_to=age_to)


def search_users_borovl(account_id):
    return UsersApi(account_id).search(count=1000,
                                       city=2017,
                                       sex=1,
                                       age_from=19,
                                       age_to=49)


def search_users_lesnoi(account_id):
    return UsersApi(account_id).search(count=1000,
                                       city=1517622,
                                       sex=1,
                                       age_from=19,
                                       age_to=49)


def get_user_by_id(account_id, user_id):
    return UsersApi(account_id).get(user_id)
