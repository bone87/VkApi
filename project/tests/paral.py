# -*- coding: utf-8 -*-
import sys, time
from subprocess import Popen, list2cmdline
from robot import rebot

def exec_commands(cmds):
    ''' Exec commands in parallel
    '''
    if not cmds: return # empty list

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

path_to_test1 = 'C:/test_p1.txt'
path_to_test2 = 'C:/test_p2.txt'
commands = [
    ['c:/Python27/Scripts/pybot.bat', '--test', 'math_p1','--outputdir','c:/TMP','--output','test_set1_output.xml' ,'--report','test_set1_report.html','--log','test_set1_log.html',path_to_test1],
    ['c:/Python27/Scripts/pybot.bat', '--test', 'math_p2','--outputdir','c:/TMP','--output','test_set2_output.xml' ,'--report','test_set2_report.html','--log','test_set2_log.html',path_to_test2],
]
exec_commands(commands)
print "Merge test reports"
rebot('c:/TMP/test_set1_output.xml', 'c:/TMP/test_set2_output.xml', report='c:/TMP/common_report.html', log='c:/TMP/common_log.html',xunit='c:/TMP/xunit.xml')​