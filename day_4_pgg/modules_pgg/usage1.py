import sys
import tools  # importuje plik tools.py z aktualnego katalogu
import datetime
from pprint import pprint

print('\n'.join(sys.path))  # dane pobrane ze zmiennej srodowiskowej PYTHONPATH

"""
Przy takim sposobie importu, zeby wykorzystac kod z modulu tools musze go prefiksowac nazwa modulu.
"""

print(tools.adder(2, 3))
print(datetime.datetime.now())

pprint(locals())  # mamy tools