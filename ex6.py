#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import yaml
import json


def main ():
    yaml_file = 'ex6_test.yml'
    json_file = 'ex6_test.json'

    my_dict = {
        'ip_addr': '1.1.1.1',
        'platform': 'cisco_ios',
        'vendor': 'cisco',
        'model': '2800'
    }

    my_list = [
        'some string',
        99,
        100,
        my_dict,
        'test1',
        'test2'
    ]

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)


if __name__ == "__main__":
    main()
