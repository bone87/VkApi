# coding=utf-8
from project.steps.likesSteps import likes_users_photo_account
from project.steps.usersSteps import search_users_minsk, search_users_lesnoi, search_users_borovl

opera_account = '310582170'
ff_account = '291495044'
# black = id78641892

# users_minsk = search_users_minsk(account_id=opera_account)
# users_borov = search_users_borovl(account_id=opera_account)
users_les = search_users_lesnoi(account_id=ff_account)
# print len(users_les)
# users_with_photo = delete_users_without_photo(users_les)
# print len(users_with_photo)
# likes_friends(ff_account)
likes_users_photo_account(account_id=ff_account, users=users_les)
