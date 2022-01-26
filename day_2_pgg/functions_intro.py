"""
Funkcje
- type-hinting - podpowiedz jakiego typu beda argumenty lub wartosc jaka funkcja bedzie zwracac
- docstring
"""


def say_hello(first_name: str, last_name: str) -> None:
    """Says hello.
    
    Prints Hello first_name last_name.

    :param first_name: First name to greet
    :param last_name: Last name to greet
    :return:
    """
    print(f"Hello {first_name} {last_name}!")


say_hello('Piotr', 'GG')
say_hello('Ala', 'Nowak')

my_first_name = 'Krysia'
my_last_name = 'Kowalska'
say_hello(my_first_name, my_last_name)
say_hello(44, 55)

print('---')

from typing import Union

# def adder(a: int, b: int) -> int:
def adder(a: Union[int, float, str, list], b: Union[int, float, str, list]) -> Union[int, float, str, list]:
    return a + b

result = adder(2.7, 5.1)
print(result)

result = adder("Ala", "kot")
print(result)

result = adder([1,2,3], [4,5,6])
print(result)

print('---')

def funny_multiplier(a: int, b: int) -> int:
    return a * b  # return oznacza natychmiastowe zwrocenie wartosci i wyjscie z funkcji!
    print("Ala ma kota")


result = funny_multiplier(2, 3)
print(result)

print('---')

def funny_multiplier(a: int, b: int) -> int:
    if a > 0:
        return a * b
    else:
        return a * b * 123


result = funny_multiplier(2, 3)
print(result)

result = funny_multiplier(-10, 3)
print(result)

print('---')

# zwracanie z funkcji wielu wartosci
def add_and_multiply(a: int, b: int):
    return a + b, a * b

result_sum, result_mul = add_and_multiply(2, 3)
print(result_sum)
print(result_mul)

print(add_and_multiply(2, 3))
print(type(add_and_multiply(2, 3)))  # po prostu zwracamy tuple z kilkoma wartosciami

print('-' * 60)

"""
Argumenty w funkcjach
- na poziomie definicji funkcji
    - czesc argumentow moze posiadac wartosci domyslne
- na poziomie uruchomienia funkcji
    - nie musze podawac wartosci dla argumentow, ktore posiadaja zdefiniowane wartosci domyslne
    - wywolania pozycyjne
    - wywolania nazwane
    - wywolanie pozycjne i nazwane razem - najpierw pozycyjne, pozniej nazwane
"""

def wrapper(string_to_wrap: str, prefix: str = '>>', suffix: str = '<<') -> str:
    return f'{prefix}{string_to_wrap}{suffix}'


# wywolania pozycyjne
print(wrapper('Ala ma kota'))
print(wrapper('Ala ma kota', '!!'))
print(wrapper('Ala ma kota', '!!', '??'))
print(wrapper('Ala ma kota', '>>', '<<'))

# wywolania nazwane
print(wrapper(string_to_wrap='Ala ma kota', prefix='!!', suffix='@@'))
print(wrapper(suffix='@@', prefix='!!', string_to_wrap='Ala ma kota'))
print(wrapper(suffix='@@', string_to_wrap='Ala ma kota'))

# wywolanie pozycyjne i nazwane
print(wrapper('Ala ma kota', suffix='@@'))
print('asd', 'aaa', 'bbb', sep='<->')


print('-' * 60)

"""
W jaki sposob przekazac do funkcji wiele argumentow?
"""

print(1, 2, 43, 6 , 123, 123, 65, 2, 2, 4, 56, 7, 5, 3, 2, sep='---')

print('---')

"""
args - tupla z wszystkimi argumentami pozycyjnymi
kwargs (key-worded arguments) - slownik z wszystkimi argumentami nazwanymi
"""
def counter(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


counter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('---')
counter(a=1, b=2, c=3, d=4)
print('---')
counter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3, d=4)

print('---')

print(1, 2, 43, 6 , 123, 123, 65, 2, 2, 4, 56, 7, 5, 3, 2, sep='\'')
print(1, 2, 43, 6 , 123, 123, 65, 2, 2, 4, 56, 7, 5, 3, 2, sep="\"")
print(1, 2, 43, 6 , 123, 123, 65, 2, 2, 4, 56, 7, 5, 3, 2, sep='"')
print(1, 2, 43, 6 , 123, 123, 65, 2, 2, 4, 56, 7, 5, 3, 2, sep="'")


print('-' * 60)

"""
Funkcje lambda
- https://realpython.com/python-lambda/
- https://en.wikipedia.org/wiki/First-class_function 
- This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.
- lambda argument1, argument2, ...: wartosc zwracana
"""

def square(number):
    return number ** 2

print(square(4))


square_lambda = lambda number: number ** 2
print(square_lambda(4))

print(square(10))

my_variable = square
print(my_variable(5))
print(my_variable is square)

"""
obszar 1 (stos, stack)                                    obszar 2 (stera, heap)
square = wartosc jest pod adresem 123                     adres 123: funkcja ...
my_variable = wartosc jest pod adresem 123
"""

print('-' * 60)

"""
Funkcje jako kolejny typ danych.
- funkcje mozemy traktowac jako kolejny typ danych
- przypisywac referencje na funkcje do roznych zmiennych
- funkcje mozemy przekazac jako argument do innej funkcji
"""


