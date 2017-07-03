# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_tests = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.join(path_to_tests, 'send_birthday_message.robot')
path_to_output = os.path.join(path_to_tests, 'reports{sep}message{sep}tmp{sep}'.format(sep=os.sep))

tests_list = ['375298462344_Minsk_offset_0',
              '375298360265_Minsk_offset_30',
              '375298681142_Minsk_offset_60',
              '375447693824_Minsk_offset_90',
              '375445528788_Minsk_offset_120',
              '375336610743_Minsk_offset_150',
              '375292025693_Minsk_offset_180']

run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="send_birthday_message")
