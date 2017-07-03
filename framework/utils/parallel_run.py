# -*- coding: utf-8 -*-
import os
import time
from subprocess import Popen, list2cmdline
import sys

import datetime
from robot import rebot

from framework.utils.email_sender import send_email_with_attach


def get_path_to_pybot():
    path_to_pybot_unix = '/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot'
    path_to_pybot_win = 'c:/Python27/Scripts/pybot.bat'
    if sys.platform == 'win32':
        return path_to_pybot_win
    else:
        return path_to_pybot_unix


def exec_commands(cmds):
    """ Exec commands in parallel
    """
    if not cmds:
        return

    def done(p):
        return p.poll() is not None

    processes = []
    while True:
        while cmds:
            task = cmds.pop()
            print list2cmdline(task)
            processes.append(Popen(task))
        for p in processes:
            if done(p):
                processes.remove(p)
        if not processes and not cmds:
            break
        else:
            time.sleep(0.05)


def generate_commands(tests, path_to_test, path_to_output, path_to_pybot=get_path_to_pybot()):
    return [[path_to_pybot,
             '--test', test,
             '--name', test,
             '--output', os.path.join(path_to_output, 'output_{test_name}.xml'.format(test_name=test)),
             '--report', os.path.join(path_to_output, 'report_{test_name}.html'.format(test_name=test)),
             '--log', os.path.join(path_to_output, 'log_{test_name}.html'.format(test_name=test)),
             path_to_test]
            for test in tests]


def run_rebot(path_to_output, action_name, *tests):
    list = [os.path.join(path_to_output, 'output_{test_name}.xml'.format(test_name=test_name)) for test_name in tests]
    log = os.path.abspath(os.path.join(path_to_output, '..{sep}log_{pref_data}_{action}.html'.format(
        sep=os.sep,
        action=action_name,
        pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))))

    report = os.path.abspath(os.path.join(path_to_output, '..{sep}report.html'.format(sep=os.sep)))
    rebot(*list,
          log=log,
          report=report,
          name=str(action_name).upper())


def run_and_mail(tests, path_to_test, path_to_output, action):
    commands = generate_commands(tests=tests,
                                 path_to_test=path_to_test,
                                 path_to_output=path_to_output)
    exec_commands(commands)
    run_rebot(path_to_output,
              action,
              *tests)
    send_email_with_attach(action,
                           os.path.abspath(os.path.join(path_to_output, '..{sep}log_{pref_data}_{action}.html'.format(
                               sep=os.sep,
                               action=action,
                               pref_data=datetime.datetime.now().strftime("%Y-%m-%d")))))
