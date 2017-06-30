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
path_to_test1 = os.path.join(path_to_tests, 'send_birthday_message_even.robot')

commands = [
    [path_to_pybot,
     '--test', '375298462344_Minsk_offset_180',
     '--output', 'reports/message/tmp/output_375298462344_Minsk_offset_180.xml',
     '--report', 'reports/message/tmp/report_375298462344_Minsk_offset_180.html',
     '--log', 'reports/message/tmp/log_375298462344_Minsk_offset_180.html', path_to_test1],
    [path_to_pybot,
     '--test', '375298360265_Minsk_offset_210',
     '--output', 'reports/message/tmp/output_375298360265_Minsk_offset_210.xml',
     '--report', 'reports/message/tmp/report_375298360265_Minsk_offset_210.html',
     '--log', 'reports/message/tmp/log_375298360265_Minsk_offset_210.html', path_to_test1],
    [path_to_pybot,
     '--test', '375298681142_Minsk_offset_240',
     '--output', 'reports/message/tmp/output_375298681142_Minsk_offset_240.xml',
     '--report', 'reports/message/tmp/report_375298681142_Minsk_offset_240.html',
     '--log', 'reports/message/tmp/log_375298681142_Minsk_offset_240.html', path_to_test1],
    [path_to_pybot,
     '--test', '375447693824_Minsk_offset_270',
     '--output', 'reports/message/tmp/output_375447693824_Minsk_offset_270.xml',
     '--report', 'reports/message/tmp/report_375447693824_Minsk_offset_270.html',
     '--log', 'reports/message/tmp/log_375447693824_Minsk_offset_270.html', path_to_test1],
    [path_to_pybot,
     '--test', '375445528788_Minsk_offset_300',
     '--output', 'reports/message/tmp/output_375445528788_Minsk_offset_300.xml',
     '--report', 'reports/message/tmp/report_375445528788_Minsk_offset_300.html',
     '--log', 'reports/message/tmp/log_375445528788_Minsk_offset_300.html', path_to_test1],
    [path_to_pybot,
     '--test', '375336610743_Minsk_offset_330',
     '--output', 'reports/message/tmp/output_375336610743_Minsk_offset_330.xml',
     '--report', 'reports/message/tmp/report_375336610743_Minsk_offset_330.html',
     '--log', 'reports/message/tmp/log_375336610743_Minsk_offset_330.html', path_to_test1],
]
exec_commands(commands)
rebot(os.path.join(path_to_tests, 'reports/message/tmp/output_375298462344_Minsk_offset_180.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375298360265_Minsk_offset_210.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375298681142_Minsk_offset_240.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375447693824_Minsk_offset_270.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375445528788_Minsk_offset_300.xml'),
      os.path.join(path_to_tests, 'reports/message/tmp/output_375336610743_Minsk_offset_330.xml'),
      report=os.path.join(path_to_tests, 'reports/message/report_{pref_data}_send_birthday_even.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))),
      log=os.path.join(path_to_tests, 'reports/message/log_{pref_data}_send_birthday_even.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))),
      xunit=os.path.join(path_to_tests, 'reports/message/robotxunit_{pref_data}_birthday_message_even.xml').format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d")))
