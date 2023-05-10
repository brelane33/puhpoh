#!/usr/bin/env python3

import argparse
import sys

"""
Main

Example: python -m puhpoh
"""

if __name__ == "__main__":
    """
    Running examples:

    $ ./puhpoh.py -h
    usage: puhpoh.py [-h]      --strparam STR [--boolparam]
                               [--intparam INTPARAM] [--append APPEND_LIST]
    """

    print("Welcome to puhpoh!")
    parser = argparse.ArgumentParser(description="puhpoh!")
    parser.add_argument("--engine", "-e", dest="engine", type=str, action="store", default="", required=False, help="String parameter of what engine you'd like to use")
    parser.add_argument("--model", "-m", dest="model", type=str, action="store", default="", help="String parameter of what AI model to use")
    parser.add_argument("--max_tokens", "-i", dest="max_tokens", type=int, action="store", default=0, help="Number of maximum tokens for your AI transaction")
    parser.add_argument("--messages", "-p", dest="user_message", type=str, action="store", default="", help="Message to complete")
    args = parser.parse_args(sys.argv[1:])

    print(args)
