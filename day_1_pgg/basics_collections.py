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

