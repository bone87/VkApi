# coding=utf-8
from project.api_call.friendsApi import FriendsApi


def add_user_to_friends_with_message(account_id, user_model, message=None):
    if FriendsApi(account_id).are_friends(user_model.user_id) == 0:
        status = FriendsApi(account_id).add(user_id=user_model.user_id,
                                            text='{first_name}, {message}'.format(first_name=user_model.first_name,
                                                                                  message=message))
        assert status == 1, 'Заявка на добавление пользователя {user_id} в друзья НЕ ОТПРАВЛЕНА!' \
            .format(user_id=user_model.user_id)
        return status


def add_quickly(account_id, user_model):
    status = FriendsApi(account_id).add(user_id=user_model.user_id)
    if status != 1:
        print 'Заявка на добавление пользователя {user_id} в друзья НЕ ОТПРАВЛЕНА!' \
            .format(user_id=user_model.user_id)
        return status
    else:
        if status == 1:
            print 'Пользователь: id{user_id}, {first_name} {last_name} добавлен в подписку.'.format(
                user_id=user_model.user_id,
                first_name=user_model.first_name,
                last_name=user_model.last_name)
            return status


def is_user_no_friend(account_id, user_model):
    if FriendsApi(account_id).are_friends(user_model.user_id) == 0:
        return True
    else:
        return False

# user = get('257706620')
# print user
# print is_user_no_friend(user)
