# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.abspath(os.path.join(path_to_here,
                                            '..{sep}tests{sep}send_birthday_message_even.robot'.format(sep=os.sep)))
path_to_output = os.path.abspath(os.path.join(path_to_here,
                                              '..{sep}..{sep}reports{sep}message{sep}tmp{sep}'.format(sep=os.sep)))

tests_list = ['375298462344_Minsk_offset_240',
              '375298360265_Minsk_offset_270',
              '375298681142_Minsk_offset_300',
              '375447693824_Minsk_offset_330',
              '375445528788_Minsk_offset_360',
              '375336610743_Minsk_offset_390',
              '375292025693_Minsk_offset_420']
#               ',
#               'DRON_Mama_Minsk_offset_450']

run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="send_birthday_message_even")
