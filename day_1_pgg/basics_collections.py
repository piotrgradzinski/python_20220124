"""
Kolekcje (ang. collections)
- tupla, krotka (ang. tuple)
- lista (ang. list)
- slownik (ang. dictionary, dict)
- zbior (ang. set)
"""

"""
Tupla, krotka
- https://realpython.com/python-lists-tuples/
- niemutowalna (immutable) - po stworzeniu tupli nie mozemy jej zmienic
- jest uporzadkowana (ordered) - tupla zachowuje elementy w takiej kolejnosci jak do niej dodalismy
"""

#           0      1        2   - indeks
my_tuple = ("Ala", "Tomek", "Krysia")

print(my_tuple)
print(type(my_tuple))

# dostep do elementow
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
# print(my_tuple[3])  # IndexError

#           0      1  2     3     4
my_tuple = ("Ala", 1, 3.14, True, (10, 20, 30))
#                                  0   1   2

print(my_tuple[4][1])
print(my_tuple[4])

my_tuple = 100, 200, 300  # tez bedzie tupla
print(my_tuple)
print(type(my_tuple))
# my_tuple[3] = 400  # TypeError
# my_tuple[0] = 1  # TypeError

my_tuple2 = my_tuple + (1,2,3)
print(my_tuple2)

print('-' * 60)

"""
indexing operator
kolecja[index]
kolekcja[start:stop:krok] - lewostronnie domkniety, prawostronnie otwarty
"""
#                0    1    2    3    4    5    6    7    8    9 - indeksy
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#                -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(letters_tuple[0])
print(letters_tuple[1:3])  # b, c
print(letters_tuple[1:])  # b-j
print(letters_tuple[-1])
print(letters_tuple[-9])
print(letters_tuple[-6:-1])
print(letters_tuple[1:-1])
print(letters_tuple[-3:])
print(letters_tuple[:-1])
print(letters_tuple[::2])
print(letters_tuple[::-1])

print(len(letters_tuple))
print('a' in letters_tuple)  # True 
print('z' in letters_tuple)  # False

print('a' not in letters_tuple)  # False
print('z' not in letters_tuple)  # True

print(min(letters_tuple))
print(max(letters_tuple))

print(letters_tuple * 3)


i = 0
while i < len(letters_tuple):
    print(f'Element tupli: {letters_tuple[i]}')
    i += 1


print('---')

for x in letters_tuple:
    print(x)


