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
- self - odniesienie do obiektu, na ktorym dana metoda jest wywolana, w innych jezykach to this
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

print(piotr_gg)  # przed zaimplementowaniem __str__: <__main__.Person object at 0x7fe7c805bca0>


print('-' * 60)


"""
Paradygmaty programowania obiektowego (https://pl.wikipedia.org/wiki/Programowanie_obiektowe)
- abstrakcja
- hermetyzacja - ukrywanie implementacji
- dziedziczenie
- polimorfizm

nazwy atrybutow i metod
- bez podkreslenia - atrybut/metoda publiczna (public)
- jedno podkreslenie - atrybut/metoda chroniona (protected)
- dwa podkreslenia - atrybut/metoda prywatna (private) - przy takich atrybutach Python zmienia te 
    nazwe gdybysmy sie chcieli dostac do niej z zewnetrz na _KLASA__atrybut - to sie nazywa name mangling

Kiedy obiekt jednej klasy zawiera w sobie obiekty innych klas.
- agregacja - na diagramie klas oznaczamy pustym rombem, "zawiera", Zajecia / Student
- kompozycja - na diagramie klas oznaczamy pelnym rombem, "posiada", Dom / Pokoj
"""

class Group:
    def __init__(self, group_name: str) -> None:
        self.group_name = group_name
        self.__group_members = []

    def add_person(self, person: Person):
        self.__group_members.append(person)

    def whos_in_the_group(self):
        print(f'{self.group_name} group members:')
        for member in self.__group_members:
            print(member)


piotr_gg = Person('Piotr', 'GG')
marek_kowalski = Person('Marek', 'Kowalski')

family_group = Group('family')
family_group.add_person(piotr_gg)
family_group.add_person(marek_kowalski)

family_group.whos_in_the_group()
print(family_group.group_name)
# print(family_group.__group_members)
print(family_group._Group__group_members)

print('-' * 60)

import datetime
from dateutil.relativedelta import relativedelta


"""
wlasciwosc / property - wyliczane atrybuty, 
"""

class Person:
    def __init__(self, person_first_name, person_last_name, date_of_birth: str) -> None:
        self.first_name = person_first_name
        self.last_name = person_last_name
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'Person ({self.get_full_name()})'

    @property
    def age(self) -> int:
        # return datetime.datetime.now().year - self.date_of_birth.year
        # mozemy zwracac caly obiekt relateviedelta albo tylko liczbe lat
        return relativedelta(datetime.datetime.now(), self.date_of_birth).years


piotr_gg = Person('Piotr', 'GG', "1970-01-01")
print(piotr_gg.date_of_birth.year)
print(piotr_gg.date_of_birth.month)
print(piotr_gg.date_of_birth.day)
print(piotr_gg.date_of_birth.strftime('%d.%m.%Y'))

print(piotr_gg.first_name)
print(piotr_gg.age)