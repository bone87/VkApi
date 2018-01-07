from time import sleep


from framework.support.log import log_step
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users

numbers_tokens = [
    ["25 7214755", "a3383acc5f71ac8b6b0e88184f10b0084625ab832f84f3e72fb20e6e858b1c2b11f9f98ffca7e011bd398", 10],
    ["25 9071166", "340b0643780bd0c3f5b69e2442136a6fbecdbbebfaf50d0a191125f0a4ad4a464513737d4ae0fd03b26e7", 10],
    ["25 9065400", "f041569b15d8fb4dbd6d8075e25aea4dd23ce24def7f2a2adf21993a2a4bae41d336fbaa0da3866833e8f", 10],
    ["25 9062961", "249e99f5fd6bc66baabc11d4349576fa762e1c20cba284ae1215c54204e045b52cd760e1ed37a4459eaa3", 10]
    # ["25 9068942", "ccae722d41b078eea221ba7364c0aa47f4cc7f727a5d3e82f5261ca6764f4b49088e2238ff6122addf73c", 10],
]


def run_sender(age_from, age_to, time_to_sleep=300):
    offset = 0
    for item in numbers_tokens:
        log_step(item[0])
        users = search_birthday_users(token=item[1], offset=offset, age_from=age_from, age_to=age_to)
        send_birthday_messages(token=item[1], users=users, max_count=item[2])
        offset = offset + 30
        sleep(time_to_sleep)
