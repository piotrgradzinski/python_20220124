"""
Dodajmy do tego pliku obsluge argumentow przez argparse.

Argumenty:
- file - plik ktory bedziemy czytac
- -s --start-with - poczatkowy numer od ktorego wyswietlamy wiersze, domyslnie 1
- -n --hide-line-numbers - ukrywa wyswietlanie numerow linii
"""

file_name = 'day_4_pgg/emails.txt'

with open(file_name) as file_handle:
    for line_number, line in enumerate(file_handle, start=1):
        print(f'{line_number}: {line[:-1]}')
