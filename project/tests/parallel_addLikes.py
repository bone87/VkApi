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


path_to_test1 = '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/addLikesMinskFirefox.robot'
path_to_test2 = '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/addLikesMinskOpera.robot'
commands = [
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot', '--test', 'Test title', '--outputdir', 'reports/likes', '--output',
     'test_set1_output.xml', '--report', 'test_set1_report.html', '--log', 'test_set1_log.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot', '--test', 'Test title', '--outputdir', 'reports/likes', '--output',
     'test_set2_output.xml', '--report', 'test_set2_report.html', '--log', 'test_set2_log.html', path_to_test2],
]
exec_commands(commands)
print "Merge test reports"
rebot('/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/test_set1_output.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/test_set2_output.xml',
      report='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/common_report.html',
      log='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/common_log.html',
      xunit='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/robotxunit.xml')
