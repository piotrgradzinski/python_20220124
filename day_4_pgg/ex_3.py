"""
Napisz program wczytujący listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością.
Wejściowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter, 
linie zawierające białe znaki oraz błędne adresy email (brak znaku @ lub występuje on wiele razy). 
Wynikowy plik powinien zawierać unikalne, posortowane, poprawne adresy email.

https://emailregex.com/
https://regex101.com/ - edytor do wyrazen regularnych
https://realpython.com/regex-python/
https://realpython.com/regex-python-part-2/
r"" - nie bedzie eskejpowal znakow w napisie - https://docs.python.org/3/reference/lexical_analysis.html#literals
"""

import re

file_name = 'day_4_pgg/emails.txt'

emails = set()

with open(file_name) as file_handle:
    for line in file_handle:
        if line.count('@') != 1:
            continue

        email_address = line.strip().lower().replace(' ', '')
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address):
            emails.add(email_address)
    
sorted_emails = sorted(emails)

with open('day_4_pgg/emails_cleaned.txt', 'w') as file_handle:
    file_handle.write('\n'.join(sorted_emails))
