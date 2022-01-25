"""
Uzyteczne funkcje do operowania na kolekcjach
"""

names = ['Piotr', 'Ala', 'Ela', 'Tomek']

for index, name in enumerate(names):
    print(index, name)

print('---')

for index, name in enumerate(names, start=1):
    print(f'{index}. {name}')

print('---')

names = ['Piotr', 'Ala', 'Ela', 'Tomek']
salaries = [100, 500, 1500, 80]

"""
zip - kolekcje musza miec te sama dlugosc
zip_longest - nie musza miec tej samej dlugosci
"""
for name, salary in zip(names, salaries): 
    print(name, salary)

print('---')

from itertools import zip_longest

names = ['Piotr', 'Ala', 'Ela', 'Tomek', 'Krysia', 'Zosia']
salaries = [100, 500, 1500, 80]
for name, salary in zip_longest(names, salaries): 
    print(name, salary)