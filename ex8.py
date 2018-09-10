#!/usr/bin/env python
"""
write a program that parses the 'config.txt' file.
The script should find all crypto map entries in the file
that begin with 'crypto map CRYPTO' and print the children
of each crypto map.
"""

from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse


def main():
    """
    find all crypto map entries nad print the children
    """
    cisco_file = 'config.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    for c_map in crypto_maps:
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)
    print()


if __name__ == "__main__":
    main()


