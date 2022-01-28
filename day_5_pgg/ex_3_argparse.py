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


file_name = 'day_4_pgg/emails.txt'

with open(file_name) as file_handle:
    for line_number, line in enumerate(file_handle, start=1):
        print(f'{line_number}: {line[:-1]}')
