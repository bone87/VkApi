# -*- coding: utf-8 -*-
import os
import time
from subprocess import Popen, list2cmdline

import sys
from robot import rebot


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


path_to_pybot_unix = '/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot'
path_to_pybot_win = 'c:/Python27/Scripts/pybot.bat'
if sys.platform == 'win32':
    path_to_pybot = path_to_pybot_win
else:
    path_to_pybot = path_to_pybot_unix
path_to_tests = os.path.abspath(os.path.dirname(__file__))
path_to_test1 = os.path.join(path_to_tests, 'send_birthday_message.robot')

commands = [
    [path_to_pybot,
        '--test',       '375298462344_Minsk_mes_31',
        '--output',     'reports/message/tmp/output_375298462344_Minsk_mes_31.xml',
        '--report',     'reports/message/tmp/report_375298462344_Minsk_mes_31.html',
        '--log',        'reports/message/tmp/log_375298462344_Minsk_mes_31.html', path_to_test1],
    [path_to_pybot,
        '--test',       '375298360265_Minsk_mes_30',
        '--output',     'reports/message/tmp/output_375298360265_Minsk_mes_30.xml',
        '--report',     'reports/message/tmp/report_375298360265_Minsk_mes_30.html',
        '--log',        'reports/message/tmp/log_375298360265_Minsk_mes_30.html', path_to_test1],
    [path_to_pybot,
        '--test',       '375298681142_Minsk_mes_29',
        '--output',     'reports/message/tmp/output_375298681142_Minsk_mes_29.xml',
        '--report',     'reports/message/tmp/report_375298681142_Minsk_mes_29.html',
        '--log',        'reports/message/tmp/log_375298681142_Minsk_mes_29.html', path_to_test1],
    [path_to_pybot,
        '--test',       '375447693824_Minsk_mes_28',
        '--output',     'reports/message/tmp/output_375447693824_Minsk_mes_28.xml',
        '--report',     'reports/message/tmp/report_375447693824_Minsk_mes_28.html',
        '--log',        'reports/message/tmp/log_375447693824_Minsk_mes_28.html', path_to_test1],
    [path_to_pybot,
        '--test',       '375445528788_Minsk_mes_27',
        '--output',     'reports/message/tmp/output_375445528788_Minsk_mes_27.xml',
        '--report',     'reports/message/tmp/report_375445528788_Minsk_mes_27.html',
        '--log',        'reports/message/tmp/log_375445528788_Minsk_mes_27.html', path_to_test1],
]
exec_commands(commands)
rebot(os.path.join(path_to_tests,           'reports/message/tmp/output_375298462344_Minsk_mes_31.xml'),
      os.path.join(path_to_tests,           'reports/message/tmp/output_375298360265_Minsk_mes_30.xml'),
      os.path.join(path_to_tests,           'reports/message/tmp/output_375298681142_Minsk_mes_29.xml'),
      os.path.join(path_to_tests,           'reports/message/tmp/output_375447693824_Minsk_mes_28.xml'),
      os.path.join(path_to_tests,           'reports/message/tmp/output_375445528788_Minsk_mes_27.xml'),
      report=os.path.join(path_to_tests,    'reports/message/tmp/report_send_birthday_message.html'),
      log=os.path.join(path_to_tests,       'reports/message/tmp/log_send_birthday_message.html'),
      xunit=os.path.join(path_to_tests,     'reports/message/tmp/robotxunit.xml'))
