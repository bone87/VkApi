# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.abspath(os.path.join(path_to_here,
                                            '..{sep}tests{sep}add_likes.robot'.format(sep=os.sep)))
path_to_output = os.path.abspath(os.path.join(path_to_here,
                                              '..{sep}..{sep}reports{sep}likes{sep}tmp{sep}'.format(sep=os.sep)))

tests_list = [
    # 'vlc_375444106107_Minsk_likes',
    # 'vlc_375444106104_Minsk_likes',
    # 'vlc_375299403425_Minsk_likes',
    # 'vlc_375299403419_Minsk_likes',
    # 'vlc_375445528788_Minsk_likes',
    # 'vlc_375447693824_Minsk_likes',
    # 'mts_375298462344_Minsk_likes',
    # 'mts_375298360265_Minsk_likes',
    # 'mts_375292025693_Minsk_likes',
    # 'mts_375298681142_Minsk_likes',
    # 'mts_375336610743_Minsk_likes',
    # 'mts_375298845346_Minsk_likes',
    # 'Bone_Minsk_likes_engaged',
    # 'Prichello_Minsk_likes_engaged'

    'mts_375292463065_Minsk_likes',
    'life_375255100893_Minsk_likes'

]

run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="add_likes")
