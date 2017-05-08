import json


def get_pretty(json_message):
    return json.dumps(json_message, sort_keys=True, indent=4, ensure_ascii=False)


def parse_value_from_json_file(path_to_file):
    """
    parse Json file
    :param path_to_file: Path to json file
    :return: data from json file
    """
    with open(path_to_file, "r") as json_file:
        return json.load(json_file)


def get_value_from_json(json_str, key):
    try:
        value_json = json_str[key]
        return value_json
    except KeyError:
        raise KeyError(json_str)
