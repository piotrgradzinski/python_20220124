"""
Multi-line comment, tzw. docstring
line1
line2
"""

# Comment

# Python data types

# str
print("Ala ma kota")
print('Ala ma kota')

# multi-line string literals (literal)
print('''Ala
ma 
kota
''')
print("""Ala
ma
kota
""")

# int - nieograczony
print(3)
print(-1)

# float 
print(3.14)
print(-8.5)
print(0.5)
print(.5)

print(3E5)  # notacja naukowa 3*10^5

# liczby zespolone 
# <czesc rzeczywista>+<czesc urojona>j
print(3+5j)
print(type(3+5j))

# bool
print(True)
print(False)

# None - NULL, wartość oznaczajaca brak wartosci
print(None)


print(10)
print(10.0)
print("10")

print(type(10))
print(type(10.0))
print(type("10"))

# print("10" * "5")  # can't multiply sequence by non-int of type 'str'

# Operatory
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(11 / 3)
print(11 // 3)  # // -> dzielenie calkowitoliczbowe, ucina czesc ulamkowa, 
print(10 ** 3)  # operator potegowania
print(10 % 3)  # reszta z dzielenia

print("Ala " + "ma kota")  # konkatenacja
print("Ala " * 3)

# Zmienne
"""
- staramy sie pisac po angielsku
- nazwy zmiennej nie zaczynamy od liczby
- poszczegolne slowa, w nazwie zmiennej, rozdzielamy _
- PEP8 - Style guide for Python https://www.python.org/dev/peps/pep-0008/
- python jest jezykiem slabo typowanym
- type hinting pozwala nam na okreslenie podpowiedzie, jakiego typu dane chcemy przechowywac w zmiennej, czy przekazywac do funkcji
"""

first_name:str = "Piotr"  # snake_case
firstName = "Piotr"  # camelCase w pythonie tak nie nazywamy zmiennych
print(first_name)
print(firstName)

first_name = 44
print(first_name)

# przerabianie typow
my_number = int("10")
print(my_number)
print(type(my_number))

"""
Obsluga dat
- wczytujemy dane - np. z csv "2022-01-24 11:05:00"
- strptime("2022-01-24 11:05:00", "%Y-%m-%d %H:%M:%S") -> obiekt datetime
- mozemy taki obiekt przerobic na napis poprzez strftime("%Y-%m-%d %H:%M:%S")
"""

user_age = int(input("Podaj swoj wiek: "))
print(user_age)
print(type(user_age))
