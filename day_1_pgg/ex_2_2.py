"""
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich
liczb wprowadzonych liczb przez użytkownika.

Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią 
komendą (np. KONIEC).

Jak to zrobimy?
- zdefiniujmy dwie zmienne do trzymania minimum i maximum z wprowadzonych liczb, 
ale na poczatku przypiszemy None
- w nieskończonej petli while bede wczytywal dane od uzytkownika, sprawdze 
czy wpisal KONIEC i wtedy przerwe petle
- jeśli nie KONIEC, to sprawdze czy podana liczba jest mniejsza niz minimum, 
czy jest wieksza niz maksimum,
  jesli tak, to przypisze nowe wartosci
- jesli w zmiennej minimum, maksimum jest None, to tez przypisze te wartosc
"""

found_min = None
found_max = None

while True:
    input_data = input('Podaj liczbe lub KONIEC: ')
    if input_data == 'KONIEC':
        break

    # jak poradzic sobie z uzytkownikiem, ktory nie wprowadzi porpawnych danych
    try: 
        provided_number = float(input_data)

        if found_min == None or provided_number < found_min:
            found_min = provided_number

        if found_max == None or provided_number > found_max:
            found_max = provided_number
    except ValueError:
        print('Podales nieprawidlowa wartosc!!!')
        continue
        

if found_min is None or found_max is None:
    print('Nie podales zadnych liczb!!!')
else:
    print(f'min = {found_min}, max = {found_max}')


"""
Roznica miedzy is a ==
== - porownuje wartosci
is - porownuje tozsamosc

Referencje - adres w pamieci komputera

first_name = "Piotr"

obszar 1 (stos, stack)                                    obszar 2 (stera, heap)
first_name = wartosc jest pod adresem 123                 adres 123: "Piotr"
first_name2 = wartosc jest pod adresem 123

first_name == first_name2 -> True
first_name is first_name2 -> True

---
                                                          adres 1: None
first_name = wartosc jest pod adresem 123                 adres 123: "Piotr"
first_name2 = wartosc jest pod adresem 345                adres 345: "Piotr"

first_name == first_name2 -> True
first_name is first_name2 -> False
"""