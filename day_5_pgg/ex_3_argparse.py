"""
Dodajmy do tego pliku obsluge argumentow przez argparse.

Argumenty:
- file - plik ktory bedziemy czytac
- -s --start-with - poczatkowy numer od ktorego wyswietlamy wiersze, domyslnie 1
- -n --hide-line-numbers - ukrywa wyswietlanie numerow linii

Logging:
- dodac argument -v --verbosity, jak w argparse_intro
- jezeli verbosity=1 to logujemy na poziomie WARNING
- jezeli verbosity=2 to logujemy na poziomie DEBUG
- w pozostalych przypadkach poziom CRITICAL
- dodajemy logowanie na roznych poziomach w naszym kodzie
"""

import argparse
import logging

parser = argparse.ArgumentParser('ex_3_argparse.py')
parser.add_argument('file', type=str, help='File name to process.')
parser.add_argument('-s', '--start-with', type=int, default=1, help='Initial line number. Default 1.')
parser.add_argument('-n', '--hide-line-numbers', action='store_true', help='Hide line numbers.')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output verbosity.')
arguments = parser.parse_args()

if arguments.verbosity == 1:
    log_level = logging.WARNING
elif arguments.verbosity == 2:
    log_level = logging.DEBUG
else:
    log_level = logging.CRITICAL

logging.basicConfig(level=log_level, format='%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)d|%(message)s')

try:
    logging.debug(f'Opening file {arguments.file}')
    with open(arguments.file) as file_handle:
        
        logging.debug(f'Processing file {arguments.file}')
        logging.debug(f'Starting with line number: {arguments.start_with}')
        logging.debug(f'Line numbers hidden: {arguments.hide_line_numbers}')

        if arguments.start_with < 1:
            logging.warning(f'Start line number lower than 1: {arguments.start_with}')
            
        for line_number, line in enumerate(file_handle, start=arguments.start_with):
            # if arguments.hide_line_numbers:
            #     print(line[:-1])
            # else:
            #     print(f'{line_number}: {line[:-1]}')

            print(f'{str(line_number) + ": " if not arguments.hide_line_numbers else ""}{line[:-1]}')
        
        logging.debug(f'[COMPLETED] Processing file {arguments.file}')
except FileNotFoundError:
    logging.critical(f'File {arguments.file} not found.')
    print(f'File {arguments.file} not found.')
    exit(1)
