# coding=utf-8
import uuid
from random import randint
import time
import datetime

from framework.support.log import log_info


def get_unique_string(length=8):
    """
    Generate unique string with a specific length (max 32 symbols)
    """
    return uuid.uuid4().hex[:length]


def get_random_int(lower=0, upper=100):
    """
    Generate int in range [lower, upper]
    """
    random_int = randint(lower, upper)
    # log_info('   Сгенерировано число: {random}.'.format(random=random_int))
    return random_int


def sleep(seconds):
    log_info('   Задержка {minutes:.1f} min.'.format(minutes=float(seconds)/60))
    time.sleep(seconds)


def get_ten_weeks_before_date(start=datetime.datetime.today()):
    ten_weeks = datetime.timedelta(weeks=5)
    before_ten_weeks = start - ten_weeks
    return before_ten_weeks


def convert_date_to_unix_time_stamp(date_value=get_ten_weeks_before_date()):
    return time.mktime(date_value.timetuple())
