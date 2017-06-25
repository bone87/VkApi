# -*- coding: utf-8 -*-
import os
import time
from subprocess import Popen, list2cmdline

import sys

import datetime
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
     '--test', '375298462344_Minsk_offset_0',
     '--output', 'reports/message/tmp/output_375298462344_Minsk_offset_0.xml',
     '--report', 'reports/message/tmp/report_375298462344_Minsk_offset_0.html',
     '--log', 'reports/message/tmp/log_375298462344_Minsk_offset_0.html', path_to_test1],
    [path_to_pybot,
     '--test', '375298360265_Minsk_offset_30',
     '--output', 'reports/message/tmp/output_375298360265_Minsk_offset_30.xml',
     '--report', 'reports/message/tmp/report_375298360265_Minsk_offset_30.html',
     '--log', 'reports/message/tmp/log_375298360265_Minsk_offset_30.html', path_to_test1],
    [path_to_pybot,
     '--test', '375298681142_Minsk_offset_60',
     '--output', 'reports/message/tmp/output_375298681142_Minsk_offset_60.xml',
     '--report', 'reports/message/tmp/report_375298681142_Minsk_offset_60.html',
     '--log', 'reports/message/tmp/log_375298681142_Minsk_offset_60.html', path_to_test1],
    [path_to_pybot,
     '--test', '375447693824_Minsk_offset_90',
     '--output', 'reports/message/tmp/output_375447693824_Minsk_offset_90.xml',
     '--report', 'reports/message/tmp/report_375447693824_Minsk_offset_90.html',
     '--log', 'reports/message/tmp/log_375447693824_Minsk_offset_90.html', path_to_test1],
    [path_to_pybot,
     '--test', '375445528788_Minsk_offset_120',
     '--output', 'reports/message/tmp/output_375445528788_Minsk_offset_120.xml',
     '--report', 'reports/message/tmp/report_375445528788_Minsk_offset_120.html',
     '--log', 'reports/message/tmp/log_375445528788_Minsk_offset_120.html', path_to_test1],
]
exec_commands(commands)
rebot(os.path.join(path_to_tests, 'reports/message/tmp/output_375298462344_Minsk_offset_0.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375298360265_Minsk_offset_30.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375298681142_Minsk_offset_60.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375447693824_Minsk_offset_90.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375445528788_Minsk_offset_120.xml'),
      report=os.path.join(path_to_tests, 'reports/message/report_{pref_data}_send_birthday.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d_%H-%m-%S"))),
      log=os.path.join(path_to_tests, 'reports/message/log_{pref_data}_send_birthday.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d_%H-%m-%S"))),
      xunit=os.path.join(path_to_tests, 'reports/message/robotxunit_{pref_data}_birthday_message.xml'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d_%H-%m-%S"))))
