"""
    htmlx CLI
    ====================================
    - some useful cli commands
"""

import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="htmlx",
        usage="%(prog)s [options]",
        description="Generate HTML with Python 3",
    )
    parser.add_argument("-v", "--version", action="store_true")

    args = parser.parse_args()
    return args


def do_things(arguments):

    if arguments.version is True:
        from htmlx import __version__

        print(__version__)
        return __version__


def run():
    """[Entry point required by setup.py console_scripts. Saves having to add alias to .bash_profile]"""
    args = parse_args()
    do_things(args)


if __name__ == "__main__":
    run()
