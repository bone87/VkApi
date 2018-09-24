# coding=utf-8

from time import sleep
from framework.support.commonFunctions import get_random_int
from framework.utils.email_sender import send_email_with_attach
from project.steps.messagesSteps import send_birthday_messages_sto325
from project.steps.usersSteps import search_birthday_users
from timeit import default_timer as timer
from framework.support.MyLogger import MyLogger

numbers_tokens = [
    ["29 6235325", "eed19b302144ead88c4e7c798689033343374bbbefc3c58986bf695642895a3ee1d1d37d35d88e451cf3d", get_random_int(10, 15)]

]

logger = MyLogger()


def run_sender(age_from, age_to):
    start = timer()
    # sec = get_random_int(60, 1000)
    # logger.log_info('Задержка: {min}min {sec}s.'.format(min=sec//60, sec=sec % 60))
    # sleep(sec)
    offset = 0
    count = 0
    status = 'PASS'
    message = ''
    try:
        for item in numbers_tokens:
            logger.log_step(item[0])
            logger.log_info('Смещение: {offset}.'.format(offset=offset))
            users = search_birthday_users(token=item[1], offset=offset, age_from=age_from, age_to=age_to, sex=2)
            send_count = send_birthday_messages_sto325(token=item[1], users=users, max_count=item[2])
            count = count + send_count
            offset = offset + 30
            sec = get_random_int(60, 200)
            logger.log_info('Задержка перед сменой номера: {min}min {sec}s.'.format(min=sec // 60, sec=sec % 60))
            sleep(sec)
        logger.log_info('')
        logger.log_info('Всего отправлено сообщений: {count}. Среднее значение: {mid}.'.format(count=count, mid=count/len(numbers_tokens)))
    except Exception as error:
        status = 'FAIL'
        logger.log_pretty_json(json_message=error.args)
        assert False
    finally:
        end = timer()
        duration_sec = end - start
        duration_min = duration_sec // 60
        sec_rest = duration_sec % 60
        duration_hours = duration_min // 60
        min_rest = duration_min % 60

        duration_str = '{hours}h {min}min {sec}s'.format(hours=int(duration_hours),
                                                         min=int(min_rest),
                                                         sec=int(sec_rest))
        message = 'Duration: {duration}\nCount: {count}'.format(duration=str(duration_str),
                                                                count=count) \
                  + message
        logger.__del__()
        attached_file = logger.file_name
        send_email_with_attach(message=message,
                               attached_file=attached_file,
                               subject='{status}. {count} messages.'.format(status=status,
                                                                            count=count))

run_sender(30, 50)
