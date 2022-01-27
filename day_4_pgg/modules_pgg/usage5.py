"""
Importowanie zastepuje nam istniejaca zmienne, funkcje, klasy, dlatego powinnismy robic
importy na samym poczatku pliku, zeby nie bylo problemu takiego jak tutaj.
"""
from pprint import pprint

my_string = "Pan Tadeusz"

print(my_string)
pprint(locals())

from tools import my_string

print(my_string)
pprint(locals())