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
        '--test', '+375298462344_Minsk_25',
        '--outputdir', 'reports/message',
        '--output', 'output_+375298462344_Minsk_25.xml',
        '--report', 'report_+375298462344_Minsk_25.html',
        '--log', 'log_+375298462344_Minsk_25.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
        '--test', '+375298360265_Minsk_26',
        '--outputdir', 'reports/message',
        '--output', 'output_+375298360265_Minsk_26.xml',
        '--report', 'report_+375298360265_Minsk_26.html',
        '--log', 'log_+375298360265_Minsk_26.html', path_to_test1],
]
exec_commands(commands)
print "Merge test reports"
rebot('/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message/output_'
      '+375298462344_Minsk_25.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message/output_'
      '+375298360265_Minsk_26.xml',
      report='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message'
             '/report_send_birthdayMessage_morning.html',
      log='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message'
          '/log_send_birthdayMessage_morning.html',
      xunit='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/message/robotxunit.xml')