"""
Lista
- jest mutowalna, mozemy po utworzeniu ja zmieniac
- uzywamy do niej []
"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list)
print(type(my_list))

my_list[0] = 1
print(my_list)

my_list.append(110)
print(my_list)

del(my_list[-1])

print(my_list)

my_list.insert(1, 12)
print(my_list)

my_list[2:5] = [-1, -2]
print(my_list)

my_list[0:2] = [-10, -20, -30, -40]
print(my_list)

second_list = [1000, 2000, 3000]
my_list.extend(second_list)
print(my_list)

after_tax = [x * 0.1 for x in my_list]  # list comprehension
print(after_tax)

print('-' * 60)

from pprint import pprint

"""
Slownik (dict)
- struktura ktora zawiera klucze i wartosci
"""
my_dict = {
    'first_name': 'Piotr',
    'last_name': 'GG',
    'shoe_number': 46, 
    1: 100,
    2: 200,
    3: [10, 20, 30, 40],
    4: {
        'number': 123
    },
    5: None,
}

print(my_dict)
pprint(my_dict)
print(my_dict['first_name'])
print(my_dict[3])
print(my_dict[3][1])
my_dict['address'] = 'ul. Polna 1'
print(my_dict)

# print(my_dict['company_name'])  # KeyError

print('company_name' in my_dict)
print('first_name' in my_dict)

if 'company_name' in my_dict:
    print(my_dict['company_name'])

company_name = my_dict.get('company_name')  # zwroci None jak nie ma takiego klucza w slowniku, nie bedzie wyjatku
print(company_name)

company_name = my_dict.get('company_name', 'Unknown')
print(company_name)

print('Piotr' in my_dict.values())

# Standardardowo iterujemy po kluczach
for key in my_dict:
    print(key, my_dict[key])

print('---')

# Iterowanie po wartosciach ze slownika
for value in my_dict.values():
    print(value)

print('---')

# Iterowanie po kluczach i wartosciach na raz
# key, value = ('first_name', 'Piotr')
for key, value in my_dict.items():
    print(key, value)

print('---')

"""
Rozpakowywanie kolekcji na wiele zmiennych (unpacking).
Jezeli wymiery sie nie zgadzaja to bedzie ValueError.
"""
a, b = 10, 20
a, b = (10, 20)
a, b = [10, 20]
print(a)
print(b)

print(my_dict.items())  # items oddaje list?? tupli [(klucz, wartosc), (klucz, wartosc), ...]


print('-' * 60)

"""
Co moze byc kluczem w slowniku? Prawie wszystko :)
- generalnie typy niemutowalne
- kluczami w slowniku moga byc tylko takie obiekty, ktore posiadaja zaimplementowana metode __hash__
- tzw. typy hashowalne
"""
my_dict = {
    'first_name': 'Piotr',
    'last_name': 'GG', 
    0: [-1, -2, -3, -4],
    1: [10, 20, 30, 40],
    3.14: 'liczba ulamkowa',
    False: 'wartosc False',
    True: 'wartosc True',
    (1,2,3): 'tupla',
    # [10, 20, 30]: 'lista'
}

pprint(my_dict)
print(my_dict[(1,2,3)])
print('ala ma kota'.upper())  # wszystkie operacje na napisach powoduja utworzenie nowego napisu

print('first_name'.__hash__())  # -41554381053546126
print((0).__hash__())  # 0
print(3.14.__hash__())  # 322818021289917443
print(False.__hash__())  # 0
print((1,2,3).__hash__())  # 529344067295497451
# print([1,2,3].__hash__())  # lista nie ma metody hash - rzuca wyjatkiem

print(my_dict[0])
print(my_dict[False])

print('-' * 60)


"""
Slownik domyslny
"""
from collections import defaultdict
my_def_dict = defaultdict(float)
print(my_def_dict)

my_def_dict['unit_price'] += 30.5

print(my_def_dict)
print(my_def_dict['standard_price'])

print('-' * 60)

"""
Ziory (ang. set)
"""

my_set = {10, 20, 30, 40, 50}
print(my_set)
print(type(my_set))
# print(my_set[0])  # TypeError: 'set' object is not subscriptable
my_set.add(60)
print(my_set)
my_set.remove(10)
print(my_set)

print('-' * 60)

"""
Operacje teoriomnogosciowe na zbiorach
"""

a = {1, 2, 3}
b = {1, 2, 4, 5}

# suma
print(a.union(b))
print(a | b)

# czesc wspolna - iloczyn
print(a.intersection(b))
print(a & b)

# roznica - od a odejme b
print(a - b)
print(a.difference(b))

# roznica symetryczna zbiorow - od sumy zbiorow odejmujemy czesc wspolna
print(a.symmetric_difference(b))
print(a ^ b)

# czy a jest podzbiorem b
print(a < b)
c = {1, 2}
print(c < a)

print('-' * 60)

"""
Konwersja jednej kolekcji na druga
"""

my_list = [1, 2, 3, 3, 3, 1, 1, 2, 10, -1, 10, 5]
print(my_list)

set_based_on_list = set(my_list)
print(set_based_on_list)

my_list = list(set_based_on_list)
print(my_list)

my_list = list("Ala ma kota")
print(my_list)

my_set = set("Ala ma kota")
print(my_set)


for i in range(0, 11):
    print(i)

print('---')

my_range = iter(range(0, 6))

print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
# print(next(my_range))  # StopIteration


my_numbers = list(range(0, 6))
print(my_numbers)

my_numbers = list(range(11, 0, -1))
print(my_numbers)
