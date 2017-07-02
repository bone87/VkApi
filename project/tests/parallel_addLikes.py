# -*- coding: utf-8 -*-
import os
import datetime
from robot import rebot
from framework.utils.email_sender import send_email_with_attach
from framework.utils.parallel_run import *


path_to_tests = os.path.abspath(os.path.dirname(__file__))
path_to_test1 = os.path.join(path_to_tests, 'add_likes.robot')
path_to_output = os.path.join(path_to_tests, 'reports{sep}likes{sep}tmp{sep}'.format(sep=os.sep))

# commands = [
#     [path_to_pybot,
#      '--test', '375298681142_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375298681142_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', '375447693824_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375447693824_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', '375298462344_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375298462344_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', '375298360265_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375298360265_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', '375445528788_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375445528788_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', '375292025693_Minsk_likes',
#      '--output', os.path.join(path_to_output, 'output_375292025693_Minsk_likes.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', 'Bone_Minsk_likes_engaged',
#      '--output', os.path.join(path_to_output, 'output_Bone_Minsk_likes_engaged.xml'),
#      path_to_test1],
#
#     [path_to_pybot,
#      '--test', 'Prichello_Minsk_likes_engaged',
#      '--output', os.path.join(path_to_output, 'output_Prichello_Minsk_likes_engaged.xml'),
#      path_to_test1]
# ]
commands = generate_commands(tests=['375298681142_Minsk_likes',
                                    '375447693824_Minsk_likes',
                                    '375298462344_Minsk_likes',
                                    '375298360265_Minsk_likes',
                                    '375445528788_Minsk_likes',
                                    '375292025693_Minsk_likes',
                                    'Bone_Minsk_likes_engaged',
                                    'Prichello_Minsk_likes_engaged',
                                    ],
                             path_to_pybot=path_to_pybot,
                             path_to_output=path_to_output,
                             path_to_tests=path_to_test1)

exec_commands(commands)
rebot(os.path.join(path_to_output, 'output_375298681142_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_375447693824_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_375298462344_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_375298360265_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_375445528788_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_375292025693_Minsk_likes.xml'),
      os.path.join(path_to_output, 'output_Bone_Minsk_likes_engaged.xml'),
      os.path.join(path_to_output, 'output_Prichello_Minsk_likes_engaged.xml'),
      log=os.path.join(path_to_output, '..{sep}log_{pref_data}_add_likes.html'.format(
          sep=os.sep,
          pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))))

send_email_with_attach("add_likes",
                       os.path.join(path_to_output, '..{sep}log_{pref_data}_add_likes.html'.format(
                           sep=os.sep,
                           pref_data=datetime.datetime.now().strftime("%Y-%m-%d"))))
