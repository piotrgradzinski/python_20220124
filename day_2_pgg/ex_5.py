"""
Napisz funkcję zwracającą zbiór wszystkich znaków
występujących w napisie więcej niż zadana liczba razy (domyślnie 2).
Wielkosc znakow nie ma znaczenia.

Przykład użycia:
> more_than('ala ma kota a kot ma ale', 3) -> {'a', ' '}

1. Definiujemy funkcje
2. Policzyc ile jest znakow (.count()) i dodac je do zbioru,
ktory na koncu zwracamy

Przypadki testowe:
???
"""

def more_than(input_string: str, number_of_occurences: int = 2) -> set:
    input_string = input_string.lower()
    result = set()

    for letter in input_string:
        if input_string.count(letter) >= number_of_occurences:
            result.add(letter)

    return result
