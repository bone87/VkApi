# -*- coding: utf-8 -*-
from framework.utils.parallel_run import *

path_to_here = os.path.abspath(os.path.dirname(__file__))
path_to_test = os.path.abspath(os.path.join(path_to_here,
                                            '..{sep}tests{sep}add_likes.robot'.format(sep=os.sep)))
path_to_output = os.path.abspath(os.path.join(path_to_here,
                                              '..{sep}..{sep}reports{sep}likes{sep}tmp{sep}'.format(sep=os.sep)))

tests_list = [
    '375298681142_Minsk_likes',
    '375447693824_Minsk_likes',
    '375298462344_Minsk_likes',
    '375298360265_Minsk_likes',
    '375445528788_Minsk_likes',
    '375292025693_Minsk_likes',
    # 'DRON_Mama_Minsk_likes',
    'Bone_Minsk_likes_engaged',
    'Prichello_Minsk_likes_engaged'
]

run_and_mail(tests=tests_list,
             path_to_test=path_to_test,
             path_to_output=path_to_output,
             action="add_likes")
