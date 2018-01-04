from time import sleep


from framework.support.log import log_step
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users

numbers_tokens = [
    # {"25 7214755": "f325c6364f158a6c2b21a1e9272c605dfb167171369f3390d065dfc247f7a607f903af0b7e3511a538f19"},
    {"25 9071166": "340b0643780bd0c3f5b69e2442136a6fbecdbbebfaf50d0a191125f0a4ad4a464513737d4ae0fd03b26e7"}
]


def run_sender(age_from, age_to, max_count=20, time_to_sleep=300):
    offset = 0
    for item in numbers_tokens:
        number = item.keys()[0]
        token = item.values()[0]
        log_step(number)
        users = search_birthday_users(token=token, offset=offset, age_from=age_from, age_to=age_to)
        send_birthday_messages(token=token, users=users, max_count=max_count)
        offset = offset + 30
        sleep(time_to_sleep)
