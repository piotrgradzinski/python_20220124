"""
Dodajmy przekazywanie nazwy pliku do otwarcia z poziomu sys.argv.
Niech program przyjmuje dwa argumenty: 
- nazwe pliku do odczytania
- nazwe pliku, do ktorego ma zapisac wynik

uruchomienie: python ex_2_argv.py emails.txt emails_cleaned.txt
"""
import re
import sys

try:
    file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    emails = set()

    with open(file_name) as file_handle:
        for line in file_handle:
            if line.count('@') != 1:
                continue

            email_address = line.strip().lower().replace(' ', '')
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address):
                emails.add(email_address)
        
    sorted_emails = sorted(emails)

    with open(output_file_name, 'w') as file_handle:
        file_handle.write('\n'.join(sorted_emails))
except IndexError:
    print('Usage: python ex_2_argv.py SOURCE_FILE OUTPUT_FILE')
    exit(1)
except FileNotFoundError:
    print(f'File not found.')
    exit(1)
