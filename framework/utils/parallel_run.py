# -*- coding: utf-8 -*-
import os
import time
from subprocess import Popen, list2cmdline
import sys


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


def generate_commands(tests, path_to_pybot, path_to_output, path_to_tests):
    commands = []
    for test in tests:
        commands.append([path_to_pybot,
                         '--test',
                         str(test),
                         '--output',
                         os.path.join(path_to_output, 'output_{test_name}.xml'.format(test_name=test)),
                         path_to_tests])
    return commands

path_to_pybot_unix = '/home/ITRANSITION.CORP/e.bondarenko/.local/bin/pybot'
path_to_pybot_win = 'c:/Python27/Scripts/pybot.bat'
if sys.platform == 'win32':
    path_to_pybot = path_to_pybot_win
else:
    path_to_pybot = path_to_pybot_unix
