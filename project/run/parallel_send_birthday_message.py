# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.abspath(os.path.join(path_to_here,
                                            '..{sep}tests{sep}send_birthday_message.robot'.format(sep=os.sep)))
path_to_output = os.path.abspath(os.path.join(path_to_here,
                                              '..{sep}..{sep}reports{sep}message{sep}tmp{sep}'.format(sep=os.sep)))

tests_list = [
    # 'vlc_375444106107_Minsk_offset_0',

    'life_375255100893_Minsk_offset_30',
    'mts_375292463065_Minsk_offset_60',
    'vlc_375299403419_Minsk_offset_90',
    'vlc_375445528788_Minsk_offset_120',
    'vlc_375447693824_Minsk_offset_150',
    'mts_375298462344_Minsk_offset_180',
    # 'mts_375298360265_Minsk_offset_210',
    'mts_375292025693_Minsk_offset_240',
    # 'mts_375298681142_Minsk_offset_270',
    'mts_375336610743_Minsk_offset_300',
    'mts_375298845346_Minsk_offset_330'
]
run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="send_birthday_message")
