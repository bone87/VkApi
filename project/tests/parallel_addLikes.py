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


path_to_test1 = '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/add_likes.robot'
commands = [
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
     '--test', '375298462344_Minsk_likes',
     '--output', 'output_375298462344_Minsk_likes.xml',
     '--report', 'report_375298462344_Minsk_likes.html',
     '--log', 'log_375298462344_Minsk_likes.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
     '--test', '375298360265_Minsk_likes',
     '--output', 'output_375298360265_Minsk_likes.xml',
     '--report', 'report_375298360265_Minsk_likes.html',
     '--log', 'log_375298360265_Minsk_likes.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
     '--test', 'Bone_Minsk_likes_engaged',
     '--output', 'output_Bone_Minsk_likes_engaged.xml',
     '--report', 'report_Bone_Minsk_likes_engaged.html',
     '--log', 'log_Bone_Minsk_likes_engaged.html', path_to_test1],
    ['/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot',
     '--test', 'Prichello_Minsk_likes_engaged',
     '--output', 'output_Prichello_Minsk_likes_engaged.xml',
     '--report', 'report_Prichello_Minsk_likes_engaged.html',
     '--log', 'log_Prichello_Minsk_likes_engaged.html', path_to_test1]
]
exec_commands(commands)
print "Merge test reports"
rebot('/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/'
      'output_375298462344_Minsk_likes.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/'
      'output_375298360265_Minsk_likes.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/'
      'output_Bone_Minsk_likes_engaged.xml',
      '/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/'
      'output_Prichello_Minsk_likes_engaged.xml',
      report='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes'
             '/report_add_likes.html',
      log='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes'
          '/log_add_likes.html',
      xunit='/home/ITRANSITION.CORP/e.bondarenko/My_projects/VkApi/project/tests/reports/likes/robotxunit.xml')