def executor(function_to_execute):
    print('Uruchamiam executor')
    function_to_execute()
    print('Koncze executor')


def my_function():
    print('Ala ma kota')

executor(my_function)

executor(lambda: print('Kot ma kompilator'))

print('---')

def calculate_vat(amount):
    return amount * 1.23

invoices = [10, 20, 30, 40, 50]
invoices2 = [100, 200, 300, 400, 500]
invoices_with_vat = []

for amount in invoices:
    invoices_with_vat.append(calculate_vat(amount))

print(invoices)
print(invoices_with_vat)

for x in map(calculate_vat, invoices):
    print(x)


invoices_with_vat = list(map(calculate_vat, invoices))
print(invoices_with_vat)

print('---')

tmp_iter = map(calculate_vat, invoices)
print(next(tmp_iter))
print(next(tmp_iter))
print(next(tmp_iter))
print(next(tmp_iter))
print(next(tmp_iter))
# print(next(tmp_iter))  # StopIteration

print('---')

"""
any()
https://docs.python.org/3/library/functions.html?highlight=any#any
"""
my_list = [None, [], '', 0, False]
print(any(my_list))  # False

my_list = [None, [], '', 0, False, 12]
print(any(my_list))  # True

print('---')

"""
all()
https://docs.python.org/3/library/functions.html?highlight=any#all
"""
my_list = [1, 'asd', [1,2,3], True]
print(all(my_list))  # True

my_list = [1, 'asd', [1,2,3], True, 0]
print(all(my_list))  # False

print('-' * 60)

"""
filter()
https://docs.python.org/3/library/functions.html#filter
"""

my_list = [-10, 3, 5, -2, 0, 15]

only_positive = list(filter(lambda x: x > 0, my_list))
print(only_positive)

print('---')

"""
reduce()
https://realpython.com/python-reduce-function/
"""
from functools import reduce

my_list = [-10, 3, 5, -2, 0, 15]
my_sum = reduce(lambda a, b: a + b, my_list)
print(my_sum)  # 11

print('---')

"""
Sortowanie list
"""

my_list = [(2, 2), (3, 4), (4, 1), (1, 3)]

print(my_list)

# my_list.sort()
my_list.sort(key=lambda element: element[1])

print(my_list)

print('---')

from functools import cmp_to_key

def comparer(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1


my_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(my_list)
my_list.sort(key=cmp_to_key(comparer))
print(my_list)

print('---')

"""
Zasiegi
https://realpython.com/python-scope-legb-rule/ 

W pythonie mamy 4 zasiegi:
- Built-in scope
    - Global (or module) scope
        - Enclosing (or nonlocal) scope
            - Local (or function) scope


locals() - https://docs.python.org/3/library/functions.html#locals
dir() - https://docs.python.org/3/library/functions.html#dir

z zasiegu lokalnego moge siegac do globalnego (albo innego wyzszego zasiegu), ale nie odwrotnie
"""

from pprint import pprint

print(dict)
empty_dict = dict()
print(empty_dict)

pprint(dir())

# jezeli odkomentuje ten kod, to nie bede mogl korzystac ze slownika, zastepuje wbudowany slownik w Pythona napisem 'Ala ma kota'
# dict = 'Ala ma kota'
# empty_dict = dict()
# print(empty_dict)

print('-' * 60)

a = 1

def fun_1():
    a = 1000  # stworzylismy zmienna lokalna w zasiegu lokalnym (funkcyjnym)
    print(f'fun_1 a={a}')


print(f'global a={a}')
fun_1()
print(f'global a={a}')


print('-' * 60)

a = 1

def fun_1(a):
    print(f'fun_1 a={a}')


print(f'global a={a}')
fun_1(15)
print(f'global a={a}')

print('-' * 60)

a = [1, 2, 3]

def fun_1(my_list):
    # w pythonie argumenty przekazywane sa przez referencje, czyli moze modyfikowac obiektu mutowalne, dostajemy sie do oryginalnego obiektu a nie operujemy na kopii
    my_list.append(4)
    print(f'fun_1 my_list={my_list}')


print(f'global a={a}')
fun_1(a)
print(f'global a={a}')


print('-' * 60)

a = 1

def fun_1(x1, x2):
    a = 100
    print(f'fun_1 a={a}')
    print(f'x1 = {x1}')

    def fun_2():
        a = 1000
        print(f'fun_2 a={a}')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')

    fun_2()
    print(f'fun_1 a={a}')



print(f'global a={a}')
fun_1(-10, -20)
print(f'global a={a}')

print('-' * 60)

"""
Wartosci domyslne, ktore nie sa typami niemutowalnymi
Wartosciami domyslnymi powinny byc tylko wartosci typow niemutowalnych. 
W przeciwnym wypadku, kazde uruchomienie funkcji bedzie dostawala ta sama wartosc domyslna, 
czyli w naszym przypadku, caly czas te sama liste.
"""
def tax_fun(tax, list_of_taxes = None):
    # list_of_taxes = list_of_taxes or []  # The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
    if list_of_taxes is None:
        list_of_taxes = []

    print('tax_fun', list_of_taxes)
    list_of_taxes.append(tax)

    return list_of_taxes


result = tax_fun(23, [10,20,30])
print('result', result)

result = tax_fun(8)
print('result', result)

result = tax_fun(12)
print('result', result)