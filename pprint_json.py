import json


def load_data(filepath):
    f = open(filepath)
    js = json.load(f)
    return js


def pretty_print_json(data):
    print(data)


if __name__ == '__main__':
    pretty_print_json(load_data(input('Enter path: ')))