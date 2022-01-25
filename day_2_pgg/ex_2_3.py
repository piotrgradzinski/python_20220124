"""
Napisz program zliczający liczbę wystąpień każdego znaku
w podanym przez użytkownika napisie.


1. Robimy pusty słownik, w którym będziemy zliczać litery
2. Wczytujemy napis od użytkownika
3. Przechodzimy przez wszystkie znaki (for)
  3a. jesli nie ma danego znaku w slowniku to dodajemy
  4b. jezeli jest to zwiększamy liczbe o 1


slownik
klucz  => wartość
litera => liczba wystąpień (int)

Trzeba sprawdzić czy dana litera wystepuje w slowniku!

Od biznesu: wielkość liter nie ma znaczenia.
"""
from collections import defaultdict

user_input = input('Podaj napis: ')
occurences = defaultdict(int)

for letter in user_input.lower():  # Ala ma kota
    # Dzieki temu, ze uzywamy domyslnego slownika, nie musimy sprawdzac czy klucz w nim istnieje.
    occurences[letter] += 1

for letter, number in occurences.items():
    print(f'{letter} = {number}')
