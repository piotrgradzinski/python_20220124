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

