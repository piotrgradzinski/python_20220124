"""
argparse
https://docs.python.org/3/library/argparse.html
https://realpython.com/command-line-interfaces-python-argparse
"""

import argparse

parser = argparse.ArgumentParser('argparse_intro.py')
parser.add_argument('file_name', nargs='+', help='Path to the file to read.')
parser.add_argument('-s', '--safe-mode', action='store_true', help='Safe mode, no db changes.')
parser.add_argument('-l', '--start-with-line', type=int, default=1, help='Start numbering lines with this number. Default 1.')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output verbosity.')

arguments = parser.parse_args()
print(arguments)
print(arguments.file_name)
