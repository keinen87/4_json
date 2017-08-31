import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r') as raw_json_file:
        return json.load(raw_json_file)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        source_json = load_data(filepath)
        pretty_print_json(source_json)
    else:
        print("Error! Enter path!")