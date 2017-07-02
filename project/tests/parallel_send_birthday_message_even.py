# -*- coding: utf-8 -*-
import os
from framework.utils.parallel_run import *
import datetime
from robot import rebot
from framework.utils.email_sender import send_email_with_attach

path_to_tests = os.path.abspath(os.path.dirname(__file__))
path_to_test1 = os.path.join(path_to_tests, 'send_birthday_message_even.robot')
path_to_output = os.path.join(path_to_tests, 'reports{sep}message{sep}tmp{sep}'.format(sep=os.sep))

commands = [
    [path_to_pybot,
     '--test', '375298462344_Minsk_offset_210',
     '--output', os.path.join(path_to_output, 'output_375298462344_Minsk_offset_210.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375298360265_Minsk_offset_240',
     '--output', os.path.join(path_to_output, 'output_375298360265_Minsk_offset_240.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375298681142_Minsk_offset_270',
     '--output', os.path.join(path_to_output, 'output_375298681142_Minsk_offset_270.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375447693824_Minsk_offset_300',
     '--output', os.path.join(path_to_output, 'output_375447693824_Minsk_offset_300.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375445528788_Minsk_offset_330',
     '--output', os.path.join(path_to_output, 'output_375445528788_Minsk_offset_330.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375336610743_Minsk_offset_360',
     '--output', os.path.join(path_to_output, 'output_375336610743_Minsk_offset_360.xml'),
     path_to_test1],

    [path_to_pybot,
     '--test', '375292025693_Minsk_offset_390',
     '--output', os.path.join(path_to_output, 'output_375292025693_Minsk_offset_390.xml'),
     path_to_test1],
]
exec_commands(commands)
rebot(os.path.join(path_to_output, 'output_375298462344_Minsk_offset_210.xml'),
      os.path.join(path_to_output, 'output_375298360265_Minsk_offset_240.xml'),
      os.path.join(path_to_output, 'output_375298681142_Minsk_offset_270.xml'),
      os.path.join(path_to_output, 'output_375447693824_Minsk_offset_300.xml'),
      os.path.join(path_to_output, 'output_375445528788_Minsk_offset_330.xml'),
      os.path.join(path_to_output, 'output_375336610743_Minsk_offset_360.xml'),
      os.path.join(path_to_output, 'output_375292025693_Minsk_offset_390.xml'),
      log=os.path.join(path_to_output, '..{sep}log_{pref_data}_send_birthday_even.html'.format(
          sep=os.sep,
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))))
send_email_with_attach("send_birthday_message_even",
                       os.path.join(path_to_output, '..{sep}log_{pref_data}_send_birthday_even.html'.format(
                           sep=os.sep,
                           pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))))
