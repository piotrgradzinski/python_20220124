"""
Dodajmy przekazywanie nazwy pliku do otwarcia z poziomu sys.argv.
Niech program przyjmuje dwa argumenty: 
- nazwe pliku do odczytania
- nazwe pliku, do ktorego ma zapisac wynik
"""
import re

file_name = 'day_5_pgg/emails.txt'

emails = set()

with open(file_name) as file_handle:
    for line in file_handle:
        if line.count('@') != 1:
            continue

        email_address = line.strip().lower().replace(' ', '')
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address):
            emails.add(email_address)
    
sorted_emails = sorted(emails)

with open('day_5_pgg/emails_cleaned.txt', 'w') as file_handle:
    file_handle.write('\n'.join(sorted_emails))
