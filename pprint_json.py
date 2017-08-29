import json


def load_data(filepath):
    raw_json_file = open(filepath)
    json_file = json.load(raw_json_file)
    return json_file


def pretty_print_json(json_data):
    print(json_data)


if __name__ == '__main__':
    pretty_print_json(load_data(input('Enter path: ')))