"""
Dodajmy do tego pliku obsluge argumentow przez argparse.

Argumenty:
- file - plik ktory bedziemy czytac
- -s --start-with - poczatkowy numer od ktorego wyswietlamy wiersze, domyslnie 1
- -n --hide-line-numbers - ukrywa wyswietlanie numerow linii
"""

import argparse

parser = argparse.ArgumentParser('ex_3_argparse.py')
parser.add_argument('file', type=str, help='File name to process.')
parser.add_argument('-s', '--start-with', type=int, default=1, help='Initial line number. Default 1.')
parser.add_argument('-n', '--hide-line-numbers', action='store_true', help='Hide line numbers.')

arguments = parser.parse_args()

try:
    with open(arguments.file) as file_handle:
        for line_number, line in enumerate(file_handle, start=arguments.start_with):
            # if arguments.hide_line_numbers:
            #     print(line[:-1])
            # else:
            #     print(f'{line_number}: {line[:-1]}')

            print(f'{str(line_number) + ": " if not arguments.hide_line_numbers else ""}{line[:-1]}')
except FileNotFoundError:
    print(f'File {arguments.file} not found.')
    exit(1)
