# coding=utf-8
from time import sleep

from framework.support.commonFunctions import get_random_int
from framework.support.log import log_step, log_info
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users

numbers_tokens = [
    ["25 7214755", "a3383acc5f71ac8b6b0e88184f10b0084625ab832f84f3e72fb20e6e858b1c2b11f9f98ffca7e011bd398", get_random_int(10, 15)],
    ["25 9071166", "340b0643780bd0c3f5b69e2442136a6fbecdbbebfaf50d0a191125f0a4ad4a464513737d4ae0fd03b26e7", get_random_int(7, 15)],
    ["25 9065400", "f041569b15d8fb4dbd6d8075e25aea4dd23ce24def7f2a2adf21993a2a4bae41d336fbaa0da3866833e8f", get_random_int(7, 15)],
    ["25 9062961", "ed9694b71bcd0a51d2c907fb0ef2163a4d99201ffa0c2a0287ea5a18c2cc44580a2731ba2e26e9018ea5f", get_random_int(7, 15)],
    ["25 9068942", "ccae722d41b078eea221ba7364c0aa47f4cc7f727a5d3e82f5261ca6764f4b49088e2238ff6122addf73c", get_random_int(7, 15)],
    ["25 9056798", "7ceb6dc02053c584513027d790b960fa5ef9581c6d11a7a54bbb9f3fb2e8ad590dff1c67234cf63b5a09b", get_random_int(7, 15)],
    ["25 7632584", "998aac3cf32cbf901a98720e7091839c6b708fd95535bb52b4c2ad55ad3c83278b194d59bd7b247056631", get_random_int(7, 15)],
    ["25 7596046", "3e78124b5b34bfae2791945dc750f0c942df217d2750b96843158d11f01f61350c8925755c3e72ab966d1", get_random_int(7, 15)],
    ["25 7578000", "cf14583ea9f67746d39ae41e202dfe981195cdf7cb192a24b56230361ca5b468b1b896d9ec3d71e2137b2", get_random_int(7, 15)],
    ["25 7544404", "3e847e01dfc92e5d490e3d2773799f11ddc370d13e72b8f8ef0e1dbeaff8e34d7b69a4855bc225cdbd680", get_random_int(7, 15)],
    ["25 7512198", "7e5c37575bbd495ea9b287f0572a22e067311ef7436edc436cdee828f33b3173ea89626736ca344532e02", get_random_int(7, 15)],
    ["25 7311641", "728de0d39c92ddec5d292956e0c3152a4abbebd6111b4858b0469a110f470fe60b2426b05faae3dcdcf26", get_random_int(5, 9)],
    ["25 7351050", "b11dcee35fbbf091e5f1a31e6bcb38fbbea8ca77c2119226d126ad3881e5052bd7232cf46335c761cbd1e", get_random_int(5, 9)],
    ["25 7369155", "e1e44e192a795f1127a9cb9c50ee8dea291fbb56675e64392c1a9a838d4e5e970f8e4798f54cbb09b0168", get_random_int(5, 9)]
]


def run_sender(age_from, age_to):
    sec = get_random_int(60, 5000)
    log_info('Задержка: {min}min {sec}s.'.format(min=sec//60, sec=sec % 60))
    sleep(sec)
    offset = 0
    for item in numbers_tokens:
        log_step(item[0])
        log_info('Смещение: {offset}.'.format(offset=offset))
        users = search_birthday_users(token=item[1], offset=offset, age_from=age_from, age_to=age_to)
        send_birthday_messages(token=item[1], users=users, max_count=item[2])
        offset = offset + 30
        sec = get_random_int(60, 500)
        log_info('Задержка перед сменой номера: {min}min {sec}s.'.format(min=sec // 60, sec=sec % 60))
        sleep(sec)
