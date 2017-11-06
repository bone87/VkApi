# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.abspath(os.path.join(path_to_here,
                                            '..{sep}tests{sep}send_birthday_message.robot'.format(sep=os.sep)))
path_to_output = os.path.abspath(os.path.join(path_to_here,
                                              '..{sep}..{sep}reports{sep}message{sep}tmp{sep}'.format(sep=os.sep)))

tests_list = [
    # 'life_375255102578_Minsk_offset_0',
    # 'life_375255100893_Minsk_offset_30',
    # 'mts_375292463065_Minsk_offset_60',
    # 'vlc_375299403419_Minsk_offset_90',
    # 'life_375255220296_Minsk_offset_120',
    # 'vlc_375447693824_Minsk_offset_150',
    # 'mts_375298462344_Minsk_offset_180',
    # 'mts_375298360265_Minsk_offset_210',
    # 'life_375255145904_Minsk_offset_240',
    # 'life_375255157173_Minsk_offset_270',

    # 'life_375255218247_Minsk_offset_300',

    # 'life_375255174804_Minsk_offset_330',
    # 'life_375255095305_Minsk_offset_360',
    # 'life_375255092593_Minsk_offset_390',
    # 'life_375255092031_Minsk_offset_420',
    # 'life_375257214755_Minsk_offset_450',
    'life_375257246699_Minsk_offset_480'
]
run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="send_birthday_message")
