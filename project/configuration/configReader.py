import os

from framework.data_proc.jsonLib import parse_value_from_json_file


def parse_value_from_users_tokens():
    users_tokens_file = os.path.abspath(os.path.dirname(__file__)
                                        + '{sep}..{sep}configuration{sep}users_tokens.json'.format(sep=os.sep))
    return parse_value_from_json_file(users_tokens_file)
