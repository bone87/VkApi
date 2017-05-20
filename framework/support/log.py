# encoding=windows-1251
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import inspect
import json
import logging
import os
import datetime
import sys


def create_log_file():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__) + '/../../'), 'log/')
    now = datetime.datetime.now()
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = os.path.join(path, now.strftime("%Y-%m-%d") + ".log")
    return file_name


def config_log():
    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    log.addHandler(ch)
    # fh = handlers.RotatingFileHandler(create_log_file(), maxBytes=(1048576 * 5), backupCount=7)
    # fh.setFormatter(format)
    # log.addHandler(fh)
    return log


log = config_log()
template = '::[{file_name} => {module_name}]::'


def log_step(number, message):
    log.info("\n")
    log_info(":::::::::: {number}. {message} ::::::::::".format(number=number,
                                                                message=message))


def log_info(message):
    log.info('{template:<50} {message}'.format(template=template.format(module_name=inspect.stack()[1][3],
                                                                        file_name=os.path.split(inspect.stack()[1][1])[
                                                                            1]),
                                               message=message))


def log_pretty_json(json_message, message=None):
    log_info(message + '\n' + json.dumps(json_message, sort_keys=True, indent=4) + '\n')


def error(message):
    log.error(template.format(module_name=inspect.stack()[1][3],
                              file_name=os.path.split(inspect.stack()[1][1])[1],
                              message=message))


def end_log():
    log.info(":::::::::: END LOG ::::::::::")
    log.info("\n\n")
