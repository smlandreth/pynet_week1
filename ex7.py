#!/usr/bin/env python
"""
write a script that reads the yaml and json files and pretty prints
the data that is returned in those files.
"""

from __future__ import unicode_literals, print_function
import yaml
import json
from pprint import pprint


def output_format(my_list, my_str):
    """make the output easier to read"""
    print('\n\n')
    print('#' * 3)
    print('#' * 3 + my_str)
    print('#' * 3)
    pprint(my_list)


def main():
    """read json and yaml files and pretty print out"""
    yaml_file = 'ex6_test.yml'
    json_file = 'ex6_test.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, ' YAML')
    output_format(json_list, ' JSON')
    print('\n')


if __name__ == "__main__":
    main()


