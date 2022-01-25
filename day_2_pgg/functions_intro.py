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

