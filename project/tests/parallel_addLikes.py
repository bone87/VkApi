# -*- coding: utf-8 -*-
import os
import shutil
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

# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports{sep}likes{sep}tmp'.format(sep=os.sep))
# if os.path.exists(path):
#     shutil.rmtree(path)

path_to_pybot_unix = '/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot'
path_to_pybot_win = 'c:/Python27/Scripts/pybot.bat'
if sys.platform == 'win32':
    path_to_pybot = path_to_pybot_win
else:
    path_to_pybot = path_to_pybot_unix
path_to_tests = os.path.abspath(os.path.dirname(__file__))
path_to_test1 = os.path.join(path_to_tests, 'add_likes.robot')


commands = [
    [path_to_pybot,
     '--test',      '375298681142_Minsk_likes',
     '--output',    'reports/likes/tmp/output_375298681142_Minsk_likes.xml',
     '--report',    'reports/likes/tmp/report_375298681142_Minsk_likes.html',
     '--log',       'reports/likes/tmp/log_375298681142_Minsk_likes.html', path_to_test1],
    [path_to_pybot,
     '--test',      '375447693824_Minsk_likes',
     '--output',    'reports/likes/tmp/output_375447693824_Minsk_likes.xml',
     '--report',    'reports/likes/tmp/report_375447693824_Minsk_likes.html',
     '--log',       'reports/likes/tmp/log_375447693824_Minsk_likes.html', path_to_test1],
    [path_to_pybot,
     '--test',      '375298462344_Minsk_likes',
     '--output',    'reports/likes/tmp/output_375298462344_Minsk_likes.xml',
     '--report',    'reports/likes/tmp/report_375298462344_Minsk_likes.html',
     '--log',       'reports/likes/tmp/log_375298462344_Minsk_likes.html', path_to_test1],
    [path_to_pybot,
     '--test',      '375298360265_Minsk_likes',
     '--output',    'reports/likes/tmp/output_375298360265_Minsk_likes.xml',
     '--report',    'reports/likes/tmp/report_375298360265_Minsk_likes.html',
     '--log',       'reports/likes/tmp/log_375298360265_Minsk_likes.html', path_to_test1],
    [path_to_pybot,
     '--test',      '375445528788_Minsk_likes',
     '--output',    'reports/likes/tmp/output_375445528788_Minsk_likes.xml',
     '--report',    'reports/likes/tmp/report_375445528788_Minsk_likes.html',
     '--log',       'reports/likes/tmp/log_375445528788_Minsk_likes.html', path_to_test1],
    [path_to_pybot,
     '--test',      'Bone_Minsk_likes_engaged',
     '--output',    'reports/likes/tmp/output_Bone_Minsk_likes_engaged.xml',
     '--report',    'reports/likes/tmp/report_Bone_Minsk_likes_engaged.html',
     '--log',       'reports/likes/tmp/log_Bone_Minsk_likes_engaged.html', path_to_test1],
    [path_to_pybot,
     '--test',      'Prichello_Minsk_likes_engaged',
     '--output',    'reports/likes/tmp/output_Prichello_Minsk_likes_engaged.xml',
     '--report',    'reports/likes/tmp/report_Prichello_Minsk_likes_engaged.html',
     '--log',       'reports/likes/tmp/log_Prichello_Minsk_likes_engaged.html', path_to_test1]
]
exec_commands(commands)
rebot('c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_375298681142_Minsk_likes.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_375447693824_Minsk_likes.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_375298462344_Minsk_likes.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_375298360265_Minsk_likes.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_375445528788_Minsk_likes.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_Bone_Minsk_likes_engaged.xml',
      'c:/TeamCity/buildAgent/work/c5b3fb5b1ac0d88e/reports/likes/tmp/output_Prichello_Minsk_likes_engaged.xml',
      report=os.path.join(path_to_tests, 'reports/likes/report_{pref_data}_add_likes.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))),
      log=os.path.join(path_to_tests, 'reports/likes/log_{pref_data}_add_likes.html'.format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))),
      xunit=os.path.join(path_to_tests, 'reports/likes/robotxunit_{pref_data}_add_likes.xml').format(
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d")))
