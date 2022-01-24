"""
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy. 
Skorzystaj z funkcji wbudowanej sum().

Pozwól na wprowadzenie maksymalnie 10 liczb.

- zasilanie listy danymi
- policzenie sredniej
- wyswietlenie wynikow
"""


numbers = []

while len(numbers) < 10:
# while True:  # wersja z dowolna liczba liczb
    input_data = input('Podaj liczbe lub KONIEC: ')

    if input_data.lower() == 'koniec':
        break

    try:
        number = int(input_data)
        numbers.append(number)
    except ValueError:
        print('Niepoprawna liczba, sprobuj jeszcze raz.')
        continue

average = sum(numbers) / len(numbers)
print(f'Srednia z wprowadzonych liczb to {average:.2f}')
