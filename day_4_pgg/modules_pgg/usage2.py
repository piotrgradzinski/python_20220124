# from tools import db_config, adder  # tylko db_config i adder
from tools import *  # wszystkie rzeczy z tools
from pprint import pprint

"""
Importujac przez wyrazenie from MODUL import COS, elementy, ktore importujemy
staja sie od razu dostepne w naszym skrypcie, nie musimy ich prefiksowac nazwa modulu.

from MODULE import * - na takie rozwiazanie trzeba uwazac. Starajmy sie importowac tylko potrzebne rzeczy a nie wszystko.
"""

print(db_config)
print(adder(2, 5))

pprint(locals())
