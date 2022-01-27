"""
Napisz program wypisujący na konsolę zawartość pliku (emails.txt) wraz z numerami linii.

Przykład użycia:
1: pierwsza linia pliku
2: druga linia pliku
"""

file_name = 'day_4_pgg/emails.txt'

with open(file_name) as file_handle:
    # wersja 1 
    line_number = 1
    for line in file_handle:
        # print(f'{line_number}: {line.rstrip()}')
        print(f'{line_number}: {line[:-1]}')
        line_number += 1 

    print('---')

    # wersja 2
    file_handle.seek(0)
    for line_number, line in enumerate(file_handle, start=1):
        print(f'{line_number}: {line[:-1]}')

    print('---')

    # wersja 3
    file_handle.seek(0)
    line_number = 1
    while True:
        line = file_handle.readline()

        if not line:
            break

        print(f'{line_number}: {line.rstrip()}')
        line_number += 1



