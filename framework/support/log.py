import json
import logging
import os
import datetime


def create_log_file():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__) + '/../../'), 'test_project/log/')
    now = datetime.datetime.now()

    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    file_name = os.path.join(path, now.strftime("%Y-%m-%d_%H-%M") + ".log")
    return file_name


log = logging
log.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                level=logging.INFO,
                filename=create_log_file())


def log_step(number, message):
    log.info("\n")
    log.info(":::::::::: {number}. {message} ::::::::::".format(number=number,
                                                                message=message))


def log_info(message):
    log.info(message)


def log_pretty_json(json_message, message=None):
    log_info(message + '\n' + json.dumps(json_message, sort_keys=True, indent=4) + '\n')


def error(message):
    log.error(message)


def end_log():
    log.info(":::::::::: END LOG ::::::::::")
    log.info("\n\n")
