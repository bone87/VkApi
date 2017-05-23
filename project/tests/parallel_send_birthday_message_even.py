# -*- coding: utf-8 -*-
import time
from subprocess import Popen, list2cmdline

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


path_to_test1 = '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/send_birthday_message.robot'
commands = [
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
        '--test', '+375298681142_Minsk_28',
        '--output', 'output_375298681142_Minsk_28.xml',
        '--report', 'report_375298681142_Minsk_28.html',
        '--log', 'log_375298681142_Minsk_28.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
        '--test', '+375447693824_Minsk_29',
        '--output', 'output_375447693824_Minsk_29.xml',
        '--report', 'report_375447693824_Minsk_29.html',
        '--log', 'log_375447693824_Minsk_29.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
        '--test', '+375298462344_Minsk_32',
        '--output', 'output_375298462344_Minsk_32.xml',
        '--report', 'report_375298462344_Minsk_32.html',
        '--log', 'log_375298462344_Minsk_32.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
        '--test', '+375298360265_Minsk_33',
        '--output', 'output_375298360265_Minsk_33.xml',
        '--report', 'report_375298360265_Minsk_33.html',
        '--log', 'log_375298360265_Minsk_33.html', path_to_test1],
]
exec_commands(commands)
print "Merge test reports"
rebot('/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/output_'
      '375298462344_Minsk_32.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/output_'
      '375298360265_Minsk_33.xml',
      '375298681142_Minsk_28.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/output_'
      '375447693824_Minsk_29.xml',
      report='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message'
             '/report_send_birthday_message_evening.html',
      log='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message'
          '/log_send_birthday_message_evening.html',
      xunit='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message/robotxunit.xml')
