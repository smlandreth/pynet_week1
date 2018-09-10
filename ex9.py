#!/usr/bin/env python
"""
write a program that finds crypto maps that use PFS group 2
"""

from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse


def main():
    """
    find all crypto map entries that are using pfs group 2
    """
    cisco_file = 'config.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO',
                                                childspec=r'pfs group2')
    print("\nCrypto Maps using PFS group2:")
    for entry in crypto_maps:
        print("  {}".format(entry.text))
    print()


if __name__ == "__main__":
    main()


