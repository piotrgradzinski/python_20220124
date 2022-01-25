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

my_str = "Ala ma kota"
for letter in my_str:
    print(letter)
