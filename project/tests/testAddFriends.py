# coding=utf-8
import time

from project.steps.friendsSteps import add_quickly, add_friends
from project.steps.usersSteps import search_users_borovl, search_users_lesnoi, search_users_minsk

# 282 - Minsk
# 649 - Grodno
# 2017 - Borovlyany
# 1517622 - Lesnoi

opera_account = '310582170'
ff_account = '291495044'
# black = id78641892

users_minsk = search_users_minsk(account_id=opera_account, count=100, age_from=25, age_to=25)
# users_borov = search_users_borovl(account_id=opera_account)
# users_les = search_users_lesnoi(account_id=ff_account)
add_friends(opera_account, users_minsk)
