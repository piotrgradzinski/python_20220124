"""
OOP - Object Oriented Programming
Klasa - przepis na to jak zrobić obiekt
Obiekt - instancja klasy, twor ktory z klasy powstaje, i jest odzwierciedleniem schematu
nazwa klasy - PascalCase
"""

piotr_gg = {
    'first_name': 'Piotr',
    'last_name': 'GG',
}

def get_full_name(person: dict) -> str:
    return f'{person["first_name"]} {person["last_name"]}'

print(get_full_name(piotr_gg))

print('---')

marek = {
    'first_name': 'Marek',
}

# print(get_full_name(marek))  # KeyError: 'last_name'

print('-' * 60)


"""
Z czego sklada sie klasa?
- atrybuty - np. first_name, last_name, itd. Ze to takie zmienne, ale ktore siedza w obiekcie
- metody - np. get_full_name - to nic innego jak funkcje, ktore dzialaja w kontekscie konkretnego obiektu
- __init__ - tzw. dunder method - jest uruchamiana kiedy tworzy sie nowy obiekt danej klasy
- dunder methods - to pewien zestaw wbudowanych na poziomie pythona metod, ktore moga pojawic sie w klasach, i ktore beda mialy pwne okreslone znaczenie
    - lista metod magicznych (dunder methods) z przykladami: https://piotr.gg/python/python3-dunder-methods-summary.html
    - __init__ - uruchamiana przy tworzeniu obiektu
    - __str__ - urchamiana, kiedy python bedzie probowal przerobic nasz obiekt na str
"""

class Person:
    def __init__(self, person_first_name, person_last_name) -> None:
        self.first_name = person_first_name
        self.last_name = person_last_name

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'Person ({self.get_full_name()})'


piotr_gg = Person('Piotr', 'GG')
print(piotr_gg)
print(piotr_gg.first_name)
print(piotr_gg.last_name)
print(piotr_gg.get_full_name())

# print(Person.get_full_name(piotr_gg))

print('---')

print(piotr_gg)  # <__main__.Person object at 0x7fe7c805bca0>
