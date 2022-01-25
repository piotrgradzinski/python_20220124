"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych 
przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi
w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.
"""

even_numbers = set(range(0, 101, 2))

user_numbers = set()

while True:
    number = input('Podaj liczbe calkowita lub KONIEC: ')
    if number.upper() == 'KONIEC':
        break

    user_numbers.add(int(number))


print(f'Unikalnych liczb = {len(user_numbers)}')
print(f'Wprowadzone parzyste liczby od 0 do 100 = {even_numbers & user_numbers}')
print(f'Liczba parzystych liczba od 0 do 100 = {len(even_numbers & user_numbers)}')
