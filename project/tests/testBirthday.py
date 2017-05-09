# coding=utf-8

# 282 - Minsk
# 649 - Grodno
# 2017 - Borovlyany
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users

minsk_id = 282
opera_account = '310582170'
ff_account = '291495044'

users = search_birthday_users(ff_account, age_from=20, age_to=20)
send_birthday_messages(ff_account, users)